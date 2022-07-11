import matplotlib.pyplot as plt
import numpy as np
from PIL import Image,ImageEnhance, ImageStat
from utils.merge_images import merge_images_row
from images_visual.add_infor import write_text_on_numpy_image
from images_visual.zoom_image import zoom_image
from glob import glob
import matplotlib
# matplotlib.rcParams['text.usetex'] = True

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
    # datasets = ['sidd','polyu','renoir']
    xy_zoom_dict_renoir = { '2': (130, 150, 155, 175), '3': (50,150,75,175),'9':(55,150,80,175),
                            '11':(3,170,28,195),'13':(30,150,55,175),'20':(60,150,85,175)}
    # datasets = ['renoir']
    # renoir_choosen = ['3','5','9','11','13','20']
    renoir_choosen = ['3','9','11','13','20']

    # datasets = ['sidd']
    # sidd_choosen = ['5_0_','15_0','15_1','16_1','31_0','36_1']
    sidd_choosen = ['5_0_','15_0','15_1','31_0','36_1']
    xy_zoom_dict_sidd = { '5_0_': (10, 40, 35, 65), '15_0': (50,120,75,145),'15_1':(60,160,85,185),
                            '15_2':(50,100,75,125),'16_0':(40,80,65,105),'16_1':(30,140,55,165),
                          '16_2':(70,70,95,95),'30_0':(50,120,75,145),'30_1':(40,170,75,195),
                          '31_0':(60,125,85,150),}
    datasets = ['polyu']
    polyu_choosen = ['1','10','14','17','18']
    xy_zoom_dict_polyu = { '0': (35, 175, 60, 200), '1': (45,100,70,125),'7':(40,100,65,125),
                           '8':(40,70,65,95),'9':(40,120,65,145),'10':(30,195,55,220),
                           '13':(60,50,96,75),'14':(30,170,55,195),'17':(30,140,55,165)
                           }
    # datasets = ['synthetic']
    # models = ['bayes_noise2void','bayes_2model' ,'neigh2neigh', 'bayes_neigh2neigh_3_taylor_2']
    models = ['bayes_noise2void','bayes_2model' ,'neigh2neigh','noise2same', 'bayes_neigh2neigh_3_taylor_2']
    # models = ['bayes_noise2void','bayes_gauss' ,'neigh2neigh', 'bayes_neigh2neigh_3_taylor_2']
    # models = ['bayes_noise2void','bayes_gauss' ,'neigh2neigh','noise2same', 'bayes_neigh2neigh_3_taylor_2']
    for data in datasets:
        fontsize = 210
        images_list_noise = glob(f'../images/{data}/{models[0]}*/*noise*.png')
        # print(images_list_noise)

        for image_path_noise in images_list_noise:
            xy_zoom_image = xy_zoom_dict[data]
            # if image_path_noise.split("/")[-1].split("_")[0] != "14":
            #     continue
            if image_path_noise.split("/")[-1].split("_")[0] not in polyu_choosen:
            # if image_path_noise.split("/")[-1][:4] not in sidd_choosen:
            # if image_path_noise.split("/")[-1].split("_")[0] not in renoir_choosen:
                continue
            if image_path_noise.split("/")[-1].split("_")[0] in xy_zoom_dict_polyu.keys():
                xy_zoom_image = xy_zoom_dict_polyu[image_path_noise.split("/")[-1].split("_")[0]]
            # if image_path_noise.split("/")[-1][:4] in xy_zoom_dict_sidd.keys():
            #     xy_zoom_image = xy_zoom_dict_sidd[image_path_noise.split("/")[-1][:4]]
            # if image_path_noise.split("/")[-1].split("_")[0] in xy_zoom_dict_renoir.keys():
            #     xy_zoom_image = xy_zoom_dict_renoir[image_path_noise.split("/")[-1].split("_")[0]]
                # continue
            # continue
            list_image_merge = []
            if data == 'dnd' or data == 'sidd':
                image_name = image_path_noise.split('/')[-1][:4]
            elif data == 'synthetic':
                image_name = image_path_noise.split('/')[-1][:7]
            else:
                image_name = image_path_noise.split('/')[-1][:2]
            img_gt_zoom = None
            img_noise = Image.open(image_path_noise).convert('RGB')
            # print(img_noise.getextrema())
            # print(max(img_noise.getextrema()))
            stat = ImageStat.Stat(img_noise)
            # print(np.mean(stat.mean))
            enhance_value = 100.0/np.mean(stat.mean)
            if enhance_value > 1.0:
                if enhance_value < 3.5:
                    pass
                else:
                    enhance_value = 3.5
            else:
                enhance_value = 1.2
            # enhance_value = 1.75
            # enhance_value = 250.0/max(img_noise.getextrema())[1]
            enhancer = ImageEnhance.Brightness(img_noise)
            img_noise = enhancer.enhance(enhance_value)
            if data == 'synthetic':
                wpixels, hpixels = img_noise.size
                xy_zoom_dict['synthetic'] = int(0.1 * wpixels), int(0.75 * hpixels), int(0.2 * wpixels), int(
                    0.85 * hpixels)
                fontsize = int(175*wpixels/256)
            if data != 'dnd':
                image_path_gt = glob(f'../images/{data}/{models[0]}*/{image_name}*gt*.png')[0]
                # print(image_path_gt)
                img_gt = Image.open(image_path_gt).convert('RGB')
                enhancer = ImageEnhance.Brightness(img_gt)
                img_gt = enhancer.enhance(enhance_value)
                img_gt_zoom = zoom_image(np.array(img_gt),xy_zoom=xy_zoom_image)
            img_noise_zoom = zoom_image(np.array(img_noise),xy_zoom=xy_zoom_image)
            list_image_merge.append(Image.fromarray(img_noise_zoom))
            for model_name in models:
                print(f'../images/{data}/{model_name}*/{image_name}*mu*.png')
                image_path_model_mu = glob(f'../images/{data}/{model_name}*/{image_name}*mu*.png')[0]
                image_model_mu = Image.open(image_path_model_mu).convert('RGB')
                enhancer = ImageEnhance.Brightness(image_model_mu)
                image_model_mu = enhancer.enhance(enhance_value)
                print(image_path_model_mu)
                if data == 'dnd':
                    str_mu = ''
                else:
                    # str_mu = r"PSNR=" + image_path_model_mu.split('/')[-1].split('_')[-3][:5] + "\nSSIM=" + \
                    #         image_path_model_mu.split('/')[-1].split('_')[-1][:4]
                    str_mu = r"" + image_path_model_mu.split('/')[-1].split('_')[-3][:5] + "/" + image_path_model_mu.split('/')[-1].split('_')[-1][:4]
                # print(image_path_model_mu.split('/')[-1].split('_')[4][:5])
                # print(str_mu)
                img_mu_text = write_text_on_numpy_image(np.array(image_model_mu), str_mu,fontsize=fontsize)
                img_mu_zoom = zoom_image(np.array(img_mu_text),xy_zoom=xy_zoom_image)
                list_image_merge.append(Image.fromarray(img_mu_zoom))

                # print(image_path_model_mu)
                # exit()
            if img_gt_zoom is not None:
                list_image_merge.append(Image.fromarray(img_gt_zoom))
            img_merge = merge_images_row(list_image_merge,padding=3)
            # img_merge.show()
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
