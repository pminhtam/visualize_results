import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from PIL import Image, ImageDraw,ImageFont

def write_text_on_pil_image(image,text):
    draw = ImageDraw.Draw(image)
    x, y = (0,0)
    h,w = (30,6*len(text))
    draw.rectangle((x, y, x + w, y + h), fill=(200,200,200))
    draw.text((0, 0), text, fill=(255, 0, 0))
    return draw
def write_text_on_numpy_image(image,text):
    # print(image)
    # height, width,c = image.shape
    xpixels, ypixels, _ = image.shape
    # print(xpixels, ypixels)
    dpi = 10
    fig, ax = plt.subplots(figsize=(ypixels / dpi, xpixels / dpi),dpi=dpi)
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    # plt.margins(0, 0)
    width, height = fig.get_size_inches()* fig.get_dpi()
    width, height = int(width), int(height)

    ax.imshow(image)
    # ax.text(1.0, 1.0, text,horizontalalignment='left',verticalalignment='top', bbox=dict(fill=True, linewidth=2,facecolor='red',edgecolor='red'),fontsize=110)
    ax.text(2.0, 2.0, text,horizontalalignment='left',verticalalignment='top',color='red', bbox=dict(fill=True, linewidth=2,facecolor=(0.8,0.8,0.8),edgecolor=(0.8,0.8,0.8)),fontsize=110)
    # ax.axis('off')
    fig.canvas.draw()  # draw the canvas, cache the renderer

    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8').reshape(height, width, 3)
    # print(image)
    return image

if __name__ == "__main__":
    img_path = "../images/bayes_gauss_25_checkpoint_sample_image/0_bsd300_gt.png"
    image_noise = Image.open(img_path).convert('RGB')
    # write_text_on_pil_image(image_noise,"hello every asdwaefsgg \n efwefw")
    image_noise = np.array(image_noise)
    image_noise=write_text_on_numpy_image(image_noise,"PSNR = 23.53 \nSSIM = 0.61")
    xpixels, ypixels,_ = image_noise.shape
    print(xpixels,ypixels)
    dpi = 10
    fig, ax = plt.subplots(figsize=(ypixels / dpi, xpixels / dpi),dpi=dpi)
    # fig, ax = plt.subplots()
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
    ax.imshow(image_noise)
    # plt.axis('off')
    # plt.text(1, 1, "string ccccccccedefwef\n adadef",horizontalalignment='left',verticalalignment='top', bbox=dict(fill=True, edgecolor='red', linewidth=2),fontsize=150)
    plt.show()