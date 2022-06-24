import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from utils.merge_images import merge_images_row,merge_images_col
from images_visual.add_axis_label import add_x_label
from images_visual.add_infor import write_text_on_numpy_image
from images_visual.zoom_image import zoom_image
from glob import glob


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

