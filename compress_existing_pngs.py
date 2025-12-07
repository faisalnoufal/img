import os
from zopfli.png import compress

directories_to_scan = [
    "blkfri_25/cmg/cmg/",
    "blkfri_25/lm/lm/",
    "blkfri_25/pm/pm/",
    "blkfri_25/vcc/vcc/",
    "blkfri_25/vm/vm/",
    "dec25/cmg/",
    "dec25/lm/",
    "dec25/pm/",
    "dec25/vcc/",
    "dec25/vm/",
    "Logos/",
    "nov25/cmg/",
    "nov25/dgl/",
    "nov25/dw/",
    "nov25/finance/",
    "nov25/lc/",
    "nov25/pm/",
    "nov25/tradein/",
    "nov25/vcc/",
    "nov25/vm/"
]

def compress_png(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        compressed_data = compress(data)
        with open(file_path, "wb") as f:
            f.write(compressed_data)
        print(f"Compressed: {file_path}")
    except Exception as e:
        print(f"Error compressing {file_path}: {e}")

def main():
    for directory in directories_to_scan:
        abs_dir = os.path.abspath(directory)
        if os.path.exists(abs_dir):
            for filename in os.listdir(abs_dir):
                if filename.lower().endswith(".png"):
                    file_path = os.path.join(abs_dir, filename)
                    compress_png(file_path)

if __name__ == "__main__":
    main()
