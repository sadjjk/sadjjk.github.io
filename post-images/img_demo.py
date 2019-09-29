from random import choice
import tinify
import os

keys  = ['yKMpRXCWQrwssnkXv5HFrbRy1W5V2Q3N',
		'B9ywkSLNSjx9xmGgq1zPQYn3d90F6myN']

tinify.key = choice(keys)

imgpath = "/Users/sadjjk/Desktop/5d3d4aa51d0dc93847.png" # 图片存放的路径



print("图片压缩前大小: %.3f KB" % (os.path.getsize(imgpath) / 1024))
print("开始压缩 ...")
tinify.from_file(imgpath).resize(method = 'scale',width=800).to_file(imgpath)
# tinify.from_file(imgpath).to_file(imgpath)
print("... 压缩完成" )
print("图片压缩后大小: %.3f KB" % (os.path.getsize(imgpath) / 1024))


compressions_this_month = tinify.compression_count
print("当月已压缩%d次,剩余%d次" % (compressions_this_month,500-compressions_this_month))