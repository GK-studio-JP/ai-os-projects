# 技術資料：ChatGPT + Python + FFmpeg による低コストYouTube動画制作

Verified: 2026-11-01 (ChatGPT側のLinux実行環境での1本の実例)
Scope: project / prototype
Applies to: `youtube-line-sticker-video-demo`

## 0. 制作方針とアーキテクチャ

動画生成AIへの秒数課金は使わず、**台本→シーンデータ→静止素材・図解の描画→カメラ移動・切替→BGM・音声合成→MP4**で制作する。スライドショーに限定する設計ではないが、**現行実装は静止画ベースのモーショングラフィックス**であり、実写複数レイヤー編集、複雑なキャラクターアニメーション、動画生成AIの代用は実装していない。

データフロー：

```text
ChatGPT（台本・絵コンテ）
  -> manifest.json（project, canvas, scenes[].duration/kind/title/detail/narration）
  -> generate_stickers.py -> assets/stickers/*.png
  -> render_video.py + Pillow（1280x720の各シーン静止画）
  -> FFmpeg zoompan / fade / libx264（シーン別MP4）
  -> FFmpeg concat（映像タイムライン）
  + NumPyによるオリジナルシンセBGM（WAV）
  + 任意の assets/voiceover.wav（今回は不在）
  -> FFmpeg libx264 bitstream copy + AAC, +faststart
  -> line_sticker_youtube_test.mp4 と line_sticker_youtube_thumbnail.png
```

**素材と台本を別管理する。** `manifest.json` はシーン内容・時間の単一の情報源。ただし現状の色設定は `render_video.py` にも定数として重複しており、`manifest.json.style` は実際の描画に使われていない。次版ではスタイルの単一情報源化が必要。

## 1. 使用ツール・費用・確認済みバージョン

| 役割 | ツール | 今回の使用実績 |
| --- | --- | --- |
| 台本・構成 | ChatGPT | 11シーンのナレーション原稿・タイトル・説明文 |
| 描画 | Python 3.13.5 / Pillow 12.3.0 | 猫イラスト、透過PNG、シーン画像、文字・図解 |
| 音楽生成 | NumPy 2.3.5 / wave | 簡易的な独自のインストゥルメンタルBGMを合成 |
| 動画・音声合成 | FFmpeg 7.1.5 / ffprobe | H.264/AAC、zoompan、fade、concat、検査 |
| 文字 | Noto Sans CJK JP | 日本語フォントをローカル環境から参照、フォントファイルは配布しない |
| 公開 | YouTube | 今回は未実行 |
| スマホ内編集 | なし | ChatGPT実行環境からスマホで保存する方式 |

すべての動画処理はローカルOSSで実行し、CapCut等の有料プランなし。ChatGPTの利用枠や実行環境は別条件。**クラウド上の計算が完全に無料・無制限という意味ではない**。

## 2. 元プロジェクトの構成

```text
line_sticker_video_source/
  README.md
  manifest.json
  generate_stickers.py
  render_video.py
  script_and_storyboard.md
  youtube_description.md
  test_report.md
  assets/
    stickers/
      01_おはよう.png ... 08_おやすみ.png
      main.png
      tab.png
    voiceover.wav        # 任意。初回テストには含まれない
  build/                 # 実行時に生成・削除される一時出力
../line_sticker_youtube_test.mp4
../line_sticker_youtube_thumbnail.png
```

コード・PNG等は元ZIPに格納。**このGitHub文書群自体に元ソースやバイナリをアップロードしたわけではない**ので、原版を失わないこと。保存物のハッシュはARTIFACTS_AND_QA.md参照。

## 3. 再現手順（Linux系、ソースZIPがある場合）

1. 日本語名を正しく扱える `line_sticker_video_project_utf8.zip` を展開する。旧ZIPはファイル名が文字化けしていたため使用しない。
2. Python 3、Pillow、NumPy、FFmpeg、`libx264`、Noto Sans CJK JPフォントを用意。ネット接続や有料動画APIは必須ではない。
3. `generate_stickers.py` と `render_video.py` ではフォントパスを `/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc` 等に固定している。実環境に合わせて存在確認・変更が必要。
4. `manifest.json` の `canvas`（1280×720、24fps）、`scenes`（11件）、各 `duration` と `kind` を確認。内容を変更するときは `scenes[].title/detail/narration` を編集。
5. `python generate_stickers.py` で透過PNG10枚を生成。
6. `python render_video.py` で各シーン画像とFFmpeg動画を生成し、シーン結合・音声合成を実行。最後に親フォルダへMP4/サムネイルが出る。
7. `ffprobe` でcodec/duration/size/fpsを確認、`ffmpeg -v error -i line_sticker_youtube_test.mp4 -f null -` で全編デコード、サムネイルや複数の時点を目視確認する。
8. ファイルをスマホに渡し、公開前にYouTube Studioでタイトル、説明、リンク、権利、AI加工表示要件を確認。

実行例（`line_sticker_video_source` フォルダ内）：

```bash
python -m pip install Pillow numpy
python generate_stickers.py
python render_video.py
ffprobe -v error -show_entries format=duration,size:stream=index,codec_name,width,height,r_frame_rate -of json ../line_sticker_youtube_test.mp4
ffmpeg -v error -i ../line_sticker_youtube_test.mp4 -f null -
```

## 4. 動画構成（今回の11シーン）

| No. | 時間 | 内容 |
| --- | ---: | --- |
| 1 | 0:00.0–0:06.5 | LINEスタンプはスマホでも作れる |
| 2 | 0:06.5–0:13.5 | LINEスタンプメーカーの準備 |
| 3 | 0:13.5–0:20.5 | 言葉を考える |
| 4 | 0:20.5–0:29.5 | 猫スタンプ8個を作る |
| 5 | 0:29.5–0:38.0 | 写真・イラストを選び編集 |
| 6 | 0:38.0–0:45.0 | 文字と余白の視認性 |
| 7 | 0:45.0–0:54.0 | PNG規格と枚数 |
| 8 | 0:54.0–1:01.0 | 名前・説明文 |
| 9 | 1:01.0–1:08.0 | LINEの審査申請 |
| 10 | 1:08.0–1:15.0 | 権利と視認性のチェック |
| 11 | 1:15.0–1:21.0 | まとめ |

## 5. 実装上の重要事項・注意

- **公式画面ではない**：スマホUIは描画した説明用イメージ。実際のLINEアプリ画面と誤認させない表示を維持し、公開版では必要に応じて実画面収録へ差し替える。
- **LINE規格は更新され得る**：動画の記載は通常の静止画スタンプを対象にしている。ポップアップスタンプ/APNGと混同しない。公開直前に公式仕様と申請条件を再確認。
- **画像と音楽の権利**：今回の猫・図解・BGMはプログラムによる独自生成。第三者素材、商標、LINE公式UIの転載に切り替える場合は権利確認が必要。
- **音声**：`manifest.json` の `narration` は台本テキストで、現在のプログラムは直接TTSを実行しない。実音声が必要なら `assets/voiceover.wav` を別途用意。原稿時間・発話同期を検査。
- **書き出し**：1080p、縦型9:16、Shorts用のリフレーミングは現状テストしていない。横型720pの結果のみ実証。
- **動き**：FFmpegのzoompanは軽い中心ズーム。実写/画面録画・B-rollの切り替えは今回のソースが対応済みと断定しない。
- **移植性**：スクリプトはLinuxフォント絶対パスを前提とする。スマホ本体での実行可否は未確認。メモリ、CPU、コーデック、フォント差分で再現性が変わる。
- **中間ファイル**：`build/clip_*.mp4` と `build/scene_*.png` はレンダリング開始時に消去する。重要な原画はbuild外へ保管。
- **ZIP文字化け**：旧ZIP内の日本語ファイル名が破損している。修正版はPython zipfileで書き直し、UTF-8フラグ7件・CRC検査合格を確認した。
- **制作結果と公開は別**：映像のデコード成功、YouTubeアップロード成功、収益化承認を同一視しない。

## 6. 公式参照先

- LINEスタンプメーカー：https://creator.line.me/ja/stickermaker/
- 通常スタンプ制作ガイド：https://creator.line.me/ja/guideline/sticker/
- YouTube Studio：https://studio.youtube.com/

本書の実証は2026-11-01時点。上記サービスの現在の仕様・利用条件は公開時に再確認すること。
