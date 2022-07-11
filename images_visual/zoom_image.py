import matplotlib.pyplot as plt
import numpy as np
from PIL import Image,ImageEnhance
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset


def zoom_image(image,xy_zoom = (40, 150, 65, 175)):
    # x1, y1, x2, y2 = [40, 150, 65, 175]
    x1, y1, x2, y2 = xy_zoom
    xpixels, ypixels, _ = image.shape
    dpi = 10
    fig, ax = plt.subplots(figsize=(ypixels / dpi, xpixels / dpi), dpi=dpi)
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    # plt.margins(0, 0)
    width, height = fig.get_size_inches() * fig.get_dpi()
    width, height = int(width), int(height)
    ax.imshow(image)

    axins = zoomed_inset_axes(ax, 4, loc=1, borderpad=5,
                              axes_kwargs={'axisbelow': True})  # zoom-factor: 2.5, location: upper-left
    axins.imshow(image)
    axins.set_xlim(x1, x2)  # apply the x-limits
    axins.set_ylim(y2, y1)  # apply the y-limits
    plt.setp(axins.spines.values(), color='green')
    for axis in ['top', 'bottom', 'left', 'right']:
        axins.spines[axis].set_linewidth(20)  # change width
        axins.spines[axis].set_color('red')  # change color
    _patch, pp1, pp2 = mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="red",lw=10)
    # _patch, pp1, pp2 = mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="red",lw=1)
    pp1.loc1, pp1.loc2 = 2, 4  # inset corner 1 to origin corner 4 (would expect 1)
    pp2.loc1, pp2.loc2 = 3, 1  # inset corner 3 to origin corner 2 (would expect 3)

    fig.patch.set_alpha(0)
    ax.patch.set_alpha(0)
    axins.patch.set_alpha(1)
    axins.patch.set_facecolor('#909090')

    fig.canvas.draw()  # draw the canvas, cache the renderer

    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8').reshape(height, width, 3)
    return image


if __name__ == "__main__":

    # img_path = "../images/synthetic/bayes_gauss_25_checkpoint_sample_image/0_bsd300_gt.png"
    # img_path = "/home/dell/code/vin/image_denoise/visualize_results/images/polyu/bayes_neigh2neigh_3_2_polyU_checkpoint_sample_image/17_noise_psnr_35.09603584581735_ssim_0.9057411744106661.png"
    # img_path = "/home/dell/code/vin/image_denoise/visualize_results/images/sidd/bayes_neigh2neigh_3_taylor_2_checkpoint_sample_image/36_1_noise_psnr_23.759949273280498_ssim_0.46564729109977315.png"
    # img_path = "/home/dell/code/vin/image_denoise/visualize_results/images/noise_m1.png"
    # img_path = "/home/dell/code/vin/image_denoise/visualize_results/images/noise_m2.png"
    # img_path = "/home/dell/code/vin/image_denoise/visualize_results/images/synthetic/bayes_neigh2neigh_3_taylor_2_checkpoint_sample_image/1_kodak_noise_psnr_20.3816319293012_ssim_0.21652462496010783.png"
    img_path = "/home/dell/code/vin/image_denoise/visualize_results/images/synthetic/bayes_neigh2neigh_3_taylor_2_checkpoint_sample_image/1_kodak_gt.png"

    image_noise = Image.open(img_path).convert('RGB')
    enhancer = ImageEnhance.Brightness(image_noise)
    # image_noise = enhancer.enhance(2.0)
    xpixels, ypixels = image_noise.size
    xxx = xpixels*0.05 + 0.06
    yyy = ypixels*0.85 +0.26
    # xxx = xpixels*0.05 + 0.24
    # yyy = ypixels*0.85 - 0.06
    # xxx =0
    # yyy = 436
    print(xxx,yyy)
    img_noise_zoom = zoom_image(np.array(image_noise), xy_zoom=(xxx, yyy, xxx + 4, yyy+4))
    # img_noise_zoom = zoom_image(np.array(image_noise), xy_zoom=(xxx, yyy, xxx + 2, yyy+2))
    # plt.imshow(img_noise_zoom)
    # plt.show()
    img_noise_zoom= Image.fromarray(img_noise_zoom)
    img_noise_zoom.show()
    # img_noise_zoom.save("../images/1_kodak_noise_zoom.png")
    img_noise_zoom.save("../images/1_kodak_gt_zoom.png")
    # img_noise_zoom.save("../images/m2_noise_zoom.png")