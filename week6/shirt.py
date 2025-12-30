# CS50 P-Shirt
# Overlays a shirt onto a photo using PIL

import sys
from PIL import Image, ImageOps


def main():
    # Check command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Check if files have valid image extensions
    valid_extensions = [".jpg", ".jpeg", ".png"]
    input_ext = input_file.lower()
    output_ext = output_file.lower()
    
    if not any(input_ext.endswith(ext) for ext in valid_extensions):
        sys.exit("Invalid input")
    
    if not any(output_ext.endswith(ext) for ext in valid_extensions):
        sys.exit("Invalid output")
    
    # Check if extensions match
    input_extension = input_ext[input_ext.rfind("."):]
    output_extension = output_ext[output_ext.rfind("."):]
    
    if input_extension != output_extension:
        sys.exit("Input and output have different extensions")
    
    # Try to open the input image
    try:
        input_image = Image.open(input_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")
    
    # Open the shirt image
    shirt = Image.open("shirt.png")
    
    # Resize and crop the input image to match the shirt size
    size = shirt.size
    input_image = ImageOps.fit(input_image, size)
    
    # Paste the shirt onto the input image
    input_image.paste(shirt, shirt)
    
    # Save the result
    input_image.save(output_file)


if __name__ == "__main__":
    main()
