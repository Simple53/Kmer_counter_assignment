

def complement(file):
    fi = open('./test.txt','r')
    fw = open('./out.txt', 'w')
    line = fi.read()
    transline = line.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g').upper()[::-1]
    fw.write(transline)
    fi.close()
    fw.close()
    return fw

if __name__ == '__main__':
complement(file)



