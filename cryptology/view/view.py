from model.readFile import ReadFile
from model.writeFile import WriteFile
from bitarray import bitarray
import re
import os


def str2bitarray(s):
    ret = bitarray(''.join([bin(int('1' + hex(c)[2:], 16))[3:] for c in s.encode('utf-8')]))
    return ret


def bitarray2str(bit):
    return bit.tobytes().decode('utf-8')


# m = ReadFile('static/b.docx').loadfile()
# print("原来的字符串：" + m)
# b = str2bitarray(m)
# print("原来:",b)
# # b = re.findall(r'\d+', str(b))[0]
# print(bitarray2str(b))
#
#
#
# print(str2bitarray(m))
# b = str2bitarray(m)
# print(type(b))
# length = b.length()


def encryption(original, key):
    """异或运算加密算法"""
    ciphertext = 1  # 密文
    original = re.findall(r'\d+', str(original))[0]
    for i, j in zip(str(original), str(key)):
        # print(i ,j)
        index = int(i) ^ int(j)
        if index == 0:
            ciphertext = ciphertext * 10
        else:
            ciphertext = ciphertext * 10 + 1
    ciphertext = str(ciphertext)
    ciphertext = ciphertext[1:]
    return ciphertext  # 将经过的密文返回


def deciphering(ciphertext, key):
    """对密文进行异或运算解密"""
    original = 1
    for i, j in zip(str(ciphertext), str(key)):
        # print(i, j)
        index = int(i) ^ int(j)
        if index == 0:
            original = original * 10
        else:
            original = original * 10 + 1
    original = str(original)
    # print(original)
    original = original[1:]
    return bitarray2str(bitarray(original))


# ciphertext = encryption(b, key)
# original = deciphering(ciphertext, key)
# print("密文：",ciphertext)
# print("原文：",original)

class jiamijiemi:
    def __init__(self, path):
        self._path = path
        print(os.getcwd())
        keyPath = os.path.abspath(os.path.dirname(os.getcwd()))
        with open(keyPath + r'\\view\\static\\key.txt', 'r') as fp:
            self._key = fp.read()

    def encrytext(self):
        m = ReadFile(self._path).loadfile()
        b = str2bitarray(m)
        ciphertext = encryption(b, self._key)
        with open(self._path, 'w') as fp:
            fp.write(ciphertext)

    def ciptolotext(self):
        m = ReadFile(self._path).loadfile()
        original = deciphering(m, self._key)
        with open(self._path, 'w') as fp:
            fp.write(original)

# w = WriteFile('static/cyptions/b.txt')
# w.writeFile(ciphertext)
# w.writeFile(original)
