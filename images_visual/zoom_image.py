import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset


def zoom_image(image,x1=0,y1=0,x2=0,y2=0):
    x1, y1, x2, y2 = [100, 150, 130, 210]

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

    img_path = "../images/bayes_gauss_25_checkpoint_sample_image/0_bsd300_gt.png"
    image_noise = Image.open(img_path).convert('RGB')
    image_noise = np.array(image_noise)
    xpixels, ypixels,_ = image_noise.shape
    print(xpixels,ypixels)
    dpi = 10
    fig, ax = plt.subplots(figsize=(ypixels / dpi, xpixels / dpi),dpi=dpi)
    # fig, ax = plt.subplots()
    # print(image_noise)
    # make data
    # Z, extent = get_demo_image()
    # Z2 = np.zeros((150, 150))
    # ny, nx = Z.shape
    # Z2[30:30+ny, 30:30+nx] = Z
    # plt.gca().set_axis_off()
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
    ax.imshow(image_noise)
    # plt.axis('off')
    # plt.show()
    # # inset axes....
    # axins = ax.inset_axes([0.5, 0.5, 0.47, 0.47])
    # axins.imshow(Z2, extent=extent, origin="lower")
    # # sub region of the original image
    # x1, x2, y1, y2 = -1.5, -0.9, -2.5, -1.9
    # axins.set_xlim(x1, x2)
    # axins.set_ylim(y1, y2)
    # axins.set_xticklabels([])
    # axins.set_yticklabels([])
    # #
    # ax.indicate_inset_zoom(axins, edgecolor="black")
    from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar

    # def add_sizebar(ax, size):
    #     asb = AnchoredSizeBar(ax.transData,
    #                           size,
    #                           str(size),
    #                           loc=8,
    #                           pad=0.1, borderpad=0.5, sep=5,
    #                           frameon=False)
    #     ax.add_artist(asb)

    x1, y1, x2, y2 = [100, 150, 130, 210]
    axins = zoomed_inset_axes(ax, 4, loc=1,borderpad =5,axes_kwargs={'axisbelow':True}) # zoom-factor: 2.5, location: upper-left
    # axins = inset_axes(ax, 2,2, loc=1,bbox_to_anchor=(0.75, 0.75),bbox_transform=ax.figure.transFigure) # zoom-factor: 2.5, location: upper-left
    axins.imshow(image_noise)
    axins.set_xlim(x1, x2) # apply the x-limits
    axins.set_ylim(y2, y1) # apply the y-limits
    # axins.set_edgecolor('green') # apply the y-limits
    plt.setp(axins.spines.values(), color='green')
    print(axins.spines.values())
    for axis in ['top', 'bottom', 'left', 'right']:
        axins.spines[axis].set_linewidth(20)  # change width
        axins.spines[axis].set_color('red')    # change color

    # plt.setp([axins.get_xticklines(), axins.get_yticklines()], color='green')

    # axins.yaxis.get_major_locator().set_params(nbins=7)
    # axins.xaxis.get_major_locator().set_params(nbins=7)

    # plt.setp(axins.get_xticklabels(), visible=False)
    # plt.setp(axins.get_yticklabels(), visible=False)


    # add_sizebar(axins, 5)
    # axins.set_linewidth(2.5)  # change width
    # axins.set_color('red')  # change color
    # plt.yticks(visible=False)
    # plt.xticks(visible=False)
    # _patch, pp1, pp2 = mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="red",lw=10,joinstyle="bevel",rasterized=True,zorder=1,facecolor="blue")
    _patch, pp1, pp2 = mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="red",lw=10)
    # _patch, pp1, pp2 = mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="red",lw=1)
    pp1.loc1, pp1.loc2 = 2, 4  # inset corner 1 to origin corner 4 (would expect 1)
    pp2.loc1, pp2.loc2 = 3, 1  # inset corner 3 to origin corner 2 (would expect 3)

    fig.patch.set_alpha(0)
    ax.patch.set_alpha(0)
    axins.patch.set_alpha(1)
    axins.patch.set_facecolor('#909090')

    plt.show()