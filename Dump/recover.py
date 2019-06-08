if __name__ == '__main__':
    f = open('unko.txt', 'r')

    line = f.readline()
    barray = bytearray([])

    while line:
        line = line.strip()
        oct_list = line.split()
        for oct_bit in oct_list:
            barray.append(int(oct_bit, 8))
        line = f.readline()

    f.close()

    f = open('output', 'wb')
    f.write(barray)
    f.close()
