import os

# 文件复制 文件夹中含有文件夹
src_path = r"C:\Users\QHF\Desktop\qhf_TEST1"
target_path = r"C:\Users\QHF\Desktop\qhf_TEST2"


def copy(src_path, target_path):
    # 获取文件夹里面的内容
    filelist = os.listdir(src_path)
    # print(filelist)

    # 遍历列表
    for file in filelist:
        path = os.path.join(src_path, file)  # 拼接路径
        if os.path.isdir(path):  # 判断是否为文件夹
            target_path1 = os.path.join(target_path, file)  # 拼接目标路径
            os.mkdir(target_path1)  # 创建目标文件夹
            copy(path, target_path1)  # 拷贝

        else:
            with open(path, 'rb') as rstream:
                container = rstream.read()

                path1 = os.path.join(target_path, file)
                with open(path1, 'wb') as wstream:
                    wstream.write(container)
    else:
        print("复制完成！")



# 调用函数
copy(src_path, target_path)
