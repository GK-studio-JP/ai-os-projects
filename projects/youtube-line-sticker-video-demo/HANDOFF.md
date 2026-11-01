# YouTube動画制作デモ：LINEスタンプの作り方

Status: active (prototype verified, publication pending)
Status date: 2026-11-01
Project ID: `youtube-line-sticker-video-demo`
Canonical project record: `GK-studio-JP/ai-os-projects/projects/youtube-line-sticker-video-demo/`

## 目的と既存プロジェクトとの境界

スマートフォンで視聴・公開できるYouTube解説動画を、追加の有料AI動画生成サービスに依存せず、ChatGPTで台本を設計しPython/Pillow/NumPy/FFmpegで動画合成する方式で1本通してテストしたもの。今回のテーマは「LINEスタンプの作り方」。

**LINEスタンプそのものを作成・申請する既存プロジェクト `line-stamp-creation` とは別プロジェクト。** こちらは動画制作基盤とYouTubeコンテンツ制作の検証が対象。既存LINEスタンプの原画や申請状態を上書きしない。

## 実証済みの結果（2026-11-01）

- 台本＋絵コンテ11シーン、合計81.0秒、1280×720、24fps。
- オリジナルの猫キャラクター通常スタンプ8枚（370×320 RGBA）＋メイン画像（240×240）＋タブ画像（96×74）を作成。
- 各シーン静止フレーム→軽いズーム＋フェード→H.264動画→結合→自作シンセBGM→AAC→MP4。
- 動画はH.264/AAC、81秒、5,999,216 bytes。全編FFmpegデコードエラーなし。
- シーン一覧とサムネイルを視覚確認。Python構文、ZIP CRC、画像の寸法・RGBAを再確認。
- 元の制作ZIPの日本語ファイル名文字化けを検出し、UTF-8名の新しいZIPを生成。**元ZIPは証跡として維持。**
- 追加の動画生成課金、CapCut契約、スマホ内の動画編集アプリは使用していない。

## 未完了・非実証

- ナレーション原稿は準備済みだが、**日本語読み上げ音声の生成・収録・同期は未実施**。現在のAACはBGMのみ。
- LINE公式アプリの実画面録画・操作・審査申請は未実施。映像のスマホ画面は**独自の説明用イメージ**。
- YouTubeへのアップロード・公開・収益化審査は未実施。
- ZIP/MP4等のバイナリは2026-11-01にDropboxへ保存し、11個の制作ファイルと管理インデックス（計12ファイル）の**ファイル名・サイズ・格納パス**をDropbox一覧で確認。クラウドから再ダウンロードしたバイト単位のSHA再照合・Windows端末同期の検証は未実施。詳細はARTIFACTSを参照。
- スマホ単体でPython/FFmpegを実行したのではなく、ChatGPT側のPython実行環境で書き出してスマホへ渡す方式。

## Dropbox素材保管（2026-11-01確認済み）

- プロジェクト専用の保存先：`/ChatGPT-Transfer/YouTube-Production/projects/line-sticker-howto-20261101/`
- `YOUTUBE_STORAGE_INDEX.md` に各フォルダの用途、相対ファイル名、保存元SHA-256、旧ZIPの注意事項を記録。
- `01_script`: 台本・概要欄／`02_assets`: PNG10枚のUTF-8 ZIP＋確認用PNG／`03_source`: プロジェクトソースZIP。
- `04_exports`: MP4・サムネイル／`05_qa`: テスト報告・11シーン画像／`90_archive`: 文字化けした旧ZIP2件。
- `00_inbox` と共通素材用 `../../_shared` は新規素材の受け取り・次案件共用のため空のまま確保。
- 既存の `/ChatGPT-Transfer/LINEスタンプ制作/` は変更なし。今回の保存は新規フォルダへのコピーのみで、元ファイルを削除・移動していない。
- Dropboxのクラウド保存とローカルPC同期を混同しない。上記はDropboxクラウドの書込み・ファイル一覧で確認した範囲。

## 引継ぎ先

- [制作ツール・再現手順・注意事項](TECHNICAL_RUNBOOK.md)
- [成果物とSHA-256・検査証跡](ARTIFACTS_AND_QA.md)
- [判断と次回改善事項](DECISIONS.md)
- プロジェクト登録の正本：リポジトリルート `projects.json`

## 次に行うこと

1. Dropboxに保存済みのMP4とUTF-8修正版ZIPを再ダウンロードしてSHA-256を照合し、必要ならWindows側Dropbox同期も検証。コード本体のGitHub管理は任意。
2. 動画の目視最終確認。文字の視認性・テンポ・説明の正確性を確認。
3. 必要なら実機画面のスクリーン録画、TTS/収録音声を加えて再レンダリング。
4. LINE公式の現行ガイドと整合を確認してからYouTubeへ公開（この登録作業では公開しない）。

## 2026-11-01: VOICEVOXナレーション連携（未完了）

- VOICEVOXローカルエンジンへのAPI接続を前提とした11シーンの音声生成・自動同期・BGMミックスのソースを作成し、Dropbox `03_source/line_sticker_voicevox_pipeline_v1.zip` に保存。
- 同じフォルダ群の `01_script/VOICEVOX_README_JA.md` と `05_qa/VOICEVOX_TEST_REPORT.md` に実行方法・テスト結果を記録。
- 公式エンジン不在のため **VOICEVOX実音声生成と音声付きMP4は未完了**。11シーンのHTTPモック／無音WAVによるFFmpeg結合テストは通過。成果物は旧動画v1のまま維持。
- 実装・制限・再開手順は [VOICEVOXナレーション実装記録](VOICEVOX_NARRATION.md) を正本とする。
