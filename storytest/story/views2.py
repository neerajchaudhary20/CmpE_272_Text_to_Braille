from django.shortcuts import render_to_response
from django.http import HttpResponse
from newspaper import Article
import MySQLdb
import re


url = u'http://timesofindia.indiatimes.com/world/us'
db = MySQLdb.connect("localhost","root","fallcon2015","python123")
cursor = db.cursor()
article = Article(url)
article.download()
article.html
article.parse()
x = article.authors
print x
print 'hi'
#print article.summary
#y = "<center><h2>Top News</h2></center><table border=1>"
#start1 = "<tr><td>"
#start2 = "</td><td>"
#i = 1
#end = "</td></tr>"
#z = " "
#for x in article.text.encode("utf-8").split("|"):
#		if (x != " "):
#			start = start1 + str(i)+ start2
#			z +=  start + x  + end  
#			i = i + 1
#abc = y + z
#print (abc)
for x in article.text.encode("utf-8").split("|"):
#	try:
		y = x
		cursor.execute("insert into news(news_data) values (%s)",[y])
		print ("Hi---",y)
		db.commit()


print ("======================")
no = 21
cursor.execute("select news_data from news where news_id =(%s)", [no])
rows = cursor.fetchall()
rowss = re.sub(r'\W+', ' ', str(rows))
print rowss

rowss_value = "Test braille values"

def home(request):
#	return HttpResponse("Hello world!")
# Create your views here.
	#for x in article.text.encode("utf-8").split("|"):
	#	z +=  start + x  + end  
	#	print (y) 
	#print ("Hey ya'all ")
	#x = "<table> <tr><td>1</td><td>thisi is one</td></tr><tr><td>2</td><td>this is two</td></tr>"
	#abc = y + z
	return HttpResponse(abc)
def home(request):
	return render_to_response("story/home.html", {'hello': rowss, 'bye' : rowss_value})
