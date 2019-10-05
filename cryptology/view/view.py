from model.readFile import ReadFile
from bitarray import bitarray
import re


def str2bitarray(s):
    ret = bitarray(''.join([bin(int('1' + hex(c)[2:], 16))[3:] for c in s.encode('utf-8')]))
    return ret


def bitarray2str(bit):
    return bit.tobytes().decode('utf-8')


m = ReadFile('static/a.txt').loadfile()
print("原来的字符串：" + m)
b = str2bitarray(m)
print("原来:",b)
# b = re.findall(r'\d+', str(b))[0]
print(bitarray2str(b))

def str_to_hex(s):
    return ' '.join([hex(ord(c)).replace('0x', '') for c in s])


def hex_to_str(s):
    return ''.join([chr(i) for i in [int(b, 16) for b in s.split(' ')]])


def str_to_bin(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])


def bin_to_str(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])


print(str2bitarray(m))
b = str2bitarray(m)
print(type(b))
length = b.length()

key = 1
for i in range(length - 1):
    if i % 2 == 0:
        key = key * 10
    else:
        key = key * 10 + 1


def encryption(original, key):
    """异或运算加密算法"""
    ciphertext = 1  # 密文
    original = re.findall(r'\d+', str(original))[0]
    for i, j in zip(str(original), str(key)):
        print(i ,j)
        index = int(i) ^ int(j)
        if index == 0:
            ciphertext = ciphertext * 10
        else:
            ciphertext = ciphertext * 10 + 1
    ciphertext = ciphertext % (10 ** (ciphertext.bit_length() - 1))
    return str(ciphertext)  # 将经过的密文返回


def deciphering(ciphertext, key):
    """对密文进行异或运算解密"""
    original = 1
    for i, j in zip(str(ciphertext), str(key)):
        index = int(i) ^ int(j)
        if index == 0:
            original = original * 10
        else:
            original = original * 10 + 1
    original = original % (10 ** (len(ciphertext) - 1))
    original = str(original)
    print(original)
    return bitarray(original)


ciphertext = encryption(b, key)
original = deciphering(ciphertext, key)
print("密文：",ciphertext)
print("原文：",original)
