import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from PIL import Image, ImageDraw,ImageFont

def add_x_label_one_image(ypixels ,font_size=500,lb="Clean"):
    xx_label = font_size*15/400
    # print(image)
    # height, width,c = image.shape
    # print(xpixels, ypixels)
    dpi = 10
    fig, ax = plt.subplots(figsize=(ypixels / dpi , xx_label),dpi=dpi)
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
    width, height = fig.get_size_inches()* fig.get_dpi()
    width, height = int(width), int(height)
    print(width,height)
    plt.text(0.5, 0.5, lb, fontsize=font_size, horizontalalignment='center',
                 verticalalignment='center', transform=ax.transAxes)
    plt.show()
    fig.canvas.draw()  # draw the canvas, cache the renderer

    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8').reshape(height, width, 3)
    return image

from utils.merge_images import merge_images_row
def add_x_label(image,label,font_size=10):

    xpixels, ypixels, _ = image.shape
    images_label_list = []
    yy = (ypixels - 3*len(label)) / len(label)
    for lb in label:
        image = add_x_label_one_image(yy,font_size,lb)
        images_label_list.append(Image.fromarray(image))
    img_merge = merge_images_row(images_label_list, padding=3)
    img_merge.show()
    # exit()
    return img_merge