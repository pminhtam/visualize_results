import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from utils.merge_images import merge_images_row
from images_visual.add_infor import write_text_on_numpy_image
from images_visual.zoom_image import zoom_image
from glob import glob

def process_one_image(image_path,xy_zoom):
    img = Image.open(image_path).convert('RGB')
    str = ''
    if 'psnr' in image_path and 'ssim' in image_path:
        str = "PSNR=" + image_path.split('/')[-1].split('_')[-3][:5] + "\nSSIM=" + image_path.split('/')[-1].split('_')[
                                                                                    -1][:4]

    img_text = write_text_on_numpy_image(np.array(img), str)
    img_zoom = zoom_image(img_text,xy_zoom)
    return img_zoom

if __name__ == "__main__":
    xy_zoom_dict = {
                    'synthetic':(40, 200, 90, 250),
                    'dnd':(100, 350, 150, 400),
                    'polyu':(40, 150, 65, 175),
                    'renoir':(40, 150, 65, 175),
                    'sidd':(40, 150, 65, 175),
                    # 'synthetic':(40, 150, 65, 175),
                    }

    # datasets = ['dnd','polyu','renoir','sidd','sythetic']
    # datasets = ['dnd','polyu','renoir','sidd']
    datasets = ['synthetic']
    # models = ['bayes_noise2void','bayes_2model' ,'neigh2neigh', 'bayes_neigh2neigh_3_taylor_2']
    models = ['bayes_noise2void','bayes_gauss' ,'neigh2neigh', 'bayes_neigh2neigh_3_taylor_2']
    for data in datasets:
        fontsize = 140
        images_list_noise = glob(f'../images/{data}/{models[0]}*/*noise*.png')
        # print(images_list_noise)
        for image_path_noise in images_list_noise:
            list_image_merge = []
            if data == 'dnd' or data == 'sidd':
                image_name = image_path_noise.split('/')[-1][:4]
            elif data == 'synthetic':
                image_name = image_path_noise.split('/')[-1][:7]
            else:
                image_name = image_path_noise.split('/')[-1][:2]
            img_gt_zoom = None
            img_noise = Image.open(image_path_noise).convert('RGB')
            if data == 'synthetic':
                wpixels, hpixels = img_noise.size
                xy_zoom_dict['synthetic'] = int(0.1 * wpixels), int(0.75 * hpixels), int(0.2 * wpixels), int(
                    0.85 * hpixels)
                fontsize = int(140*wpixels/256)
            if data != 'dnd':
                image_path_gt = glob(f'../images/{data}/{models[0]}*/{image_name}*gt*.png')[0]
                # print(image_path_gt)
                img_gt = Image.open(image_path_gt).convert('RGB')
                img_gt_zoom = zoom_image(np.array(img_gt),xy_zoom=xy_zoom_dict[data])
            img_noise_zoom = zoom_image(np.array(img_noise),xy_zoom=xy_zoom_dict[data])
            list_image_merge.append(Image.fromarray(img_noise_zoom))
            for model_name in models:
                print(f'../images/{data}/{model_name}*/{image_name}*mu*.png')
                image_path_model_mu = glob(f'../images/{data}/{model_name}*/{image_name}*mu*.png')[0]
                image_model_mu = Image.open(image_path_model_mu).convert('RGB')
                print(image_path_model_mu)
                if data == 'dnd':
                    str_mu = ''
                else:
                    str_mu = "PSNR=" + image_path_model_mu.split('/')[-1].split('_')[-3][:5] + "\nSSIM=" + \
                            image_path_model_mu.split('/')[-1].split('_')[-1][:4]
                # print(image_path_model_mu.split('/')[-1].split('_')[4][:5])
                # print(str_mu)
                img_mu_text = write_text_on_numpy_image(np.array(image_model_mu), str_mu,fontsize=fontsize)
                img_mu_zoom = zoom_image(np.array(img_mu_text),xy_zoom=xy_zoom_dict[data])
                list_image_merge.append(Image.fromarray(img_mu_zoom))

                # print(image_path_model_mu)
                # exit()
            if img_gt_zoom is not None:
                list_image_merge.append(Image.fromarray(img_gt_zoom))
            img_merge = merge_images_row(list_image_merge,padding=3)
            img_merge.save(f'../images/merge/{data}_{image_name}_merge.png')
            # exit()
    """
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
    """
