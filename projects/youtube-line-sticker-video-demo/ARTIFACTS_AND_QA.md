# 成果物一覧・検証証跡（2026-11-01）

Status: prototype technically verified; no publish claim.

## ハッシュ付き成果物

| ファイル | サイズ（bytes） | SHA-256 | 状態 |
| --- | ---: | --- | --- |
| `line_sticker_youtube_test.mp4` | 5,999,216 | `1c82f6e1e1ef3dc65d81e2b0cb5381721ee87846327339ef1ef41a8bc5d059c2` | 検証済み |
| `line_sticker_youtube_thumbnail.png` | 122,858 | `741c1c8bfe406599e6f1446b29438bfe91d2336537329a82192adecc5934f16c` | 画像生成済み |
| `line_sticker_video_contact_sheet.png` | 197,801 | `972f900351050f86a755a0a871944fc007cabcf15b67368325900b9bf251d59c` | 11シーン確認用 |
| `line_sticker_sticker_samples.zip` | 362,562 | `4410f0331d016ee3e69bf68e9abf08c2223579f9c4476a87080944edb43233e2` | **旧ZIP、日本語名文字化け** |
| `line_sticker_video_project.zip` | 379,225 | `94e1dbb9d25de80a24b042bd59a8ca84e36141d8f370764a9ba014670cea9d18` | **旧ZIP、日本語名文字化け** |
| `line_sticker_video_project_utf8.zip` | 378,077 | `1abfaed977178a360539c659f36d96d2a892fdf10c374823ced8aea97f8b964b` | **推奨ソースアーカイブ、UTF-8名修正版** |

これらのハッシュは同一のChatGPT会話のコンテナ内で計測。**GitHubに動画やZIPのバイト列は保存されていない**。2026-11-01にDropbox新規プロジェクトフォルダへコピーし、Dropbox一覧からパスとサイズを検証した。保存元のSHA-256がDropboxへ送信したバイトと一致することの独立した再ダウンロード照合は未実施。

## Dropbox保存・確認（2026-11-01）

基点：`/ChatGPT-Transfer/YouTube-Production/projects/line-sticker-howto-20261101/`

- `YOUTUBE_STORAGE_INDEX.md`: フォルダ目的と11ファイルのSHA-256台帳（3,396 bytes）。
- `01_script/`: `script_and_storyboard.md`, `youtube_description.md`
- `02_assets/`: `line_sticker_assets_utf8.zip`（PNG10枚、361,323 bytes、SHA-256 `da7ecd0c0d0acd7bc0bf20bb5cf6d79d459c95024470240c402abd981480ad80`）と `02_ありがとう.png`
- `03_source/`: `line_sticker_video_project_utf8.zip`
- `04_exports/`: `line_sticker_youtube_test.mp4`, `line_sticker_youtube_thumbnail.png`
- `05_qa/`: `test_report.md`, `line_sticker_video_contact_sheet.png`
- `90_archive/`: `line_sticker_video_project_legacy.zip` と `line_sticker_sticker_samples_legacy.zip`（**ファイル名文字化けの旧版**）
- `00_inbox/`: 空。共通の `/ChatGPT-Transfer/YouTube-Production/_shared/` も空。
- Dropboxでの検証：プロジェクト配下7フォルダ＋管理インデックス1件＋成果物11件（計19エントリ）。ファイルサイズと名前を保存元と照合し一致。
- Dropbox APIから全ファイルを再取得したSHA比較、PC同期、YouTube公開については未検証。

## 動画の技術検査

- `ffprobe`：長さ81.000000秒、サイズ5,999,216 bytes、H.264映像1280×720、24fps、AAC音声。
- 期待総フレーム数：81×24=1,944。
- `ffmpeg -v error -i ... -f null -`：全編エラー出力なし。
- `render_video.py`、`generate_stickers.py`：Pythonコンパイル（構文チェック）成功。
- `manifest.json`：JSONロード成功、シーン11、合計81秒。
- PNG：8通常スタンプ各370×320 RGBA、メイン240×240 RGBA、タブ96×74 RGBA、10枚すべて1MB未満。
- 元ZIP：CRC検査は成功したが7件の日本語ファイル名が文字化け。UTF-8修正版は17ファイル、UTF-8名7件、CRC異常なし。
- 表現上の確認：サムネイル/シーン一覧の画像を確認。**視覚的な完全承認や音声ナレーション検証はしていない**。

## 未実施テスト

- LINEスタンプメーカー実機操作 / 実際のスタンプ申請。
- 生成された動画のYouTubeアップロード / 動画公開 / 収益化審査。
- 声の読み上げ、音声とシーンの同期品質。
- 異なるOS/フォント環境での再構築。
- 継続的な自動処理、再実行の完全冪等性、CIによる回帰テスト。
- 1080p/縦型動画/画面録画の差し込み動作。

## 再試験の判定基準

1. 使うソースZIPのハッシュと日本語パスを照合。
2. 生成後に `ffprobe`、全編デコード、音声存在、先頭/中間/末尾の画像検査。
3. 内容変更時はフレームの文字重なり・切れ・誤字の目視、台本との整合を確認。
4. 外部仕様・権利確認、LINEとYouTubeの公開手続きをそれぞれ独立して検証。
5. 何を実施したか、実施していないかを明確に記録。
