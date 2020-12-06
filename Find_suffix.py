
import os

def judge(file_dir):
    "判断输入的路径是否正确"
    file_dir = input("请输入需要查找的路径：\n")
    while True:
        if os.path.exists(file_dir) == False:
            file_dir=input("路径不存在，请重新输入：\n")
        else:
            print("路径输入正确")
            break
    return file_dir

def suffix_list(path):
    # 提取文件夹内所有文件的后缀
    suffix_list=[]
    files = os.listdir(path)
    for file in files:
        if not os.path.splitext(file)[1] in suffix_list:
            suffix_list.append(os.path.splitext(file)[1])
        while '' in suffix_list:
            suffix_list.remove('')
    print("当前路径中的文件后缀有：",'')
    for item in suffix_list:
        print(item,end=" ")
    return suffix_list

def suffix(str,list):
    #判断后缀是否存在
    str = input("请输入需要查找的后缀：\n")
    while True:
        if not str in list:
            str = input("后缀不存在，请重新输入：\n")
        else:
            print("后缀输入正确。")
            break
    return str


def find(path,suffix):
    file_list = []
    for root,dirs,files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[1] == suffix:
               file_list.append(os.path.join(root,file))
    print("查找结束。")
    print(file_list)
    return file_list


if __name__ == '__main__':
    file_dir=''
    path=judge(file_dir)
    suffix_list=suffix_list(path)
    suffix=suffix(str,suffix_list)
    file_list=find(path,suffix)