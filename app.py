from PIL import Image
import numpy
from blend_modes import soft_light

def cut_image(image, width, height = 0):
	center_width = len(image[0]) / 2
	center_height = len(image) / 2
	if height == 0:
		init_width = int(center_width - (width/2))
		end_width = int(init_width + width)
		init_height = int(center_height - (width/2))
		end_height = int(init_height + width)
	else:
		init_width = int(center_width - (width/2))
		end_width = int(init_width + width)
		init_height = int(center_height - (height/2))
		end_height = int(init_height + height)
	return image[init_height:end_height, init_width:end_width]


bg_path = input("Background image path: ")
# Loads backgroung image and converts to RGBA so 
# the blend modes module can work
bg_img = Image.open(bg_path).convert("RGBA")

# Shows loaded image
# bg_img.show()


ov_path = input("Overlay image path: ")
# Loads backgroung image and converts to RGBA so 
# the blend modes module can work
ov_img = Image.open(ov_path).convert("RGBA")

# Shows loaded image
# ov_img.show()

# Converts images to arrays of float type so
# the blend modes module can work
bg_img_arr = numpy.array(bg_img).astype(float)
ov_img_arr = numpy.array(ov_img).astype(float)

# Gets background image height and width
bg_height = len(bg_img_arr)
bg_width = len(bg_img_arr[0])

# Gets overlay image height and width
ov_height = len(ov_img_arr)
ov_width = len(ov_img_arr[0])

width = min(bg_width, ov_width)
height = min(bg_height, ov_height)
square = min(width, height)

print("What cut style do you want?")
print("   (1) square")
print("   (2) the best the app can do (hehehe)")
cut_style = int(input("Selected number option: "))

if cut_style == 1:
	bg_img_arr = cut_image(bg_img_arr, square)
	ov_img_arr = cut_image(ov_img_arr, square)
elif cut_style == 2:
	bg_img_arr = cut_image(bg_img_arr, width, height)
	ov_img_arr = cut_image(ov_img_arr, width, height)

# Cuts the images to 500x500px
# The iamges need to have the same size to
# be blended using the blend modes module
# bg_img_arr = bg_img_arr[0:500, 0:500]
# ov_img_arr = ov_img_arr[0:500, 0:500]

# Selects the opacity that the images will be blended
# (the overlay over the background)
opacity = float(input("Opacity: "))
# Blend the images using soft light mode
final_img_arr = soft_light(bg_img_arr, ov_img_arr, opacity)

# Transforms array of floats to array of unsigned integer
# between 0 and 255
final_img_arr = numpy.uint8(final_img_arr)
# Transforms array to image
final_img = Image.fromarray(final_img_arr)

# Show the final blended image
final_img.show()