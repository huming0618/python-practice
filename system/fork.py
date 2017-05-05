#coding=utf8

import os
from time import sleep

count = 10

try:
	pid = os.fork()
	if pid == 0: #child process , pid is 0
		print "this is child"
		count = count - 1
		sleep(3)
	else: #parent process
		print "this is parent"
		sleep(10)

	#print "the count", count, ' from ', "child" if pid == 0 else "parent"
	#print "the count", count, ' from ', "child" , pid==0 and "child" or "parent"
	print "the count", count, ' from ', "child" , (pid==0 and ["child"] or ["parent"])[0]
except OSError, e:
	pass

