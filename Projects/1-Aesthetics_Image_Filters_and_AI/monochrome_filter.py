"""
A monchrome filter using the Pillow library

The program opens the image, converts it to a grayscale format,
then slightly enhances the contrast
"""

from PIL import Image, ImageEnhance

# Specify the input and output image paths
input_image = "cute_yarn_robot.jpeg"  # Replace with your input image path
output_image = "monochrome_output.jpeg"

# Open the image
img = Image.open(input_image)

# Convert the image to grayscale
grayscale = img.convert('L')
    
# Enhance the contrast
enhancer = ImageEnhance.Contrast(grayscale)
enhanced = enhancer.enhance(1.5)  # Increase contrast by 50%
    
# Save the result
enhanced.save(output_image)

print(f"Monochrome image saved as {output_image}")
