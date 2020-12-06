# ！user/bin/env python
# -*- UTF-8 -*-
"""
Author: zxp
Time: 2020年11月27日
"""



if __name__ == '__main__':

 fi=open(r"C:\Users\zxp\Desktop\三轮\rotation\rotation\fasta.txt","r+")
 seq = fi.read()
 fi.close()
 k=input('请输入K-mer的值：'+'\n')
 interval=[]
 while True:
    if k.isdigit() == False:
        k = input('K-mer值不合理，请重新输入：' + '')
    else:
        k= int(k)
        if k in range(2,len(seq)):
            break
        else:
            k=input('K-mer值不合理，请重新输入：'+'')
 count=0
 k_mer=[]
 f_kmer=open(r"C:\Users\zxp\Desktop\kmer.txt","a")
 for n in range(0,len(seq)-k+1):
     k_mer.append(seq[n:n+k])
     count+=1
     f_kmer.write(seq[n:n+k]+'  ')
 f_kmer.close()

 f_stat = open(r"C:\Users\zxp\Desktop\stat.txt", "r+")
 library={}
 for x in k_mer:
    library[x] =library.get(x,0) + 1
 print('基因组长度：' + str(len(seq)) + '\n'
        'k-mer的数量：' + str(count) + '')

 percent = {}
 num = len(k_mer)
 for y in library.keys():
    percent[y]='%.2f%%' % (library.get(y,0)/num*100)

 f_stat.write("组成及比例："+'\n')
 print("组成及比例："+'\n')
 for key in percent.keys():
    f_stat.write(str(key)+'：'+str(library[key])+','+str(percent[key]))
    print(key+'：'+str(library[key])+','+str(percent[key])+'')
 f_stat.close()