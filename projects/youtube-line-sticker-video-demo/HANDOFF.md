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
- ZIP/MP4等のバイナリ成果物は当時のChatGPT会話成果物として存在するが、**GitHub/Dropbox等の永続保存をこの登録で実施したわけではない**。以下のARTIFACTSを照合して保存先を確定する必要あり。
- スマホ単体でPython/FFmpegを実行したのではなく、ChatGPT側のPython実行環境で書き出してスマホへ渡す方式。

## 引継ぎ先

- [制作ツール・再現手順・注意事項](TECHNICAL_RUNBOOK.md)
- [成果物とSHA-256・検査証跡](ARTIFACTS_AND_QA.md)
- [判断と次回改善事項](DECISIONS.md)
- プロジェクト登録の正本：リポジトリルート `projects.json`

## 次に行うこと

1. 完成MP4とUTF-8修正版プロジェクトZIPを永続保存先へ配置し、SHA-256を再照合。必要ならコード本体も専用リポジトリに格納。
2. 動画の目視最終確認。文字の視認性・テンポ・説明の正確性を確認。
3. 必要なら実機画面のスクリーン録画、TTS/収録音声を加えて再レンダリング。
4. LINE公式の現行ガイドと整合を確認してからYouTubeへ公開（この登録作業では公開しない）。
