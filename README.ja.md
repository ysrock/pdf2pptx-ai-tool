# PDF to PPTX AI Converter 📄➡️📊

[English](README.md) | [中文版](README.zh-CN.md)

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/platform-windows-lightgrey)

**AIを使用して、PDFスライドを*編集可能*なPowerPointプレゼンテーションに変換します。**

従来のコンバーターは静的な画像のみをエクスポートするものがほとんどですが、このツールは **OCR** (光学文字認識) を使用してテキストを抽出し、**AI インペインティング (LaMa)** を使用して背景から元のテキストを消去することで、きれいで編集可能なスライドを作成します。

> [!WARNING]
> **メモリ使用量に関する警告**: このツールは、GPUメモリ (VRAM) とシステムメモリを大量に消費するAIモデルを使用します。クラッシュや「メモリ不足 (Out of Memory)」エラーが発生した場合は、画像の解像度を下げるか、メモリの多いマシンで実行してみてください。

---

## ✨ 特徴

- **AIによる背景復元**: LaMa (Large Mask Inpainting) を使用してスライドから元のテキストを消去し、きれいな背景を作成します。
- **テキスト再構築**: RapidOCRを使用してテキストの位置を検出し、クリーニングされた背景の上に編集可能なテキストボックスを配置します。
- **適応型クリーニング**: 高度なダイレーションアルゴリズムにより、「ゴーストテキスト」が残らないようにします。
- **モダンなGUI**: ドラッグ＆ドロップに対応した使いやすいインターフェイス。
- **プロセスキュー**: 複数のファイルを一括変換できます。
- **プライバシー重視**: 100% ローカルで実行されます。データがクラウドに送信されることはありません。

## 🛠️ 前提条件

- **OS**: Windows 10/11 (推奨)
- **Python**: 3.8 以上
- **GPU (オプション)**: 高速なAI処理のために、NVIDIA GPU (CUDA) の使用を強く推奨します (CPUモードもサポートされていますが、速度は遅くなります)。

## 🚀 インストール

1.  **リポジトリをクローン**:
    ```bash
    git clone https://github.com/your-username/pdf2pptx.git
    cd pdf2pptx
    ```

2.  **仮想環境の作成** (推奨):
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **依存関係のインストール**:
    ```bash
    pip install -r requirements.txt
    ```

    > **💡 GPU ユーザー**: 高速なGPUアクセラレーションを有効にするには、CUDAバージョンのPyTorchをインストールしてください:
    > ```bash
    > pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
    > ```

## 📖 使用方法

### GUI モード (推奨)
スクリプトを実行してインターフェイスを起動します:
```bash
python pdf2pptx_converter.py
```
- ウインドウにPDFファイルを **ドラッグ＆ドロップ** します。
- **品質 (DPI)** を調整します (高いほど背景はきれいになりますが、処理が遅くなります)。
- **アーティファクト除去 (Artifact Cleanup)** を調整します (高いほどテキスト消去が強力になります)。
- **一括変換開始 (Start Batch Conversion)** をクリックします。

### コマンドライン (CLI)
自動化やヘッドレス使用の場合:
```bash
python pdf2pptx_converter.py "input.pdf" "output.pptx" [DPI] [Dilation]
```
例:
```bash
python pdf2pptx_converter.py "lecture.pdf" "lecture_editable.pptx" 250 15
```

## ⚙️ 仕組み

1.  **レンダリング**: PDFページを高解像度画像に変換します。
2.  **検出**: OCRがテキスト領域を特定します。
3.  **マスク**: テキスト領域のマスクを作成します。
4.  **インペインティング**: LaMa AIモデルがマスクを使用して、テキストの背後にある背景を「推測」して描画します。
5.  **再構築**: きれいな背景画像をPPTXスライドに配置 -> 正確な座標に編集可能なテキストボックスを重ねます。

## 🤝 貢献

プルリクエストによる貢献を歓迎します！

## 📄 ライセンス

このプロジェクトは MIT ライセンスの下でライセンスされています。詳細は [LICENSE](LICENSE) ファイルを参照してください。
