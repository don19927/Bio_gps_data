import pymysql
import csv

conn = pymysql.connect(user='root',passwd="",db='bio_gps')


cur = conn.cursor()

cur.execute("""CREATE TABLE Human_GNF1H_Annotation (ProbesetID varchar(255), Num_matched_probes int,
RefSeq varchar(255), UniGene varchar(255), RIKEN varchar(255),	EntrezGene int,	Symbol varchar(255),
Description	varchar(2500))""")



#this is the insert table statement if it doesn't run at once create the table first then run the insert statement separate but #include import pymysql to cur = 

file = csv.reader(open('/Users/Donnie/Desktop/gnf1h.annot2007.csv', 'rU'))

csv.field_size_limit(1000000)

for ProbesetID, Num_matched_probes, RefSeq, UniGene, RIKEN, EntrezGene, Symbol, Description in file:
	
	cur.execute("""INSERT INTO Human_GNF1H_Annotation  (ProbesetID, Num_matched_probes, RefSeq, 
					UniGene, RIKEN, EntrezGene, Symbol, Description) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",
					(ProbesetID, Num_matched_probes, RefSeq, UniGene, RIKEN, EntrezGene, Symbol, Description))
	
