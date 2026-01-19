# PDF 转 PPTX AI 转换器 📄➡️📊

[English](README.md) | [日本語](README.ja.md)

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/platform-windows-lightgrey)

**利用 AI 将 PDF 幻灯片转换为*可编辑*的 PowerPoint 演示文稿。**

传统的转换器通常只能导出静态图片。本工具利用 **OCR** (光学字符识别) 提取文本，并使用 **AI 修复 (LaMa)** 技术擦除背景上的原始文本，从而生成干净、可编辑的幻灯片。

> [!WARNING]
> **显存/内存占用警告**: 本工具使用的 AI 模型可能会消耗大量显存 (VRAM) 和系统内存。如果您遇到程序崩溃或提示“内存不足 (Out of Memory)”，请尝试降低图片分辨率，或在拥有更大内存的计算机上运行。

---

## ✨ 功能特点

- **AI 背景修复**: 使用 LaMa (Large Mask Inpainting) 模型擦除幻灯片上的原始文本，还原干净背景。
- **文本重构**: 使用 RapidOCR 定位文本位置，并在修复后的背景上放置可编辑的文本框。
- **自适应清理**: 智能膨胀算法，确保不会残留“重影文本”。
- **现代 GUI**: 用户友好的界面，支持拖放操作。
- **批处理列队**: 支持一次性批量转换多个文件。
- **隐私优先**: 100% 本地运行，不会将数据发送到云端。

## 🛠️ 前置要求

- **操作系统**: Windows 10/11 (推荐)
- **Python**: 3.8 或更高版本
- **GPU (可选)**: 强烈推荐使用 NVIDIA GPU (CUDA) 以获得更快的 AI 处理速度 (也支持 CPU 模式，但速度较慢)。

## 🚀 安装指南

1.  **克隆仓库**:
    ```bash
    git clone https://github.com/ysrock/pdf2pptx-ai-tool.git
    cd pdf2pptx-ai-tool
    ```

2.  **创建虚拟环境** (推荐):
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **安装依赖**:
    ```bash
    pip install -r requirements.txt
    ```

    > **💡 GPU 用户**: 要启用快速 GPU 加速，请安装 PyTorch 的 CUDA 版本:
    > ```bash
    > pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
    > ```

## 📖 使用方法

### GUI 模式 (推荐)
直接运行脚本启动界面:
```bash
python pdf2pptx_converter.py
```
- **拖放** PDF 文件到窗口中。
- 调整 **质量 (DPI)** (默认: 100, 推荐值，兼顾质量与速度)。
- 调整 **伪影清理 (Artifact Cleanup)** (数值越高擦除力度越大)。
- 点击 **开始批量转换 (Start Batch Conversion)**。

### 命令行模式 (CLI)
用于自动化或无头模式:
```bash
python pdf2pptx_converter.py "input.pdf" "output.pptx" [DPI] [Dilation]
```
示例:
```bash
python pdf2pptx_converter.py "lecture.pdf" "lecture_editable.pptx" 100 15
```

## ⚙️ 工作原理

1.  **渲染**: 将 PDF 页面转换为高分辨率图像。
2.  **检测**: OCR 识别文本区域。
3.  **遮罩**: 创建文本区域的遮罩 (Mask)。
4.  **修复**: LaMa AI 模型利用遮罩“脑补”文本背后的背景。
5.  **重构**: 将干净的背景图像放置在 PPTX 幻灯片上 -> 在精确坐标处覆盖可编辑的文本框。

## 🤝 贡献代码

欢迎提交 Pull Request 来改进本项目！

## 📄 许可证

本项目采用 MIT 许可证 - 详情请参阅 [LICENSE](LICENSE) 文件。
