# 🛠️ iOS App Icon Generator (Simple Script Version)

这个脚本是为了简化 iOS App 开发中 icon 制作流程，**自动根据 `Contents.json` 内的设定生成多个尺寸的图标文件**，用于 App 的 Asset Catalog。

## ✅ 功能介绍

- 📥 读取你的输入图片（默认为 `input/icon.png`）
- 📄 解析 `Contents.json` 中设定的 icon 尺寸与倍数
- 🔧 使用 Pillow 将图标 resize 到正确尺寸
- 📤 自动生成目标图标并输出到 `output/` 目录

---

⚠️ **使用提醒（Production 注意事项）**

此工具为开发阶段的临时工具，功能仅为 **简单 resize**：

- ❌ 没有智能裁切、居中、边距控制等高级功能  
- ❌ 没有图像质量优化处理，生成图标可能模糊或失真  
- ✅ 建议在正式发布前使用专业图形工具（如 Sketch、Figma、Photoshop）由设计师处理图标资源

若你有其他需求，例如格式转换、自动居中、加边距等，也可以自定义 `generate_icons.py` 中的代码逻辑。

---

## 🚀 如何运行

1. 准备输入图片：

   - 放置在：`input/icon.png`  
   - 建议为 **1024x1024 PNG** 格式

2. 准备 `Contents.json` 文件：

   - 结构类似 Xcode Asset Catalog 中的 AppIcon 内容
   - 示例文件已包含在仓库中

3. 执行脚本：

   ```bash
   python generate_icons.py



# 🛠️ iOS App Icon Generator (Simple Script Version)

This script is designed to simplify the icon production process in iOS App development. It automatically generates icon files of multiple sizes according to the settings in `Contents.json` and is used in the App's Asset Catalog.

## ✅ Function Introduction

- 📥 Read your input image (default is `input/icon.png`)
- 📄 Parse the icon size and multiples set in `Contents.json`
- 🔧 Use Pillow to resize the icon to the correct size
- 📤 Automatically generate the target icon and output it to the `output/` directory

---

⚠️ **Usage Reminder (Production Notes)**

This tool is a temporary tool in the development stage, and its function is only **simple resize**:

- ❌ No advanced features such as smart cropping, centering, margin control, etc.

- ❌ No image quality optimization processing, the generated icon may be blurry or distorted

- ✅ It is recommended to use professional graphic tools (such as Sketch, Figma, Photoshop) for designers to process icon resources before official release

If you have other needs, such as format conversion, automatic centering, adding margins, etc., you can also customize the code logic in `generate_icons.py`.

---

## 🚀 How to run

1. Prepare input image:

- Place in: `input/icon.png`

- **1024x1024 PNG** format is recommended

2. Prepare `Contents.json` file:

- Structure similar to AppIcon content in Xcode Asset Catalog

- Sample file is included in the repository

3. Execute script:

```bash
python generate_icons.py
