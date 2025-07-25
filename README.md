# 🖼️ Image Resizer Tool using Python

A powerful and optimized command-line tool to **batch resize** and **convert images** within a given folder. Built with 💖 using Python, Pillow, and tqdm.

---

## 🚀 Features

- ✅ Proportional image resizing (preserves aspect ratio)
- 🎨 Format conversion support (JPEG, PNG, WebP)
- 🔍 Dry-run mode to preview actions without writing files
- 🧠 Automatic format detection if not specified
- 🌈 Transparency preservation for PNGs
- ⏩ Skips already processed files
- 📊 Progress bar for visual feedback
- 🕒 Job completion timer

---

## 🛠️ Built With

- [Python](https://www.python.org/) 🐍
- [Pillow](https://pillow.readthedocs.io/en/stable/) – For image manipulation
- [tqdm](https://tqdm.github.io/) – For the progress bar

---

## 📦 Installation

1. **Clone the Repository**

   ```bash
   - git clone https://github.com/nova-550/Image-Resizer-Tool-using-Python.git
   - cd Image-Resizer-Tool-using-Python
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   - python -m venv venv
   - venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install pillow tqdm
   ```

## ⚙️ Usage
    python tool.py <input_folder> <output_folder> [options]

## 🧾 Command-Line Options

<table>
<thead>
<tr>
<th>Argument
<th>Description
<th>Default
</tr>
<tbody>
<tr>
<td>input_folder
<td>Folder containing original images
<td>required
</tr>
<tr>
<td>output_folder
<td>Folder to save resized images
<td>required
</tr>
<tr>
<td>--width
<td>Maximum width of resized images
<td>800
</tr>
<tr>
<td>--height
<td>Maximum height of resized images
<td>800
</tr>
<tr>
<td>--format
<td>Output image format (JPEG, PNG, WEBP)
<td>original
</tr>
<tr>
<td>--dry-run
<td>Preview actions without writing files
<td>False
</tr>
</tbody>
</thead>
</table>

## 🔧 Examples
### 🔹 Resize All Images to 1024x768
    python tool.py ./input ./output --width 1024 --height 768

### 🔹 Convert All Images to PNG
    python tool.py ./input ./output --format PNG

### 🔹 Resize + Convert to JPEG
    python tool.py ./input ./output --width 500 --height 500 --format JPEG

### 🔹 Dry Run (No Changes Made)
    python tool.py ./input ./output --dry-run

## 📁 Folder Structure
    Image-Resizer-Tool-using-Python/
    │
    ├── tool.py # Main script
    ├── README.md # You're reading this 😄
    ├── input/ # (You create) Source images go here
    └── output/ # (Script creates) Resized images appear here

## 🧠 Best Practices
- Use high-resolution source images.
- Always test with --dry-run for safety.
- Keep input/ and output/ separate to avoid confusion or overwriting.
