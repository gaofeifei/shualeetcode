import os
import re
from itertools import product
from itertools import combinations
from itertools import dropwhile

def test(nums):
    nums.sort()
    nums.sorted()
    for i,v in enumerate(nums):
        print(i,v)

def slice_up(source_path,capter_name):
    sf = open(source_path, 'r', encoding='utf-8')
    # print(sf.readlines())
    sn_list = [sn.strip() for sn in sf.readlines()]
    # print(sn_list)
    last = len(sn_list)
    # print(last)
    slice_list = []
    for cn in capter_name:
        # print(cn)
        # print(sn_list.index(cn))
        slice_i = sn_list.index(cn)
        slice_list.append(slice_i)
    slice_list.append(last)
    # print(slice_list)
    return slice_list, sn_list

def split_file_into_different_files(slice_list, sn_list, cpath_list):
    # print(slice_list)
    # [0, 12, 33, 58, 80, 106, 114, 121, 153, 191]
    last = len(slice_list)
    l = []
    regex = re.compile(r'([0-9]{1,3})\t')#正则找出题目编号
    for z, j in enumerate(slice_list):
        if j == 191:
            break
        # print(sn_list[j:slice_list[z+1]])
        l1 = sn_list[j:slice_list[z + 1]]
        l.append(l1)
    for i, v in enumerate(cpath_list):
        f = open(v, 'w', encoding='utf-8')
        str = "".join(l[i])
        sl = regex.findall(str)
        for q in sl:
            str = str.replace(q+'\t','\n'+q+'\t')
        f.write(str)
        f.close()

#自动写入注释 准备好 XXXcatalogue.txt 文件内容 例如 算法的题目
def auto_write_common():
    path = r'../python100topic1.txt'
    cpath = os.getcwd()  # 当前目录
    # print(cpath)
    li = []
    num = 0
    with open(path, 'r', encoding='UTF-8') as f:
        for line in dropwhile(lambda line: line.startswith(('#', '"""', ' ', '***')), f):
            # print(line, end='')
            line = line.strip()
            # print(type(line))
            li.append(line)
            num = len(li)
        if num > 0:
            for i in li:
                # print(i)
                index = li.index(i)
                filename = str(index + 1) + ".py"
                # print(filename)
                f_new = open(cpath + "\\" + filename, 'w', encoding='utf-8')
                wline = '"""\nFQA:' + i + '\n' + '\n"""' + '\n' + "'''" + "author:feifeigao cheer!!!" + "'''" + '\n'
                # print(wline)
                f_new.writelines(wline)
            f_new.close()



if __name__ == '__main__':
    # nums=[6,-4,-1,0,1,2,1,4]
    # test(nums)
    bookname = "python_180_zuo.pdf(程序员代码面试指南整理)"
    path = r'../leetcode/python_arithmetic/'
    tpath = os.path.realpath(path)  # 绝对路径
    # print(tpath)
    lessons_list_large = []
    capter_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    capter_name = ['栈和队列', '链表问题', '二叉树问题', '递归和动态规划', '字符串问题', '大数据和空间限制', '位运算', '数组和矩阵问题', '其他题目']
    lessons_list = [11, 20, 24, 20, 25, 7, 6, 31, 37]
    cl = len(capter_list)
    # print(cl)
    cnamedir_list = []
    cpath_list = []
    capter_name1 = ['第 1 章  栈和队列', '第 2 章  链表问题', '第 3 章  二叉树问题', '第 4 章  递归和动态规划', '第 5 章  字符串问题', '第 6 章  大数据和空间限制', '第 7 章  位运算', '第 8 章  数组和矩阵问题', '第 9 章  其他题目']
    for i in range(1, cl + 1):
        cname = str(i) + capter_name[i - 1]
        # print(cname)
        cnamedir_list.append(cname)
        cpath = tpath + '\\' + cname + '\\' + cname + 'catalogue.txt'
        # print(cpath)
        cpath_list.append(cpath)
    # print(cnamedir_list)
    # print(cpath_list)
    source_path = tpath+'\\'+'python_180zuo.txt'
    # print(source_path)
    #得到切片文件下标
    slice_list, sn_list = slice_up(source_path, capter_name1)
    split_file_into_different_files(slice_list, sn_list, cpath_list)