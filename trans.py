import os

from PIL import Image
import argparse

#命令行输入参数处理
parser = argparse.ArgumentParser()
parser.add_argument('file')     #输入文件
# parser.add_argument('--width', type = int, default = 80) #输出字符画宽
# parser.add_argument('--height', type = int, default = 60) #输出字符画高
#获取参数
args = parser.parse_args()

IMG = args.file
# WIDTH = args.width
# HEIGHT = args.height

charList = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(charList)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return charList[int(gray/unit)]

if __name__ == '__main__':
	pic = Image.open(IMG)
	pic = pic.resize((60,60),Image.NEAREST)
	high,width = pic.size

	txt = ""

	for i in range(high):
		for j in range(width):
			txt += get_char(*pic.getpixel((j,i)))
		txt += '\n'

	print(txt)

	fo = open("img.txt","w")
	fo.write(txt)
	fo.close()

os.system("pause")



