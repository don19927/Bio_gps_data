import pymysql
import csv

conn = pymysql.connect(user='root',passwd="",db='bio_gps')


cur = conn.cursor()


insert_statement = csv.reader(open('/Users/Donnie/Desktop/gnf1h.annot2007.csv', 'rU'))

csv.field_size_limit(1000000)

for ProbesetID, Num_matched_probes, RefSeq, UniGene, RIKEN, EntrezGene, Symbol, Description in insert_statement:
	
	cur.execute("""INSERT INTO Human_GNF1H_Annotation  (ProbesetID, Num_matched_probes, RefSeq, 
					UniGene, RIKEN, EntrezGene, Symbol, Description) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",(ProbesetID, Num_matched_probes, RefSeq, 
					UniGene, RIKEN, EntrezGene, Symbol, Description))
	
# I had to delete the last two columns because every time I tried to include them I would get the following error
# ValueError: need more than 9 values to unpack