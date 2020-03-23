# coding:utf-8


def get_url(filename):
	"""
	:param filename: jmx脚本路径及名称
	:return: url在文件中的行数及url
	"""

	file = open(filename, "r", encoding="utf-8", errors="ignore")
	"""
	open表示打开你要执行的文件用读的方式打开
	第一个参数是上面的文件path路径,第二个是所要执行的操作，（r）代表读，
	#encoding="utf-8表示指定编码为“utf-8”，errors="ignore"表示读的时候遇到错误忽略
	"""
	i = 1
	urlList = []
	while True:
		mystr = file.readline()  # 表示一次读取一行
		if not mystr:
			# 读到数据最后跳出，结束循环。数据的最后也就是读不到数据了，mystr为空的时候
			break
		if mystr.count("HTTPSampler.path") > 0:
			uLi = mystr.split('>')
			if uLi[1]:
				url = uLi[1].split('<')
				if len(url[0]) > 0:
					urlList.append((i, url[0]))
		i += 1
	return urlList



def export_jmx_url(path, targetFile):
	"""
	:param path: 脚本存放路径
	:param targetFile: 导出的文件名称
	:return:
	"""
	import os

	files = os.listdir(path)

	if os.path.exists(targetFile):
		os.remove(targetFile)

	file_test = open(targetFile, "a+")
	file_test.write('文件名\t位置\turl\n')
	for f in files:
		if f[-3:] == 'jmx':
			urlList = get_url(path + '/' + f)
			print(f'开始导出{f},一共{len(urlList)}个url')
			for u in urlList:
				file_test.write(f'{f}\t{u[0]}\t{u[1]}\n')
			print(f'{f}导出完成')
	file_test.close()

path_wj = r"\\10.0.1.xx\CeshiBu\数据平台接口\接口测试脚本\jmeter3.1脚本\name1"          #脚本存放路径
targetFile_wj = r"\\10.0.1.xx\CeshiBu\数据平台接口\接口测试脚本\name1url.xls"       # 导出的文件名称

path_zjx = r"\\10.0.1.xx\CeshiBu\数据平台接口\接口测试脚本\jmeter3.1脚本\name2"          #脚本存放路径
targetFile_zjx = r"\\10.0.1.xx\CeshiBu\数据平台接口\接口测试脚本\name2url.xls"       # 导出的文件名称

path_whw = r"\\10.0.1.xx\CeshiBu\数据平台接口\接口测试脚本\jmeter3.1脚本\whw"          #脚本存放路径
targetFile_whw = r"\\10.0.1.xx\CeshiBu\数据平台接口\接口测试脚本\whwurl.xls"       # 导出的文件名称

path_cj = r"\\10.0.1.xx\CeshiBu\数据平台接口\接口测试脚本\jmeter3.1脚本\cj"          #脚本存放路径
targetFile_cj = r"\\10.0.1.xx\CeshiBu\数据平台接口\接口测试脚本\cjurl.xls"       # 导出的文件名称

path_mjs = r"\\10.0.1.xx\CeshiBu\数据平台接口\接口测试脚本\jmeter3.1脚本\mjs"          #脚本存放路径
targetFile_mjs = r"\\10.0.1.xx\CeshiBu\数据平台接口\接口测试脚本\mjsurl.xls"       # 导出的文件名称

path_zsb = r"\\10.0.1.xx\CeshiBu\数据平台接口\接口测试脚本\jmeter3.1脚本\sb"          #脚本存放路径
targetFile_zsb = r"\\10.0.1.xx\CeshiBu\数据平台接口\接口测试脚本\sburl.xls"       # 导出的文件名称

path_ljj = r"\\10.0.1.xx\CeshiBu\数据平台接口\接口测试脚本\jmeter3.1脚本\ljj"          #脚本存放路径
targetFile_ljj = r"\\10.0.1.xx\CeshiBu\数据平台接口\接口测试脚本\ljjurl.xls"       # 导出的文件名称

path_file = {path_wj: targetFile_wj,
             path_cj: targetFile_cj,
             path_whw: targetFile_whw,
             path_zjx: targetFile_zjx,
             path_mjs: targetFile_mjs,
             path_zsb: targetFile_zsb,
             path_ljj: targetFile_ljj}

for k,v in path_file.items():
	export_jmx_url(k, v)
