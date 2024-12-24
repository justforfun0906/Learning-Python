from PIL import Image

def image_to_coe(image_path, coe_file_path):
    """
    Convert a black-and-white image to a .coe file with data width 2.

    Parameters:
    - image_path: Path to the input black-and-white image.
    - coe_file_path: Path to save the output .coe file.
    """
    # Load the image
    img = Image.open(image_path).convert("1")  # Convert to black-and-white
    width, height = img.size
    pixels = img.getdata()

    # Map pixels to 2-bit values (00 for black, 11 for white)
    data = ["0" if pixel == 0 else "1" for pixel in pixels]

    # Flatten the pixel data
    data_flattened = ",\n".join(data)

    # Write the .coe file
    with open(coe_file_path, "w") as coe_file:
        coe_file.write("memory_initialization_radix=2;\n")
        coe_file.write("memory_initialization_vector=\n")
        coe_file.write(data_flattened + ";\n")

    print(f"COE file created: {coe_file_path}")


# Example usage
file_name = input("Enter the name of the image file: ")
import os

current_directory = os.getcwd()
image_path = os.path.join(current_directory, f"{file_name}.png")
coe_file_path = os.path.join(current_directory, f"{file_name}.coe")

if os.path.exists(image_path):
    image_to_coe(image_path, coe_file_path)
else:
    print(f"Error: The file {image_path} does not exist.")
