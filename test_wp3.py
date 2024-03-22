#Melody Fang
#mkfang@uci.edu
#37001380
import wp3
import random
import decrypt

normal_text = "test_wp3_autocase.txt"
key = random.randrange(1, 20)

encrypted_text = "e.txt"
m = decrypt.writetomatrix(normal_text, int(key))
n = decrypt.transposematrix(m, int(key))
decrypt.concatenatematrix(n, encrypted_text)

key_text = "k.txt"
decrypted_text = "d.txt"
wp3.main(encrypted_text, decrypted_text, key_text)


with open(key_text) as k:
    key1 = k.readline()

    if int(key1) == key:
        print(f"test passed! the keys are the same: {key}")
    else:
        print(f"test failed. the original key is: {key}. the generated one is {key1}")