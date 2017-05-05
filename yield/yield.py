#codeing=utf-8
import time
import sys

# producer
def produce(box):
	i=0
	print "produce ... begin"
	while 1:
		print "while", i
		if i<5:
			print "yield", i
			yield i
			box.append(i)
			i=i+1
			time.sleep(1)
		else:
			return

# consumer
def consume(box):
	# p is returned as the generator when encoutered the "yield i"
	p = produce(box)
	print "generator is returned", len(box)
	while 1:
		try:
			
			next = p.next()
			print "next() is called=>", next
			#while len(box) > 0:
				#print box.pop()
			#print box
		except StopIteration:
			print box
			sys.exit(0)

box = []
consume(box)



