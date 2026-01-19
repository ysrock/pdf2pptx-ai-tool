# PDF to PPTX AI Converter 📄➡️📊

[中文版](README.zh-CN.md) | [日本語](README.ja.md)

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/platform-windows-lightgrey)

**Convert PDF slides into *Editable* PowerPoint presentations using AI.**

Traditional converters only export static images. This tool uses **OCR** (Optical Character Recognition) to extract text and **AI Inpainting (LaMa)** to erase the original text from the background, creating a clean, editable slide.

> [!WARNING]
> **High Memory Usage**: This tool uses AI models that may consume significant VRAM (GPU memory) and System RAM. If you experience crashes or "Out of Memory" errors, please try reducing the image resolution or running on a machine with more memory.

---

## ✨ Features

- **AI-Powered Background Restoration**: Uses LaMa (Large Mask Inpainting) to erase original text from slides, creating a clean canvas.
- **Text Reconstruction**: Uses RapidOCR to detect text positions and places editable text boxes over the cleaned background.
- **Adaptive Cleaning**: Intelligent dilation algorithms to ensure no "ghost text" remains.
- **Modern GUI**: User-friendly interface with Drag & Drop support.
- **Process Queue**: Batch convert multiple files at once.
- **Privacy First**: Runs 100% locally. No data is sent to the cloud.

## 🛠️ Prerequisites

- **OS**: Windows 10/11 (Recommended)
- **Python**: 3.8 or higher
- **GPU (Optional)**: NVIDIA GPU (CUDA) is highly recommended for faster AI processing. (CPU mode is supported but slower).

## 🚀 Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/ysrock/pdf2pptx-ai-tool.git
    cd pdf2pptx-ai-tool
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

    > **💡 GPU Users**: To enable fast GPU acceleration, install the CUDA version of PyTorch:
    > ```bash
    > pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
    > ```

## 📖 Usage

### GUI Mode (Recommended)
Simply run the script to launch the interface:
```bash
python pdf2pptx_converter.py
```
- **Drag & Drop** PDF files into the window.
- Adjust **Quality (DPI)** (Higher = better background, slower).
- Adjust **Artifact Cleanup** (Higher = more aggressive text erasure).
- Click **Start Batch Conversion**.

### Command Line (CLI)
For automation or headless use:
```bash
python pdf2pptx_converter.py "input.pdf" "output.pptx" [DPI] [Dilation]
```
Example:
```bash
python pdf2pptx_converter.py "lecture.pdf" "lecture_editable.pptx" 250 15
```

## ⚙️ How It Works

1.  **Render**: Converts PDF page to high-res image.
2.  **Detect**: OCR identifies text regions.
3.  **Mask**: Creates a mask of the text areas.
4.  **Inpaint**: LaMa AI model "hallucinates" the background behind the text using the mask.
5.  **Reconstruct**: Places a clean background image on the PPTX slide -> Overlays editable text boxes at exact coordinates.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
