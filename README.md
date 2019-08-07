# pil_imgs
Several PIL functions to work with pngs (mostly).

Requires pillow library and numpy

Functions:

    rotate - rotates an image
    make_sprites - creates 8 rotated in 8 directions images
    get_color_rgb - outputs a rgb pixel matrix for certain px region in image
    convertme - pastes one image onto another
    convert_64_v1 - pastes and centers smaller image onto transparent canvas
    conver_64_v2 - same
    reduce_opacity - make image less intense
    change_colour - replaces arg2 colour with arg3 colour
    change - same but with set transparency
    resize - resizes image to x,y
    cropme - cut two parts of the image, puts them onto one another and resizes
    crop_to32 - crops part of the image
    smaller - takes min([size, num]) and crops it from image
    make_transparent - makes whiter pixels transparent
    white_to_transparency - same with numpy
