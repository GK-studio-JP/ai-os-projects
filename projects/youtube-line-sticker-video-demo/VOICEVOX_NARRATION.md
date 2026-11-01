# VOICEVOX ナレーション追加 — 実装と検証状態

Status: blocked at real audio generation; API integration prepared and contract-mock tested
Date: 2026-11-01
Project: `youtube-line-sticker-video-demo`

## 利用する制作物と保存先

- 既存 MP4: `/ChatGPT-Transfer/YouTube-Production/projects/line-sticker-howto-20261101/04_exports/line_sticker_youtube_test.mp4`（81秒・H.264/AAC、BGMのみ）
- VOICEVOX連携の新ソース: `/ChatGPT-Transfer/YouTube-Production/projects/line-sticker-howto-20261101/03_source/line_sticker_voicevox_pipeline_v1.zip`（9,581 bytes、SHA-256 `a09d3fc11ac09520fd8ca8452e4ecdee2e5373c67c803772d4dd584882e73457`）
- 追加の実施報告: `/ChatGPT-Transfer/YouTube-Production/projects/line-sticker-howto-20261101/05_qa/VOICEVOX_TEST_REPORT.md`
- 操作説明: `/ChatGPT-Transfer/YouTube-Production/projects/line-sticker-howto-20261101/01_script/VOICEVOX_README_JA.md`

## 設計とOSS選択

公式 VOICEVOX Engine（2026-10-19 v0.26.0）、Windows/Mac/Linux公式VOICEVOX、VOICEVOX CORE Pythonの方法を比較。実際に実装したのはローカルVoicevox Engine HTTP API。GUI書き出しを11回繰り返さず、公式 `GET /speakers`、`POST /audio_query`、`POST /synthesis` を使用。スタイルIDは話者名とスタイル名から起動時に解決する。

`manifest.json` を各シーンの時間の正本、`narration_voicevox.json` を読み上げ専用の短縮原稿の正本とする。既存の編集ソースを上書きせず、VOICEVOX Engine経由のシーン別WAV→48kHz PCM16モノラル81秒タイムライン→元MP4 BGMを0.18倍＋ナレーション1.1倍でミックス→AACエンコード/H.264コピー→`line_sticker_youtube_voicevox_v2.mp4` とする。速すぎる読み上げを防ぐため各シーン内に前後無音、必要に応じて音声を再合成。最大速度を超えても尺に収まらない場合は自動で重ねずエラー停止する。

初期話者：四国めたん・ノーマル。YouTube概要欄へのクレジット `VOICEVOX:四国めたん` が必要。商用利用と音源の規約は `https://www.zunko.jp/con_ongen_kiyaku.html` を公開時に照合。

## 検証済み

- Python構文、11シーン（81秒）プランの読み込み：成功。
- 仮のローカルHTTPサーバーで3 APIエンドポイントの応答を模擬、無音WAV11本から81秒のタイムライン音声を作成し、既存MP4のBGMとFFmpeg合成：成功。
- テスト用の出力は H.264＋AAC 48kHz、81.000秒、全編FFmpegデコード成功。モックサーバーと一時WAV/MP4は後片づけ済み。
- Dropboxの `01_script`、`03_source`、`05_qa` に追加3ファイル保存し、Dropbox一覧で名前とサイズを照合。

## 制約・非実証

- このチャットのLinuxコンテナには VOICEVOX Engine、専用音声モデルがなく、127.0.0.1:50021はConnection refused。外部パッケージのDNS取得も失敗。
- **VOICEVOXによる本物の音声WAVやナレーション付き完成MP4は生成していない。** 模擬HTTPエンジンの無音WAVを実音声と見なしていない。
- 話者発音、抑揚、アクセント、実音声の尺合わせ・聴覚品質は未テスト。
- スマホ本体でVOICEVOX EngineやPythonを実行したわけではない。公式VOICEVOXはPC用であり、現環境からの本物の音声生成にはVOICEVOX Engineが稼働する実行先が必要。
- 完成したv2ファイルが存在しないため `04_exports` は既存のv1を変更していない。
- Dropboxクラウド保存成功と、バイト再ダウンロードSHA検証・PC同期は別。

## 復帰作業

1. 公式VOICEVOXのエンジンをローカルの実行環境に導入し、`http://127.0.0.1:50021` を**外部公開せず**起動。
2. ZIPを展開して `python voicevox_pipeline.py --mode probe` → `python voicevox_pipeline.py --mode all --video <既存MP4> --out <v2 MP4>`。
3. 実11WAV、タイミングJSON、完成MP4を作成し、発音・台本・BGMバランス・クリッピング・全編デコードを人間とツールで確認。
4. Dropboxの `04_exports` へv2新規ファイルとして保存、`05_qa`へ音声検証記録、AIOSプロジェクトを更新。YouTube公開は別承認。
 
## 公式参照

- https://voicevox.hiroshiba.jp/
- https://github.com/VOICEVOX/voicevox_engine
- https://github.com/VOICEVOX/voicevox_core
- https://www.zunko.jp/con_ongen_kiyaku.html

## 2026-11-01 PC利用許可後の実機環境調査（追加）

**状態：VOICEVOX導入・実音声生成は未完了。** Windows PCへの通常接続を確認し、使用できる構成と操作上の不足を実機で調査した。

- AIOS Production MCP稼働（Windows、専用FFmpeg 9.0.2系あり）。PC Edge専用ブラウザ起動・VOICEVOX公式サイト `https://voicevox.hiroshiba.jp/` の表示に成功。公式サイト表示版は0.26.1。
- Windows対象の標準環境：Python 3.12とwingetは存在。標準PATHから`ffmpeg`は見つからないが、AIOS Production MCP専用のFFmpeg実行ファイルは存在する。**専用環境での利用を別途検証すること**。
- VOICEVOX起動中プロセス、通常のプログラムディレクトリのVOICEVOX名付きインストール、127.0.0.1:50021の`/speakers`応答は確認できず。`VOICEVOX_API_UNAVAILABLE`。
- 実PCの`winget search --name VOICEVOX --source winget`で`HiroshibaKazuyuki.VOICEVOX.CPU`、版0.25.2が見つかった（検索時の配布候補、**導入実績ではない**）。VOICEVOX公式ページにはWindows/CPU/x64インストーラーがある。
- PC Edge上の公式ダウンロード選択画面を観測したが、WindowsのDownloadsフォルダに新たなVOICEVOXインストーラーは確認できなかった。**ダウンロード完了・ソフトインストール済み・音声エンジン起動済みとは主張しない**。
- 現行の許可済みPC接続はブラウザ操作・制作専用の型付き処理が中心。一般的なアプリのインストーラ実行や任意のPython/FFmpeg制作コマンドの実行APIは利用できない。保守専用PowerShellやRDCを通常の動画制作ジョブ中継に転用しない。

### 次の実行条件

1. 正規のVOICEVOX Windows CPU版を一度インストールし、実ユーザーのPCでVOICEVOXを起動する。商用利用時のクレジット/利用条件を最新の公式ページで確認。
2. `GET http://127.0.0.1:50021/speakers`が同じWindows実行環境で応答することを確認。外部ネットワークにAPIを公開しない。
3. Dropboxの元MP4と`line_sticker_voicevox_pipeline_v1.zip`を利用可能なローカルフォルダに置く。Dropboxクラウド保存をWindows同期完了と同一視しない。
4. 同一マシンでPython 3.12とFFmpegの実行パスを解決し、`voicevox_pipeline.py --mode probe`、`--mode all`を実行。完成音声11件とMP4の存在・音量・デコード・尺を検証する。
5. Dropboxの`04_exports`へ`line_sticker_youtube_voicevox_v2.mp4`を新規版として保存。既存MP4は上書きしない。

今回の実機調査は**アプリ導入、音声制作、Dropbox同期、v2 MP4出力の成功を含まない**。

### 追補：WinGet導入試行と後処理（2026-11-01）

- ユーザーのPC利用許可に基づき、既存のWinGetから無料CPU版 `HiroshibaKazuyuki.VOICEVOX.CPU` の一度限りの導入を試行。
- Windows保守実行の結果は `maintenance_termination_unverified`（終了検証不可）で、インストール成功を確認できず。同一インストールを**再送していない**。
- 事後調査では、この試行のWinGetプロセスが残留していた。対象パッケージのコマンドライン、元の親プロセス、子プロセス不在を一致検証し、**当該プロセスだけ**を終了。終了確認成功。
- 最終調査ではVOICEVOXのアンインストール登録なし、関連WinGet/VOICEVOX/msiexecの実行プロセスなし。ローカル音声APIも応答せず。VOICEVOX本体の**導入は未完了**。
- 調査資料（Dropbox）：`/ChatGPT-Transfer/YouTube-Production/projects/line-sticker-howto-20261101/05_qa/VOICEVOX_PC_READINESS_20261101.md`。クラウド保存後にファイルサイズ（2450 bytes）を確認。
- 既存MP4、原稿、制作プログラム、AIOS Productionサービスは変更しないまま維持。VOICEVOXの本物の音声は未生成。
- 次に必要なのはユーザー操作可能な正規インストール経路か、VOICEVOXに対応した専用の型付きPC制作経路。保守用PowerShell/RDCを日常の動画合成に使う設計にしない。
