#Melody Fang
#mkfang@uci.edu
#37001380
import sys
import os
import decrypt
import checkenglish
from multiprocessing import Process

class FailedException(Exception):
    pass


def main(ogfile, newfile, keyfile):
    with open(ogfile, "rb") as ofile:
        ofile.seek(0, 2)
        amt_keys = ofile.tell()
    if os.path.isfile(ogfile):
        try:
            h_percent = 0
            h_key = 0
            for key in range(1, amt_keys + 1):   
                d = decrypt.decrypt(ogfile, int(key))
                t = decrypt.transposematrix(d, int(key))
                decrypt.concatenatematrix(t, newfile)

                num = checkenglish.findpercentage(newfile)
                if num > h_percent:
                    h_percent = num
                    h_key = key
                    with open(keyfile, "w") as kk:
                        kk.write(str(key))
                    completed = True

            if h_key != 0:
                d = decrypt.decrypt(ogfile, int(h_key))
                t = decrypt.transposematrix(d, int(h_key))
                decrypt.concatenatematrix(t, newfile)
                print(f"done. check {newfile} for results, and {keyfile} for the key.")
            else:
                raise FailedException()
        except FailedException as e:
            print("the decryption failed.")
        except FileNotFoundError as e:
            print(f"error: {e}. we couldn't find the file.")
        except PermissionError as e:
            print(f"error: {e}. make sure you have access to this file.")
        except IOError as e:
            print(f"error: {e}")

if __name__ == '__main__':
    ogfile = sys.argv[1]
    newfile = sys.argv[2]
    keyfile = sys.argv[3]

    p = Process(target = main, args = (ogfile, newfile, keyfile))
    p.start()
    p.join()