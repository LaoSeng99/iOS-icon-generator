import json
import os
from PIL import Image

# === 配置 ===
INPUT_IMAGE = 'input/icon.png'
CONTENT_JSON = 'Contents.json'
OUTPUT_DIR = 'output'

# === 读取 JSON ===
with open(CONTENT_JSON, 'r') as f:
    content = json.load(f)

# === 创建输出目录 ===
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# === 打开原始 icon ===
base_icon = Image.open(INPUT_IMAGE)

# === 遍历生成各尺寸图标 ===
for image in content['images']:
    filename = image.get('filename')
    if not filename:
        continue  # skip missing

    size_pt = image['size']  # e.g. "29x29"
    scale = image['scale']   # e.g. "3x"

    width_pt, height_pt = map(float, size_pt.split('x'))
    scale_factor = int(scale.replace('x', ''))

    pixel_width = int(width_pt * scale_factor)
    pixel_height = int(height_pt * scale_factor)

    resized_icon = base_icon.resize((pixel_width, pixel_height), Image.LANCZOS)
    output_path = os.path.join(OUTPUT_DIR, filename)
    resized_icon.save(output_path)

    print(f"✅ Generated: {filename} ({pixel_width}x{pixel_height})")

print("\n✅ 所有图标生成完毕！输出目录：", OUTPUT_DIR)