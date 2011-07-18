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





#here is the original code with commented issues

import pymysql
import csv

conn = pymysql.connect(user='root',passwd="",db='bio_gps')


cur = conn.cursor()


insert_statement = csv.reader(open('/Users/Donnie/Desktop/NYU Research/Human data table/gnf1h.annot2007.csv', 'rU'))

csv.field_size_limit()

for ProbesetID, Num_matched_probes, RefSeq, UniGene, RIKEN, EntrezGene, Symbol, Description, Ensembl_representative, Cross_hyb_EntrezGeneIDs in insert_statement:

	cur.execute("""INSERT INTO Human_GNF1H_Annotation_2  (ProbesetID, Num_matched_probes, RefSeq, 
UniGene, RIKEN, EntrezGene, Symbol, Description, Ensembl_representative, Cross_hyb_EntrezGeneIDs)
VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(ProbesetID, Num_matched_probes, RefSeq, 
UniGene, RIKEN, EntrezGene, Symbol, Description, Ensembl_representative, Cross_hyb_EntrezGeneIDs))

# With this code I will keep getting an error 
#ValueError: need more than 9 values to unpack
#This error is saying that I don't have enough values to mach with the variable (x,y,z)=(1,2)
#however I have checked my values and their are 10 and 10 variable so I am not sure of the error
#It has something to do with the last two columns because I am able to produce a table if I exclude them
