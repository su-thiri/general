from PIL import Image

def crop_image(input_path, output_path, left, top, right, bottom):
    # Open the image file
    img = Image.open(input_path)

    # Crop the image
    cropped_img = img.crop((left, top, right, bottom))

    # Save the cropped image
    cropped_img.save(output_path)

# Example usage:
input_image_path = 'logo_real.jpg'
output_image_path = 'IFCdata123.jpg'

# Define the coordinates of the area to be cropped (left, top, right, bottom)
crop_coordinates = (0,1000,900,1300)

crop_image(input_image_path, output_image_path, *crop_coordinates)

