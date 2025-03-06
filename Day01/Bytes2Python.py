if __name__ == '__main__':
    print("Hello World!")

pink_bgr = (hex(48), hex(140), hex(201))
print(pink_bgr)
print(int(pink_bgr[0], 16), int(pink_bgr[1], 16), int(pink_bgr[2], 16))

color_pink0 =int(pink_bgr[0], 16).to_bytes(4, byteorder='big')
color_pink1 =int(pink_bgr[1], 16).to_bytes(4, byteorder='big')
color_pink2 =int(pink_bgr[2], 16).to_bytes(4, byteorder='big')
print(color_pink0, color_pink1, color_pink2)


"""
little与big的区别：

在计算机中，数据是以二进制的形式存储的，但由于不同计算机的存储方式不同，所以数据的字节序也不同。
大端法（big-endian）：最高位字节排放在内存的低地址处，最低位字节排放在内存的高地址处。
小端法（little-endian）：最高位字节排放在内存的高地址处，最低位字节排放在内存的低地址处。
实际的表述在于little的二进制顺序和big的二进制顺序相反。

举例：

little:00000000 00100100 00111001 00110001
   big:00110001 00111001 00100100 00000000
   
所以，在python中，int.to_bytes()方法默认采用小端法，而int.from_bytes()方法默认采用大端法。
另外，每一个0是一个bit(位)，每8个bit(位)组成一个字节(byte)。每4个字节(byte)组成一个字(二进制字符)。每个二进制字符的顺序跟字节序有关。
"""
data = bytes([0, 48, 140, 201])
para1 = int.from_bytes(data, byteorder="little")
print(para1)
para2 =int.from_bytes(data, byteorder="big")
print(para2)
little_endian = format(para1, "032b")
big_endian = format(para2, "032b")
print(little_endian)
print(big_endian)
print(little_endian == big_endian[::-1])



"""
signed与unsigned的区别：
在计算机中，有符号数和无符号数的区别在于，有符号数的最高位用来表示符号位，0表示正数，1表示负数。无符号数的最高位表示符号位，0表示正数，1表示负数。

举例：

unsigned:00000000 00100100 00111001 00110001
signed:10101010 00100100 00111001 00110001  

所以，在python中，int.to_bytes()方法默认采用unsigned，而int.from_bytes()方法默认采用signed。
"""
data = bytes([0b10101010])
signed_data = int.from_bytes(data, signed=True)
unsigned_data = int.from_bytes(data, signed=False)
print(signed_data)
print(unsigned_data)


"""
字符串与字节数组的转换：
使用 Python 的chr()函数，你可以将它们 .join（） 放入字符串 .请记住，此方法仅适用于 ASCII 范围内的字节值。
要破译可能使用多个字节编码的外来 Unicode 字符，您必须指定相应的字符编码
"""
byte_data = [0x52, 0x65, 0x61, 0x6c, 0x20, 0x50, 0x79, 0x74, 0x68, 0x6f, 0x6e]
string_data = "".join(map(chr, byte_data))
print(string_data)


"""
字节数组与字符串的转换：
重音字母 é 在 UTF-8 编码中表示时使用两个字节。因此，将十六进制值列表包装在一个对象中，并使用适当的编码调用其方法。
否则，当您尝试像以前一样单独解释每个字节时，最终会得到 乱码 文本 。bytes().decode()'cafÃ©'
"""
code_data = [0x63, 0x61, 0x66, 0xc3, 0xa9]
stringUtf8_data = bytes(code_data).decode("utf-8")
strintDefault_data = "".join(map(chr, code_data))
print(stringUtf8_data)
print(strintDefault_data)





"""
缓冲区协议：

类字节对象符合buffer协议，它描述了对象直接访问其内部数据缓冲区的标准接口。
这种机制消除了在对大量数据进行切片或传递大量数据时进行昂贵复制的需要，从而提高了性能和内存使用。
Python 中内置的几个 bytes-like objects ，这些对象对于在低级别处理二进制数据非常有用。
然而，底层缓冲区协议的真正强大之处在于：它可以促进第三方库之间的高效互作性
由于 Python 解释器将它们加载到同一个系统进程中，因此它们共享一个公共地址空间。NumPy 通过缓冲区协议向 Python 公开一个类似数组的内存区域。
这允许 Pillow 读取和作由 NumPy 管理的数据，而无需不必要的复制
0
总得来说，公开库的存在让 Python 成为一种高效的语言，可以轻松处理大量数据，并与其他库进行互操作。

互作性：它受到流行的 Python 库的广泛支持，尤其是科学生态系统中的库，确保它们的无缝集成。
效率：它允许直接访问原始内存，而不会产生复制或类型转换的开销。
安全：它依赖于 Python 的自动内存管理，从而降低了内存泄漏和分段错误的风险。
方便：它通过为您处理步幅和偏移量来支持复杂的内存布局。

"""


from array import array
from PIL import Image


#原始字节数组array进行的数据处理，属于低级处理


pixels = array("I", bytes([
     0x30, 0x8c, 0xc9, 0xff,
     0xfc, 0xba, 0x03, 0xff,
     0x25, 0xba, 0x34, 0xff,
     0x25, 0xba, 0x34, 0xff,
     0xfc, 0xba, 0x03, 0xff,
     0xfc, 0xba, 0x03, 0xff,
     0xfc, 0xba, 0x03, 0xff,
     0xfc, 0xba, 0x03, 0xff,
     0xfc, 0xba, 0x03, 0xff,
     0xfc, 0xba, 0x03, 0xff,
     0xfc, 0xba, 0x03, 0xff,
 ]))

image = Image.new(mode="RGBA", size=(4, 5))
image.putdata(pixels)
image.save("image1.png")


import numpy as np

#外部导入的 NumPy 库进行数据处理，属于高级处理
pixels = np.random.default_rng().random((1080, 1920, 3)) * 255
print(pixels)
image = Image.fromarray(pixels.astype("uint8"))
image.save("image.png")


""""
在python3.12版本以上，可以通过memoryview()函数来查看字节数组的内存视图。
memoryview()函数返回一个内存视图对象，它允许你访问字节数组的内存，而无需复制。

可以通过__buffer__()方法来获取底层缓冲区对象，并通过__bytes__()方法来获取字节数组。
也可以通过.__release_buffer__()方法来释放底层缓冲区对象。

__buffer__()方法在memoryview()中被调用，而我们无法显示调用它。
__release_buffer__()方法只有在memoryview()对象被del的时候才会被调用。同样也无法显示的调用

"""
text_bytes = bytes([0x63, 0x61, 0x66, 0xc3, 0xa9])
text_string = text_bytes.decode("utf-8")
print(text_string)
bool_buffer = memoryview(text_bytes)
print(bool_buffer)
print(bool_buffer[:])
print(bool_buffer[0])
print(bool_buffer[1:3])









