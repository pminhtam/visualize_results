from PIL import Image

def merge_images_row(img_list,padding=10):
    img_merge = Image.new('RGB', (img_list[0].size[0] * len(img_list) + padding*(len(img_list)-1),
                                  img_list[0].size[1]),color = (255, 255, 255))
    for i, img in enumerate(img_list):
        img_merge.paste(img, (i * (img.size[0] + padding), 0))
    return img_merge

def merge_images_col(img_list,padding=10):
    img_merge = Image.new('RGB', (img_list[0].size[0],
                                  img_list[0].size[1] * len(img_list) + padding*(len(img_list)-1)),color = (255, 255, 255))
    for i, img in enumerate(img_list):
        img_merge.paste(img, (0, i * (img.size[1] + padding)))
    return img_merge
def merge_images_col_difference_size(img_list,padding=10):
    h_size = 0
    for img in img_list:
        h_size += img.size[1] + padding
    h_size -=padding
    img_merge = Image.new('RGB', (img_list[0].size[0],
                                  h_size),color=(255, 255, 255))
    h_next = 0
    for i, img in enumerate(img_list):
        img_merge.paste(img, (0, h_next))
        h_next += img.size[1] + padding
    return img_merge
if __name__=="__main__":
    img_01 = Image.open("digit-number-img-0.jpg")
    img_02 = Image.open("digit-number-img-1.jpg")
    img_03 = Image.open("digit-number-img-2.jpg")
    img_04 = Image.open("digit-number-img-3.jpg")

    img_01_size = img_01.size
    img_02_size = img_02.size
    img_03_size = img_02.size
    img_04_size = img_04.size

    print('img 1 size: ', img_01_size)
    print('img 2 size: ', img_02_size)
    print('img 3 size: ', img_03_size)
    print('img 4 size: ', img_04_size)

    new_im = Image.new('RGB', (2 * img_01_size[0], 2 * img_01_size[1]), (250, 250, 250))

    new_im.paste(img_01, (0, 0))
    new_im.paste(img_02, (img_01_size[0], 0))
    new_im.paste(img_03, (0, img_01_size[1]))
    new_im.paste(img_04, (img_01_size[0], img_01_size[1]))

    new_im.save("merged_images.png", "PNG")
    new_im.show()