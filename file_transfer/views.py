# coding: utf-8

from django.http import HttpResponse, HttpResponseNotFound
import os

def saveData(req):
	if req.method == 'POST':
		dirname = req.POST.get('dirname', None)
		filename = req.POST.get('filename', None)
		data = req.POST.get('data', None)
		if dirname == None or filename == None or data == None:
			return HttpResponse('false')
		else:
			saveFile(dirname, filename, data)
			return HttpResponse('true')

	return HttpResponseNotFound('<h1>Page not found</h1>')

def saveFile(dirname, filename, data):
	d = os.path.join('G:\\IoT\\SyncFolder\\Identification\\data\\tizen', dirname)
	if os.path.exists(d) == False:
		os.mkdir(d)

	# 寻找一个不重复的文件名
	(name, ext) = os.path.splitext(filename)
	count = 0 # 文件名后加上数字，数字从 count 开始
	path = os.path.join(d, name + str(count) + ext)
	while os.path.exists(path):
		count = count + 1
		path = os.path.join(d, name + str(count) + ext)

	open(path, 'w').write(data)
