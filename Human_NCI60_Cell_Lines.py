import pymysql
import csv

conn = pymysql.connect(user='root',passwd="",db='bio_gps')


cur = conn.cursor()


insert_statement = open('/Users/Donnie/Desktop/NYU Research/Human data table/gnf1h.annot2007.csv', 'rb')

x = 1

while x < 22259:
	fob = insert_statement.readline(x)
	cur.execute("INSERT INTO Human_GNF1H_Annotation VALUE(%s)",(fob))
	x += 1
	

	 
