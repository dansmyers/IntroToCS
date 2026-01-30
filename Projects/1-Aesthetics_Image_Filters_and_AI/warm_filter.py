"""
An example warm filter using the Pillow library

The program opens the image, splits it into red, green, and blue
channels, then enhances the red and yellow components, while slightly
de-emphasizing the blue component
"""

from PIL import Image, ImageEnhance

# Specify the input and output image paths
input_image = "cute_yarn_robot.jpeg"  # Replace with your input image path
output_image = "warm_output.jpeg"

# Open the image
img = Image.open(input_image)

# Ensure the image is in RGB mode
img = img.convert('RGB')

# Split the image into its RGB channels
r, g, b = img.split()

# Enhance red channel
r_enhancer = ImageEnhance.Brightness(r)
r = r_enhancer.enhance(1.2)  # Increase red brightness by 20%

# Enhance green channel slightly (to add some yellow)
g_enhancer = ImageEnhance.Brightness(g)
g = g_enhancer.enhance(1.1)  # Increase green brightness by 10%

# Reduce blue channel slightly
b_enhancer = ImageEnhance.Brightness(b)
b = b_enhancer.enhance(0.9)  # Decrease blue brightness by 10%

# Merge the modified channels
warm_img = Image.merge('RGB', (r, g, b))

# Optionally, enhance the overall color saturation
color_enhancer = ImageEnhance.Color(warm_img)
warm_img = color_enhancer.enhance(1.2)  # Increase color saturation by 20%

# Save the result
warm_img.save(output_image)

print(f"Warm filter image saved as {output_image}")
