'''This snippet removes pixels with values higher than certain amount in rgb'''
from PIL import Image
import os


def transparent(name_in, limit = (150,150,150)):
	file_path = os.path.join(os.getcwd(), "input_pics", name_in)	
	img = Image.open(file_path)
	img = img.convert("RGBA")
	pixels = img.load()
	for y in range(img.size[1]):
		for x in range(img.size[0]):
			r,g,b,a = pixels[x,y]
			if r > limit[0] or g > limit[1] or b > limit[2]:
				pixels[x,y] = (r, g, b, 0)
	file_out = file_path = os.path.join(os.getcwd(), "output_pics", name_in[:-4]+'_result.png')	
	img.save(file_out)


if __name__ == '__main__':
	filename = "myfile.jpg"
	transparent(filename)