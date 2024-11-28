from PIL import Image
from rembg import remove 
import os

def convert_image(input_path, output_path, format='PNG'):
    """
    Convert image from one format to another
    Args:
        input_path: Path to source image
        output_path: Path to save converted image
        format: Target format (default: PNG)
    """
    try:
        # Verify input file exists
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input file not found: {input_path}")
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        # Open image and convert
        with Image.open(input_path) as img:
            img = remove(img)
            img.save(output_path, format=format)
            print(f"Image successfully converted to {format} format!")
    except Exception as e:
        print(f"Error converting image: {str(e)}")

# Example usage
convert_image('images/certificate.jpg', 'images/certificate.png')
