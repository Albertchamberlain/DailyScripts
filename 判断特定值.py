f = open('x.txt', 'rb')

data = int(f.read(1).encode('hex'), 16)
print (data)
print (bin(data))


mask = 0b11110000
print (mask)


res = data & mask
print (res)



#首先是打开文件，用read()函数读进去一个字节，用16进制进行编码.
# 编码之后会变成一个str类型，这时对它进行转换，int()函数可以将一个str转换成int类型.
# int()函数的第二个参数代表了进制。
# mask为11110000，我用mask和要处理的字节进行与，可以得到数据前四位的内容