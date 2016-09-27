# -*- coding:utf-8 -*- 
fie=open("addr","r")
fout=open("addr2","a")
line=fie.readline()
while line:
	line=line.replace("\r\n","")
	fout.write(line+",")
        line = fie.readline()
fie.close()
fout.close()
