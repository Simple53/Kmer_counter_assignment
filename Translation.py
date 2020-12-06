# ！user/bin/env python
# -*- UTF-8 -*-
"""
Author: zxp
Time: 2020年11月26日
"""
if __name__ == '__main__':
    fasta_file=open(r"C:\Users\zxp\Desktop\fa.txt","r+")
    mRNA_file=open(r"C:\Users\zxp\Desktop\mRNA.txt","r+")
    seq=fasta_file.read()
    mRNA= seq.replace('A', 'u').replace('T', 'a').replace('G', 'c').replace('C', 'g').upper()[::-1]
    mRNA_file.write(mRNA)
    fasta_file.close()

    RNA_codon = {
        'UUU' : 'F', 'CUU' : 'L', 'AUU' : 'I', 'GUU' : 'V',
        'UUC' : 'F', 'CUC' : 'L', 'AUC' : 'I', 'GUC' : 'V',
        'UUA' : 'L', 'CUA' : 'L', 'AUA' : 'I', 'GUA' : 'V',
        'UUG' : 'L', 'CUG' : 'L', 'AUG' : 'M', 'GUG' : 'V',
        'UCU' : 'S', 'CCU' : 'P', 'ACU' : 'T', 'GCU' : 'A',
        'UCC' : 'S', 'CCC' : 'P', 'ACC' : 'T', 'GCC' : 'A',
        'UCA' : 'S', 'CCA' : 'P', 'ACA' : 'T', 'GCA' : 'A',
        'UCG' : 'S', 'CCG' : 'P', 'ACG' : 'T', 'GCG' : 'A',
        'UAU' : 'Y', 'CAU' : 'H', 'AAU' : 'N', 'GAU' : 'D',
        'UAC' : 'Y', 'CAC' : 'H', 'AAC' : 'N', 'GAC' : 'D',
        'CAA' : 'Q', 'AAA' : 'K', 'GAA' : 'E', 'CAG' : 'Q',
        'AAG' : 'K', 'GAG' : 'E', 'UGU' : 'C', 'CGU' : 'R',
        'AGU' : 'S', 'GGU' : 'G', 'UGC' : 'C', 'CGC' : 'R',
        'AGC' : 'S', 'GGC' : 'G', 'CGA' : 'R', 'AGA' : 'R',
        'GGA' : 'G', 'UGG' : 'W', 'CGG' : 'R', 'AGG' : 'R',
        'GGG' : 'G',
        'UAG' : 'STOP' , 'UGA' : 'STOP' , 'UAA' : 'STOP',
    }

    Protein_file=open(r"C:\Users\zxp\Desktop\pro.txt","r+")
    x=0
    count=0
    code=''
    while x < len(mRNA)-2:
        for x in range(0, len(mRNA)-1, 1):
            peptide=''
            code = mRNA[x:x + 3]
            if code == 'AUG':
                count += 1
                for x in range(x, len(mRNA), 3):
                    code = mRNA[x:x + 3]
                    if code in RNA_codon:
                        x += 1
                        if RNA_codon[code] == 'STOP':
                            break
                        else:
                            peptide += RNA_codon[code]
                print('>No.'+str(count)+ '\n'+peptide + '\n')
                Protein_file.write('>No.' + str(count) + '\n' + peptide + '\n')
            else:
                continue
            x += 1

   Protein_file.close()


