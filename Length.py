from fasta import sequence

 def length(str):
    counter = 0
    while str[counter:]:
        counter += 1
    print(counter)
    return

if __name__ == '__main__':
length(sequence)



