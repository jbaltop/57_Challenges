#!/usr/local/bin/python3

# 웹사이트 생성자

# 입력: 사이트 이름, 사이트 필자, 자바스크립트 파일을 위한 폴더를 만들 것인지, CSS 파일을 위한 폴더를 만들 것인지
# 프로세스: index.html 파일 생성, 자바스크립트 폴더(옵션), CSS 폴더(옵션)
# 출력: index.html, 자바스크립트 폴더, CSS 폴더를 만들었다는 메시지

import os

messages = {
	"site": "Site name: ",
	"author": "Author: ",
	"js": "Do you want a folder for JavaScript(Y/n)? ",
	"css": "Do you want a folder for CSS(Y/n)? ",
	"m1": "Created ./{}/",
	"m2": "Created ./{}/js/",
	"m3": "Created ./{}/css/",
	"m4": "Created ./{}/index.html",
	}

site = input(messages["site"])
author = input(messages["author"])
js = input(messages["js"])
css = input(messages["css"])

os.mkdir('./{}'.format(site))
print(messages["m1"].format(site))

if js.lower() != 'n':
	os.mkdir('./{}/js'.format(site))
	print(messages["m2"].format(site))

if css.lower() != 'n':
	os.mkdir('./{}/css'.format(site))
	print(messages["m3"].format(site))

content = '<!doctype html>\n<html>\n\t<head>\n\t\t<meta name="author" content="' + author + '">\n\t\t<title>"' + site + '"</title>\n\t</head>\n</html>'

fout = open('{}/index.html'.format(site), 'wt')
fout.write(content)
fout.close()
print(messages["m4"].format(site))
