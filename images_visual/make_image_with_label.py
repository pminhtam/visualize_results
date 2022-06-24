import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from utils.merge_images import merge_images_row,merge_images_col,merge_images_col_difference_size
from images_visual.add_axis_label import add_x_label
from images_visual.add_infor import write_text_on_numpy_image
from images_visual.zoom_image import zoom_image
from glob import glob

def resize_image_list(list_image_merge):
    """
    Resize image list to the same size
    :param list_image_merge: list of image
    :return: list of image
    """
    list_image_merge_resize = []
    w_max = 0
    for image in list_image_merge:
        w_temp,h_temp = image.size
        w_max = max(w_max,w_temp)
        # print(w_temp,h_temp)
    # print(w_max)
    for image in list_image_merge:
        wpercent = (w_max / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image_resize = image.resize((w_max, hsize), Image.ANTIALIAS)
        list_image_merge_resize.append(image_resize)
    return list_image_merge_resize

if __name__ == "__main__":
    font_size_dict = {
        'dnd': 500,
        'polyu': 200,
        'renoir': 200,
        'sidd': 200,
        'synthetic': 200,
    }

    # datasets = ['dnd','polyu','renoir','sidd','sythetic']
    datasets = ['dnd']
    # datasets = ['polyu','renoir','sidd']
    label = ['Noise','N2V','Lain19_mu' ,'N2N', 'Ours_mu']
    # label = ['Noise','N2V','Lain19_mu' ,'N2N', 'Ours_mu','Clean']
    for data in datasets:
        list_image_merge = []
        images_list_noise = glob(f'../images/merge/{data}*.png')
        for image_path_noise in images_list_noise[:5]:
            list_image_merge.append(Image.open(image_path_noise).convert('RGB'))
        img_label = add_x_label(np.array(list_image_merge[0]),label=label,distance=17,font_size=font_size_dict[data]) # dnd
        # img_label = add_x_label(np.array(list_image_merge[0]),label=label,distance=22,font_size=font_size_dict[data])
        # plt.imshow(img_label)
        # plt.show()
        img_label = Image.fromarray(img_label)
        # img_label.show()
        # exit()
        # print(img_label.size)
        # list_image_merge.append(Image.fromarray(img_label))
        img_merge = merge_images_col(list_image_merge)
        # img_merge.show()
        print(img_merge.size)
        img_merge_label = Image.new('RGB', (img_merge.size[0],
                                      img_merge.size[1] + img_label.size[1]),
                              color=(255, 255, 255))
        img_merge_label.paste(img_merge, (0,  0))
        img_merge_label.paste(img_label, (0,img_merge.size[1]))
        # plt.imshow(img_merge)
        # plt.show()
        # img_merge_label.show()
        img_merge_label.save(f'../images/{data}_merge_all.png')
        # exit()

    ###############################################################################
    """
    font_size_dict = {
        'bsd30': 480,
        'set14': 520,
        'kodak': 750,

    }
    datasets_synthetic = ['bsd30','set14','kodak']
    label = ['Noise','N2V','Lain19_mu' ,'N2N', 'Ours_mu','Clean']
    for data in datasets_synthetic:
        list_image_merge = []
        images_list_noise = glob(f'../images/merge/synthetic_*{data}*.png')
        for image_path_noise in images_list_noise[:5]:
            list_image_merge.append(Image.open(image_path_noise).convert('RGB'))
        list_image_merge = resize_image_list(list_image_merge)

        # exit()
        img_label = add_x_label(np.array(list_image_merge[0]),label=label,distance=17,font_size=font_size_dict[data]) # dnd

        img_label = Image.fromarray(img_label)

        img_merge = merge_images_col_difference_size(list_image_merge)
        # img_merge.show()
        # exit()
        print(img_merge.size)
        img_merge_label = Image.new('RGB', (img_merge.size[0],
                                      img_merge.size[1] + img_label.size[1]),
                              color=(255, 255, 255))
        img_merge_label.paste(img_merge, (0,  0))
        img_merge_label.paste(img_label, (0,img_merge.size[1]))
        # plt.imshow(img_merge)
        # plt.show()
        # img_merge_label.show()
        img_merge_label.save(f'../images/synthetic_{data}_merge_all.png')
        # exit()
    """

