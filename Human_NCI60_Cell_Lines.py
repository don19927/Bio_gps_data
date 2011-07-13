import pymysql
import csv

conn = pymysql.connect(user='root',passwd="",db='bio_gps')


cur = conn.cursor()


insert_statement = csv.reader(open('/Users/Donnie/Desktop/NYU Research/Human data table/gnf1h.annot2007.csv', 'rb'))

for row in insert_statement:
	print row
	cur.execute("""INSERT INTO Human_GNF1H_Annotation  (ProbesetID, Num_matched_probes, RefSeq, 
					UniGene, RIKEN, EntrezGene, Symbol, Description, Ensembl_representative, 
					Cross_hyb_EntrezGeneIDs) VALUES(%s)""",(row))
	

#The the problem with this code is the sql VALUES statement treats the variable row as only one value.  so far I am only able to upload data into one column and not the entire table.  Having trouble getting python to recognize the values separately.