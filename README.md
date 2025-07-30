# Google Image Downloader

A Python application that downloads images from Google using the Google Custom Search API.

## Setup

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Get your Google API credentials:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one
   - Enable the Custom Search API
   - Create API credentials (API key)
   - Go to [Google Programmable Search Engine](https://programmablesearchengine.google.com/)
   - Create a new search engine
   - Get your Search Engine ID (cx)

3. Update the `google_image_downloader.py` file with your API credentials:
   ```python
   API_KEY = 'YOUR_GOOGLE_API_KEY'
   CX = 'YOUR_CUSTOM_SEARCH_ENGINE_ID'
   ```

## Usage

Run the script:
```bash
python google_image_downloader.py
```

The script will prompt you for:
1. Search term
2. Number of images to download
3. Output directory (defaults to 'downloads')

## Features

- Downloads images based on search query
- Supports customizable number of images
- Creates output directory if it doesn't exist
- Downloads only safe images
- Supports jpg and png formats
- Downloads only photos (no clipart or drawings)
- Downloads images with Creative Commons licenses

## Error Handling

The application includes error handling for:
- Failed downloads
- API errors
- Invalid input

## License

This project is licensed under the MIT License.
