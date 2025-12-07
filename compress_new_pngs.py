import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from zopfli.png import compress

# Directories to watch for new PNG images
directories_to_watch = [
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

class PNGHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.lower().endswith(".png"):
            print(f"Compressing new PNG: {event.src_path}")
            self.compress_png(event.src_path)

    def compress_png(self, file_path):
        try:
            with open(file_path, "rb") as f:
                data = f.read()
            compressed_data = compress(data)
            # Overwrite the original file with compressed data
            with open(file_path, "wb") as f:
                f.write(compressed_data)
            print(f"Compressed: {file_path}")
        except Exception as e:
            print(f"Error compressing {file_path}: {e}")

def main():
    event_handler = PNGHandler()
    observer = Observer()
    for directory in directories_to_watch:
        abs_dir = os.path.abspath(directory)
        if os.path.exists(abs_dir):
            observer.schedule(event_handler, abs_dir, recursive=False)
    observer.start()
    print("Watching for new PNG images...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
