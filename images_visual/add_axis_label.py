import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from PIL import Image, ImageDraw,ImageFont

def add_x_label(image,label,distance,font_size=500):
    xx_label = font_size*15/500
    # print(image)
    # height, width,c = image.shape
    xpixels, ypixels, _ = image.shape
    # print(xpixels, ypixels)
    dpi = 10
    fig, ax = plt.subplots(figsize=(ypixels / dpi , xx_label),dpi=dpi)
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
    width, height = fig.get_size_inches()* fig.get_dpi()
    width, height = int(width), int(height)
    text_label = ''
    # text_label = 'Neigh2Neigh' + 10*' ' + ' Neigh2Neigh'
    for lb in label:
        distance_temp = distance - len(lb)
        text_label += lb + distance_temp*' '
    print(text_label)
    plt.text(0.01, 0.6, text_label, fontsize=font_size,fontweight='bold',horizontalalignment='left',verticalalignment='top', transform=ax.transAxes)
    # ax.imshow(image)

    # ax.axis('off')
    fig.canvas.draw()  # draw the canvas, cache the renderer

    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8').reshape(height, width, 3)
    # print(image)
    return image