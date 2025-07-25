import os
import argparse
import time
from PIL import Image
from tqdm import tqdm

SUPPORTED_FORMATS = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp')

def is_image_file(filename):
    return filename.lower().endswith(SUPPORTED_FORMATS)

def get_output_path(output_dir, filename, output_format):
    base_name = os.path.splitext(filename)[0]
    extension = output_format.lower()
    return os.path.join(output_dir, f"{base_name}.{extension}")

def resize_images(input_dir, output_dir, max_width, max_height, output_format=None, dry_run=False):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    files = [f for f in os.listdir(input_dir) if is_image_file(f)]

    if not files:
        print("⚠️ No supported image files found in the input directory.")
        return

    start_time = time.time()
    print(f"\n🚀 Starting image processing... ({len(files)} files)\n")

    for filename in tqdm(files, desc="Processing", unit="image"):
        input_path = os.path.join(input_dir, filename)

        try:
            with Image.open(input_path) as img:
                original_format = img.format
                original_mode = img.mode

                # Determine final output format
                final_format = (output_format or original_format or 'JPEG').upper()

                output_path = get_output_path(output_dir, filename, final_format)

                if os.path.exists(output_path):
                    print(f"⏩ Skipping (already exists): {output_path}")
                    continue

                if dry_run:
                    print(f"[DRY RUN] Would process: {input_path} ➜ {output_path}")
                    continue

                # Resize proportionally
                img.thumbnail((max_width, max_height))

                # Handle transparency
                if final_format == 'PNG' and 'A' in original_mode:
                    img.save(output_path, final_format)
                else:
                    img.convert("RGB").save(output_path, final_format)

        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")

    end_time = time.time()
    print(f"\n✅ Completed in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="📷 Batch Resize & Convert Images (Optimized)")

    parser.add_argument("input_dir", help="Path to input folder")
    parser.add_argument("output_dir", help="Path to output folder")

    parser.add_argument("--width", type=int, default=800, help="Maximum width (default: 800)")
    parser.add_argument("--height", type=int, default=800, help="Maximum height (default: 800)")
    parser.add_argument("--format", type=str, choices=['JPEG', 'PNG', 'WEBP'], help="Convert to format (e.g. JPEG, PNG)")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing files")

    args = parser.parse_args()

    resize_images(
        input_dir=args.input_dir,
        output_dir=args.output_dir,
        max_width=args.width,
        max_height=args.height,
        output_format=args.format,
        dry_run=args.dry_run
    )
