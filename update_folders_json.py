#!/usr/bin/env python3
import os
import json
from pathlib import Path

def get_sorted_files(folder_path, exts=None):
    files = []
    for entry in os.scandir(folder_path):
        if entry.is_file():
            if not exts or any(entry.name.lower().endswith(ext) for ext in exts):
                files.append(entry.name)
    # LIFO: newest first (by modification time)
    files.sort(key=lambda f: os.path.getmtime(os.path.join(folder_path, f)), reverse=True)
    return files

def get_body_files(folder_path):
    files = []
    # Top-level images
    files += get_sorted_files(folder_path, exts=['.png', '.jpg', '.jpeg', '.gif'])
    # Subfolders (e.g., june25, july25)
    for entry in os.scandir(folder_path):
        if entry.is_dir():
            subfolder = entry.name
            subfolder_path = os.path.join(folder_path, subfolder)
            for f in get_sorted_files(subfolder_path, exts=['.png', '.jpg', '.jpeg', '.gif']):
                files.append(f"{subfolder}/{f}")
    return files

def main():
    base = Path(__file__).parent
    headers_dir = base / 'headers'
    body_dir = base / 'body'
    result = {'headers': {}, 'body': {}}
    # Headers
    for dealer in sorted(os.listdir(headers_dir)):
        dealer_path = headers_dir / dealer
        if dealer_path.is_dir():
            result['headers'][dealer] = get_sorted_files(dealer_path, exts=['.png', '.jpg', '.jpeg', '.gif'])
    # Body
    for dealer in sorted(os.listdir(body_dir)):
        dealer_path = body_dir / dealer
        if dealer_path.is_dir():
            result['body'][dealer] = get_body_files(dealer_path)
    with open(base / 'folders.json', 'w') as f:
        json.dump(result, f, indent=2)
    print('folders.json updated.')

if __name__ == '__main__':
    main()
