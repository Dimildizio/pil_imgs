from PIL import Image, ImageEnhance
import os
import numpy as np
import time
from random import choice

def rotate(image_path, degrees_to_rotate, saved_location):
    image_obj = Image.open(image_path)
    rotated_image = image_obj.rotate(
        degrees_to_rotate, resample = Image.BICUBIC) #expand = True
    rotated_image.save(saved_location)

    

def make_sprites(path = ''):
	print(path)
	img = path + '1.png'
	d = {'upright':315, 'right':270, 'downright':225, 'down':180, 'downleft':135,
	     'left':90, 'upleft':45, 'up':0}
	for key,val in d.items():

		if not os.path.isfile(img):
			key = path+key+'.png'
			rotate(img, val, key)
			
def get_color_rgb(img):
    im = Image.open(img)
    rgb_im = im.convert('RGB')
    a = []
    result = []
    for x in range(0,20):
        for y in range(0,20):
            a.append((x,y))
    for x in a:
        r, g, b = rgb_im.getpixel(x)
        result.append((r,g,b))
    with open('colours.txt', 'w') as f:
        for x in result:
            print(x, file = f)
    return result

def convertme(initial, names, to_save = '', wd = False):
    if wd:
        os.chdir(wd)
    background = Image.open(initial)
    if type(names) == list:
        for x in names:
            x = str(x)
            if '.png' not in x:
                x = x + '.png'
            foreground = Image.open(x)
            background.paste(foreground, (0, 0), foreground)
            background.save(to_save+'1.png')
        background.show()

def convert64_v1(path, name, to_save = '', size = 64):
    background = Image.new('RGBA',(size, size))
    foreground = Image.open(path+name)
    foreground = foreground.convert('RGBA')
    w,h = foreground.size
    background.paste(foreground, ((size-w)//2, (size-h)//2), foreground)
    background.save(path+to_save+'_64.png')
    background.show()

def reduce_opacity(path, image, opacity):
    image = Image.open(path+image)
    im = image.convert('P', palette=Image.ADAPTIVE)
    assert opacity >= 0 and opacity <= 1
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    else:
        im = im.copy()
    alpha = im.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    im.putalpha(alpha)
    
    im.save(path+'1.png')
    return im

def change_colour(filename, orig_color, replacement_color):
    img = Image.open(filename).convert('RGB')
    data = np.array(img)
    data[(data == orig_color).all(axis = -1)] = replacement_color
    img2 = Image.fromarray(data, mode='RGB')
    img2.save('new_color.png')
    img2.show()


def change(path, image, orig_color, replacement_color, transp = False):
    im = Image.open(path+image)
    rgb_im = im.convert('RGBA')
    w,h = im.size
    pixels = rgb_im.load()
    for x in range(0,w):
        for y in range(0,h):
            if pixels[x,y][:3] == orig_color:
                if not transp:
                    pixels[x,y] = replacement_color+tuple(pilxels[x,y][3])
                else:
                    pixels[x,y] = replacement_color + (transp,)
    rgb_im.save(path + 'newcolor.png')


def resize(path, img, name, size = (64,64)):
    try:
        im = Image.open(path+img)
        im.thumbnail(size)
        im.save(path+name)
    except IOError:
        print("cannot create thumbnail for", img)


def cropme(path, img, p):# startW,startH,endW, endH):
    img = Image.open(path+img)
    
    region1size = 50
    #return img.getpixel((800,400))
    region = img.crop((0,0,508,420))
    region1 = img.crop((0,3, 508, region1size))

    region2 = img.crop((0,70, 508, 220))
    region2 = region2.rotate(180, resample = Image.BICUBIC) 
    region.paste(region2, (5,220), region2)
    rotated = region1.rotate(180, resample = Image.BICUBIC) 
    region.paste(rotated, (5,422-region1size), rotated)
    #region = region.rotate(90, resample = Image.BICUBIC)
    region.thumbnail((220,220))
    region.save(path+p+'.png')
    region.show()


def crop_to32(path, img, name):
    img = Image.open(path+img)
    pos1,pos2 = 324,0 #32*64, 1*64
    region = img.crop((pos1, pos2, pos1+30, pos2+26))#+64))
    #region.thumbnail((32,32))
    #region.show()
    region.save(path+name+'1.png')

def smaller(path, img, name=False):
    img = Image.open(path+img)
    w,h = img.size
    region = img.crop((0, 0, min(w,64), min(h,54)))
    region.save((path+name+'.png'))

def make_transparent(image, name = 'lol.png'):
    img = Image.open(image)
    img = img.convert("RGBA")

    pixdata = img.load()

    width, height = img.size
    for y in range(height):
        for x in range(width):
            r,g,b,t = pixdata[x, y]
            if r > 250 and g > 250 and b > 250 and t > 200:
                #if pixdata[x, y] == (255, 255, 255, 255):
                pixdata[x, y] = (255, 255, 255, 0)

    img.save('images/'+name)

def white_to_transparency(img):
    x = np.asarray(img.convert('RGBA')).copy()
    x[:, :, 3] = (255 * (x[:, :, :3] != 255).any(axis=2)).astype(np.uint8)
    return Image.fromarray(x)

aquamarine = (127,255,212)
lightgold = (250,250,210)
steelblue = (176,196,222)
palegreen = (152,251,152)
darkcyan = (0,139,139)
plum = (221,160,221)
darkgray = (169,169,169)
white = (255,255,255)
red = (255, 0,0)
blue = (0,0,255)
green = (0,255,0)
maroon = (128,0,0)
firebrick = (178, 34, 34)
ilist = [aquamarine, lightgold, steelblue, palegreen, darkcyan, darkgray, white, red, green, blue, maroon]


def convert64_v2(path, name, to_save = '', size = 64):     
    background = Image.new('RGBA',(size, size))
    foreground = Image.open(path+name)
    foreground = foreground.convert('RGBA')
    w,h = foreground.size
    pos = (0,0)
    background.paste(foreground, pos, foreground)
    background.save(path+to_save)
    background.show()

if __name__ == '__main__':
    pass

