import os
import requests
from google_images_search import GoogleImagesSearch

class GoogleImageDownloader:
    def __init__(self, api_key, cx):
        """Initialize with Google Custom Search API credentials"""
        self.gis = GoogleImagesSearch(api_key, cx)

    def download_images(self, query, num_images=5, output_dir='downloads'):
        """Download images from Google based on search query"""
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Define search parameters
        search_params = {
            'q': query,
            'num': num_images,
            'safe': 'high',
            'fileType': 'jpg|png',
            'imgType': 'photo',
            'rights': 'cc_publicdomain|cc_attribute|cc_sharealike'
        }

        try:
            # Search and download images
            self.gis.search(search_params=search_params)
            
            for i, image in enumerate(self.gis.results(), 1):
                try:
                    # Download image
                    image.download(output_dir)
                    print(f'Successfully downloaded image {i}')
                except Exception as e:
                    print(f'Error downloading image {i}: {str(e)}')

            print(f'\nDownload complete! Images saved in {output_dir}')

        except Exception as e:
            print(f'Error during search: {str(e)}')

def main():
    # Replace these with your actual API credentials
    API_KEY = 'AIzaSyCNzm-1vqtEFhOyvaV-RggBU3KDcJLsxY0'
    CX = 'c4dde8b42aebb458d'

    # Create downloader instance
    downloader = GoogleImageDownloader(API_KEY, CX)

    # Example usage
    query = input('Enter search term: ')
    num_images = int(input('How many images to download? '))
    output_dir = input('Enter output directory (default: downloads): ') or 'downloads'

    # Download images
    downloader.download_images(query, num_images, output_dir)

if __name__ == '__main__':
    main()