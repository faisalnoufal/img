#!/usr/bin/env python3
import os
import json
import sys
from pathlib import Path

def get_all_files_recursive(folder_path, base_path):
    files = []
    for root, _, filenames in os.walk(folder_path):
        for filename in filenames:
            full_path = Path(root) / filename
            relative_path = full_path.relative_to(base_path)
            files.append(str(relative_path))
    return files

def main(campaign_dir):
    base = Path(__file__).parent
    campaign_path = base / campaign_dir
    result = {'headers': {}, 'body': {}}

    if not campaign_path.is_dir():
        print(f"Error: Directory '{campaign_dir}' not found.")
        sys.exit(1)

    for dealer_entry in os.scandir(campaign_path):
        if dealer_entry.is_dir():
            dealer = dealer_entry.name
            dealer_path = Path(dealer_entry.path)

            all_files = get_all_files_recursive(dealer_path, base)

            headers = sorted([f for f in all_files if f.lower().endswith('.gif')])
            body = sorted([f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg'))])

            if headers or body:
                result['headers'][dealer] = headers
                result['body'][dealer] = body

    with open(base / 'folders.json', 'w') as f:
        json.dump(result, f, indent=2)
    print(f'folders.json updated for campaign: {campaign_dir}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 update_folders_json.py <campaign_directory>")
        sys.exit(1)
    main(sys.argv[1])
