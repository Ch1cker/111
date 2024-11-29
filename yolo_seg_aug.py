import os
import cv2

img_path = './kedu_data_8/images/val/'
txt_path = './kedu_data_8/labels/val/'
output_path = './yolo_seg_output/'



# 获取txt_path中的全部文件名
# os.listdir(path): 列出指定目录下的所有文件和目录名。
# os.getcwd(): 返回当前工作目录的路径。
# os.mkdir(path): 创建一个新目录。
# os.chdir(path): 改变当前工作目录到指定的路径。


def h_Mirror_Anno(txt_path, output_path):
    txt_files = os.listdir(txt_path)
    for txt_file in txt_files:

        # open文件的名称改为txt_path+'文件名'形式
        with open(txt_path + txt_file) as f:
            txt_list = f.readlines()
            print('txt_list:', txt_list)
            new_txt_list = []
            for i in range(len(txt_list)):
                # print('txt_list[0]:', txt_list[i])
                # print(type(txt_list[i]))
                str_list = txt_list[i].split()
                # print('original str_list:', str_list)

                classes, x1, y1, x2, y2, x3, y3, x4, y4 = str_list

                x1 = str(1 - float(x1))
                x2 = str(1 - float(x2))
                x3 = str(1 - float(x3))
                x4 = str(1 - float(x4))

                new_str_list = [classes, x1, y1, x2, y2, x3, y3, x4, y4]
                # print('new_str_list:', new_str_list)

                new_line = ' '.join(new_str_list) + '\n'

                # print('new_line:', new_line, '\n')
                # print('type of new_line:', type(new_line))

                new_txt_list.append(new_line)

            print('H mirror annotation new_txt_list:', new_txt_list)

            # 接下来是保存改好的txt文件。
            # 保存文件
            if not os.path.exists(output_path):
                os.makedirs(output_path)

            output_label_path = output_path + 'labels/'
            # print('output_label_path:', output_label_path)
            if not os.path.exists(output_label_path):
                os.makedirs(output_label_path)
            new_label_file = txt_file[0:-4] + '_h' + '.txt'
            # print('output_label_path+new_txt_file:', output_label_path + new_label_file)

            if os.path.exists(output_label_path + new_label_file):
                raise Exception('The destination annotation file already exists')

            with open(output_label_path + new_label_file, 'w+', encoding='utf-8') as f:
                f.writelines(new_txt_list)

    print('\n', 'annotation horizontal mirror has been completed')


def h_Mirror_Img(img_path, output_path):
    img_files = os.listdir(img_path)
    output_image_path = output_path + 'images/'

    if not os.path.exists(output_image_path):
        os.makedirs(output_image_path)

    for img_file in img_files:
        img = cv2.imread(img_path + img_file)
        # cv2.imshow('before', img)
        # cv2.waitKey(4000)
        # cv2.destroyAllWindows()

        mirror_img = cv2.flip(img, 1)  #

        new_img_file = img_file[0:-4] + '_h' + img_file[-4:]
        # print('img_file:',img_file)
        # print('new_img_file:',new_img_file)

        if os.path.exists(output_image_path + new_img_file):
            raise Exception('The destination image file already exists')

        cv2.imwrite(output_image_path + new_img_file, mirror_img)
        # cv2.imshow('after', mirror_img)
        # cv2.waitKey(2000)
        # cv2.destroyAllWindows()
    print('\n', 'image horizontal mirror has been completed')


def v_Mirror_Anno(txt_path, output_path):
    txt_files = os.listdir(txt_path)
    for txt_file in txt_files:

        # open文件的名称改为txt_path+'文件名'形式
        with open(txt_path + txt_file) as f:
            txt_list = f.readlines()
            print('txt_list:', txt_list)
            new_txt_list = []
            for i in range(len(txt_list)):
                # print('txt_list[0]:', txt_list[i])
                # print(type(txt_list[i]))
                str_list = txt_list[i].split()
                # print('original str_list:', str_list)

                classes, x1, y1, x2, y2, x3, y3, x4, y4 = str_list

                y1 = str(1 - float(y1))
                y2 = str(1 - float(y2))
                y3 = str(1 - float(y3))
                y4 = str(1 - float(y4))

                new_str_list = [classes, x1, y1, x2, y2, x3, y3, x4, y4]
                # print('new_str_list:', new_str_list)

                new_line = ' '.join(new_str_list) + '\n'

                # print('new_line:', new_line, '\n')
                # print('type of new_line:', type(new_line))

                new_txt_list.append(new_line)

            print('V mirror annotation new_txt_list:', new_txt_list)

            # 接下来是保存改好的txt文件。
            # 保存文件
            if not os.path.exists(output_path):
                os.makedirs(output_path)

            output_label_path = output_path + 'labels/'
            # print('output_label_path:', output_label_path)
            if not os.path.exists(output_label_path):
                os.makedirs(output_label_path)
            new_label_file = txt_file[0:-4] + '_v' + '.txt'
            # print('output_label_path+new_txt_file:', output_label_path + new_label_file)

            if os.path.exists(output_label_path + new_label_file):
                raise Exception('The destination annotation file already exists')

            with open(output_label_path + new_label_file, 'w+', encoding='utf-8') as f:
                f.writelines(new_txt_list)

    print('\n', 'annotation vertical mirror has been completed')


def v_Mirror_Img(img_path, output_path):
    img_files = os.listdir(img_path)
    output_image_path = output_path + 'images/'

    if not os.path.exists(output_image_path):
        os.makedirs(output_image_path)

    for img_file in img_files:
        img = cv2.imread(img_path + img_file)
        # cv2.imshow('before', img)
        # cv2.waitKey(4000)
        # cv2.destroyAllWindows()

        mirror_img = cv2.flip(img, 0)  #

        new_img_file = img_file[0:-4] + '_v' + img_file[-4:]
        # print('img_file:',img_file)
        # print('new_img_file:',new_img_file)

        if os.path.exists(output_image_path + new_img_file):
            raise Exception('The destination image file already exists')

        cv2.imwrite(output_image_path + new_img_file, mirror_img)
        # cv2.imshow('after', mirror_img)
        # cv2.waitKey(2000)
        # cv2.destroyAllWindows()
    print('\n', 'image vertical mirror has been completed')


def a_Mirror_Anno(txt_path, output_path):
    txt_files = os.listdir(txt_path)
    for txt_file in txt_files:

        # open文件的名称改为txt_path+'文件名'形式
        with open(txt_path + txt_file) as f:
            txt_list = f.readlines()
            print('txt_list:', txt_list)
            new_txt_list = []
            for i in range(len(txt_list)):
                # print('txt_list[0]:', txt_list[i])
                # print(type(txt_list[i]))
                str_list = txt_list[i].split()
                # print('original str_list:', str_list)

                classes, x1, y1, x2, y2, x3, y3, x4, y4 = str_list

                x1 = str(1 - float(x1))
                x2 = str(1 - float(x2))
                x3 = str(1 - float(x3))
                x4 = str(1 - float(x4))
                y1 = str(1 - float(y1))
                y2 = str(1 - float(y2))
                y3 = str(1 - float(y3))
                y4 = str(1 - float(y4))

                new_str_list = [classes, x1, y1, x2, y2, x3, y3, x4, y4]
                # print('new_str_list:', new_str_list)

                new_line = ' '.join(new_str_list) + '\n'

                # print('new_line:', new_line, '\n')
                # print('type of new_line:', type(new_line))

                new_txt_list.append(new_line)

            print('H+V annotation mirror new_txt_list:', new_txt_list)

            # 接下来是保存改好的txt文件。
            # 保存文件
            if not os.path.exists(output_path):
                os.makedirs(output_path)

            output_label_path = output_path + 'labels/'
            # print('output_label_path:', output_label_path)
            if not os.path.exists(output_label_path):
                os.makedirs(output_label_path)
            new_label_file = txt_file[0:-4] + '_a' + '.txt'
            # print('output_label_path+new_txt_file:', output_label_path + new_label_file)

            if os.path.exists(output_label_path + new_label_file):
                raise Exception('The destination annotation file already exists')

            with open(output_label_path + new_label_file, 'w+', encoding='utf-8') as f:
                f.writelines(new_txt_list)

    print('\n', 'annotation horizontal vertical mirror has been completed')


def a_Mirror_Img(img_path, output_path):
    img_files = os.listdir(img_path)
    output_image_path = output_path + 'images/'

    if not os.path.exists(output_image_path):
        os.makedirs(output_image_path)

    for img_file in img_files:
        img = cv2.imread(img_path + img_file)
        # cv2.imshow('before', img)
        # cv2.waitKey(4000)
        # cv2.destroyAllWindows()

        mirror_img = cv2.flip(img, -1)  #

        new_img_file = img_file[0:-4] + '_a' + img_file[-4:]
        # print('img_file:',img_file)
        # print('new_img_file:',new_img_file)

        if os.path.exists(output_image_path + new_img_file):
            raise Exception('The destination image file already exists')

        cv2.imwrite(output_image_path + new_img_file, mirror_img)
        # cv2.imshow('after', mirror_img)
        # cv2.waitKey(2000)
        # cv2.destroyAllWindows()
    print('\n', 'image horizontal vertical mirror has been completed')


h_Mirror_Anno(txt_path=txt_path, output_path=output_path)
h_Mirror_Img(img_path=img_path, output_path=output_path)
v_Mirror_Anno(txt_path=txt_path, output_path=output_path)
v_Mirror_Img(img_path=img_path, output_path=output_path)
a_Mirror_Anno(txt_path=txt_path, output_path=output_path)
a_Mirror_Img(img_path=img_path, output_path=output_path)
