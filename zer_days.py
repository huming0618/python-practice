# coding=utf-8
import sys
import platform
#print sys.getdefaultencoding()
from datetime import datetime

def zer_days():
	birthday = datetime.strptime('2016-01-05', '%Y-%m-%d')
	return abs((datetime.now()-birthday).days)

if __name__ == "__main__":
	days = zer_days()
	os_name = platform.platform()
	if "Darwin" in os_name:
		print ('正儿%d天了, 恭喜恭喜!'%days)
	else:
		print ('正儿%d天了, 恭喜恭喜!'%days).decode('utf8').encode('gb2312')
