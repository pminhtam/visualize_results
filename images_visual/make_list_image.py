import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from utils.merge_images import merge_images_row
from images_visual.add_infor import write_text_on_numpy_image
from images_visual.zoom_image import zoom_image
if __name__ == "__main__":
    img_path_0 = "../images/bayes_gauss_25_checkpoint_sample_image/0_bsd300_gt.png"
    img_path_1 = "../images/bayes_gauss_25_checkpoint_sample_image/0_bsd300_mu_psnr_33.043701137559964_ssim_0.8668264308307748.png"
    img_path_2 = "../images/bayes_gauss_25_checkpoint_sample_image/0_bsd300_pme_psnr_33.4692176798068_ssim_0.874566267886879.png"
    img_path_3 = "../images/bayes_gauss_25_checkpoint_sample_image/0_bsd300_noise_psnr_20.61253170933923_ssim_0.2564386433838313.png"
    # img_path_4 = "../images/bayes_gauss_25_checkpoint_sample_image/4_bsd300_gt.png"

    img_0 = Image.open(img_path_0).convert('RGB')
    img_1 = Image.open(img_path_1).convert('RGB')
    img_2 = Image.open(img_path_2).convert('RGB')
    img_3 = Image.open(img_path_3).convert('RGB')

    img_0_text = write_text_on_numpy_image(np.array(img_0), img_path_0.split('/')[-1])
    str_1 = "PSNR=" + img_path_1.split('/')[-1].split('_')[4][:5] + "\nSSIM=" + img_path_1.split('/')[-1].split('_')[-1][:4]
    img_1_text = write_text_on_numpy_image(np.array(img_1), str_1)
    str_2 = "PSNR=" + img_path_2.split('/')[-1].split('_')[4][:5] + "\nSSIM=" + img_path_2.split('/')[-1].split('_')[-1][:4]
    img_2_text = write_text_on_numpy_image(np.array(img_2), str_2)
    str_3 = "PSNR=" + img_path_3.split('/')[-1].split('_')[4][:5] + "\nSSIM=" + img_path_3.split('/')[-1].split('_')[-1][:4]
    img_3_text = write_text_on_numpy_image(np.array(img_3), str_3)

    img_0_zoom = zoom_image(img_0_text)
    img_1_zoom = zoom_image(img_1_text)
    img_2_zoom = zoom_image(img_2_text)
    img_3_zoom = zoom_image(img_3_text)

    img_merge = merge_images_row([Image.fromarray(img_0_zoom), Image.fromarray(img_1_zoom), Image.fromarray(img_2_zoom), Image.fromarray(img_3_zoom)],padding=3)
    # print(img_merge)
    ypixels, xpixels = img_merge.size
    print(xpixels,ypixels)
    dpi = 10
    fig, ax = plt.subplots(figsize=(ypixels / dpi, xpixels / dpi),dpi=dpi)
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
    plt.imshow(img_merge)
    plt.axis('off')
    plt.show()
