# coding=utf-8
import sys
#print sys.getdefaultencoding()
from datetime import datetime

def zer_days():
	birthday = datetime.strptime('2016-01-05', '%Y-%m-%d')
	return abs((datetime.now()-birthday).days)

if __name__ == "__main__":
	days = zer_days()
	print ('正儿%d天了, 恭喜恭喜!'%days).decode('utf8').encode('gb2312')
