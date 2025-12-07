# Image Gallery for Email Campaigns

This project is a simple and efficient static website for displaying images from email blast campaigns. It is designed to be easily updated and deployed to Cloudflare Pages.

## Features

-   **Dynamic Image Gallery:** Displays images organized by campaign and dealer.
-   **Campaign-based Structure:** Images are organized into campaign folders (e.g., `dec25`, `nov25`).
-   **Automatic Indexing:** A Python script (`update_folders_json.py`) automatically scans campaign directories and generates a JSON data file (`folders.json`) for the website.
-   **Recursive Search:** The script finds all images within a dealer's folder, no matter how many subfolders are present.
-   **Header/Body Separation:** The gallery distinguishes between "header" images (`.gif`) and "body" images (`.png`, `.jpg`).
-   **Deployment-Ready:** Includes a `wrangler.toml` file for easy deployment to Cloudflare Pages.

## Project Structure

```
.
├── sindex.html               # The main HTML file for the gallery
├── folders.json              # Data file containing image paths (auto-generated)
├── update_folders_json.py    # Python script to generate folders.json
├── wrangler.toml             # Configuration for Cloudflare Pages deployment
├── dec25/                    # Example campaign folder
│   ├── cmg/                  # Dealer folder
│   │   ├── f.gif             # Header image
│   │   └── 1.png             # Body image
│   └── ...
└── ...                       # Other campaign folders
```

## Usage

To add new images or update a campaign, follow these steps:

### 1. Add Images

Add your new images to the appropriate campaign and dealer folders. If you are starting a new campaign, create a new directory (e.g., `jan26`) and add your dealer folders and images inside it.

The script recursively finds all images, so you can organize your images in subfolders as you see fit.

### 2. Update Image Index

After adding or changing images, you need to run the `update_folders_json.py` script to update the `folders.json` file. This tells the website about the new images.

Open a terminal in the project directory and run the following command, replacing `<campaign_directory>` with the name of the folder you updated:

```bash
python3 update_folders_json.py <campaign_directory>
```

**Example:**

If you added images to the `dec25` folder:
```bash
python3 update_folders_json.py dec25
```

If you created a new `jan26` folder and added images to it:
```bash
python3 update_folders_json.py jan26
```

*(Note: You need to have Python 3 installed to run this script.)*

## Deployment

This project is configured for deployment to [Cloudflare Pages](https://pages.cloudflare.com/).

To deploy the website, run the following command from the project directory:

```bash
npx wrangler pages publish .
```

This will publish your website to the URL associated with your Cloudflare Pages project.
