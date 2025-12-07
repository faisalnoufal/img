import os
from zopfli.png import optimize as zopfli_compress_png
from PIL import Image
import sys

image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.tiff', '.tif', '.bmp', '.webp')

def compress_image(file_path):
    ext = file_path.lower()
    try:
        original_size = os.path.getsize(file_path)
        if ext.endswith('.png'):
            # Use zopfli for PNG lossless compression
            with open(file_path, "rb") as f:
                data = f.read()
            compressed_data = zopfli_compress_png(data)
            with open(file_path, "wb") as f:
                f.write(compressed_data)
        else:
            # Use PIL for other formats with optimize
            img = Image.open(file_path)
            # Check if we can optimize this format
            if img.format in ['JPEG', 'PNG', 'GIF', 'TIFF', 'BMP', 'WEBP']:
                # For formats that support optimize
                kwargs = {'optimize': True}
                if img.format == 'JPEG':
                    # For JPEG, also use progressive=False for better compatibility, but keep quality 100
                    kwargs.update({'progressive': False, 'quality': 100})
                elif img.format == 'PNG':
                    kwargs.update({'compress_level': 9})
                elif img.format == 'WEBP':
                    # WEBP supports lossless
                    kwargs.update({'lossless': True})
                img.save(file_path, **kwargs)
            else:
                print(f"Skipping unsupported format: {file_path}")
                return

        new_size = os.path.getsize(file_path)
        reduction = original_size - new_size
        reduction_percent = (reduction / original_size) * 100 if original_size > 0 else 0
        print(f"Compressed: {file_path} - Reduced by {reduction} bytes ({reduction_percent:.1f}%)")

    except Exception as e:
        print(f"Error compressing {file_path}: {e}")

def main():
    current_dir = '.'
    for root, dirs, files in os.walk(current_dir):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', '__pycache__']]  # Skip hidden dirs and node_modules
        for file in files:
            if file.lower().endswith(image_extensions):
                file_path = os.path.join(root, file)
                compress_image(file_path)

if __name__ == "__main__":
    main()
