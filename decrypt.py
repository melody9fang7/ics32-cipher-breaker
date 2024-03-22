#Melody Fang
#mkfang@uci.edu
#37001380

import math

def writetomatrix(file1, key):
    mtrx = []

    with open(file1, "rb") as ofile:
        ofile.seek(0, 2)
        filesize = ofile.tell()

        if filesize == 0:
            print("file is empty. try again.")
        elif filesize < key:
            print("key cannot be larger than filesize. try again.")
        else:
            amt_rows = math.ceil(filesize / key)

            ofile.seek(0)
            count = 0
            row = 0
            while row < amt_rows:
                mtrx.append([])
                while count < key:
                    char = ofile.read(1)
                    if char != b'\r' and char != b'\n':
                        mtrx[row].append(char)
                    count += 1
                row += 1
                count = 0

    return mtrx


def transposematrix(matrx, key):
    newmtrx = []

    for k in range(0, len(matrx[0])):
        newmtrx.append([])

    for r in matrx:
        for c in range(0, len(r)):
            newmtrx[c].append(r[c])

    return newmtrx


def concatenatematrix(matrx, newfile):
    with open(newfile, "wb") as nfile:
        for row in matrx:
            for col in row:
                nfile.write(col)


def decrypt(file1, key):
    mtrx = []

    for x in range(0, key):
        mtrx.append([])

    with open(file1, "rb") as ofile:
        ofile.seek(0, 2)
        filesize = ofile.tell()

        needed_cols = math.ceil(filesize / key)
        remainder = needed_cols * key - filesize

        ofile.seek(0)

        col = 0
        row = 0
        for x in range(0, filesize):
            if row < key:
                char = ofile.read(1)
                mtrx[row].append(char)
                col += 1

                if (col == needed_cols) or ((col == needed_cols - 1) and (row >= key - remainder)):
                    col = 0
                    row += 1

    return mtrx
