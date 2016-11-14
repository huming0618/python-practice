#coding=utf-8
import os
import sys
import urllib
import json
import pprint
import time

# reload( sys )
# sys.setdefaultencoding('utf-8')

def query(title):
    url = 'https://api.douban.com/v2/book/search?q='+ urllib.quote(title) + '&count=1'

    print url

    response = urllib.urlopen(url)
    result = response.read() #.decode('utf-8')
    result_json = json.loads(result)
    pprint.pprint(result_json)
    if len(result_json['books']) == 0:
        return "".join([
                        '<tr>'
                            ,'<td>%s</td>' % title
                            ,'<td style="background:red;color:white" colspan=8>没有找到匹配信息</td>'
                        ,'</tr>'
                      ])
    book = result_json['books'][0]
    author = ",".join(book['author']) #[0] if len(book['author']) else ''
    isbn_1 = book['isbn10']
    isbn_2 = book['isbn13']
    link = book['alt']
    price = book['price']
    publisher = book['publisher']
    pubdate = book['pubdate']
    large_img = book['images']['large']
    print 'to join info'
    result = "".join([
                    '<tr>'
                        ,'<td>%s</td>' % title
                        ,'<td>%s</td>' % isbn_1.encode('utf-8')
                        ,'<td>%s</td>' % isbn_2.encode('utf-8')
                        ,'<td>%s</td>' % author.encode('utf-8')
                        ,'<td>%s</td>' % publisher.encode('utf-8')
                        ,'<td>%s</td>' % pubdate.encode('utf-8')
                        ,'<td>%s</td>' % price.encode('utf-8')
                        ,'<td><a href="%s" target="about:blank">豆瓣链接</a></td>' % link.encode('utf-8')
                        ,'<td><img src="%s"/></td>' % large_img.encode('utf-8')
                    ,'</tr>'
                  ])
    print result
    return result
    # with open('tushu_test.txt', 'w') as test:
    #     test.write(result_json['books'][0]['author'][0].encode('utf8'))

def listing():
    list = [];
    with open('tushu_list_1.txt') as list_file:
        for line in list_file.readlines():
            list.append(line.strip())

    html = ['<!DOCTYPE html><head><meta http-equiv="content-Type" content="text/html; charset=utf-8"></head><body><table border=1 cellspacing=3 ><tr><th>名称</th><th>ISBN #1</th><th>ISBN #2</th><th>作者</th><th>出版社</th><th>出版日期</th><th>价格</th><th>链接</th><th>图片</th>']
    for title in list:
        #None
        #html.append(query(item.decode('utf-8')))
        #title = item.decode('utf-8')
        try:
            #print 'processing ' + title.decode('utf-8')
            html.append(query(title))
        except Exception as e:
            print e
        finally:
            time.sleep(15)

    html.append('</table></body></html>')
    buffer = "".join(html)
    print buffer
    with open('tushu_report.html', 'w') as test:
        test.write(buffer)
    print 'Done!'

if __name__ == "__main__":
    listing()
