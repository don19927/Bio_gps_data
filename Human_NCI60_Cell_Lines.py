import pymysql
import csv

conn = pymysql.connect(user='root',passwd="",db='bio_gps')


cur = conn.cursor()

cur.execute("""CREATE TABLE Human_GNF1H_Annotation (ProbesetID varchar(255), Num_matched_probes int,
RefSeq varchar(255), UniGene varchar(255), RIKEN varchar(255),	EntrezGene int,	Symbol varchar(255),
Description	varchar(2500), Ensembl_representative varchar(255), Cross_hyb_EntrezGeneIDs varchar(255))""")

#here is the original code with commented issues

import pymysql
import csv

conn = pymysql.connect(user='root',passwd="",db='bio_gps')


cur = conn.cursor()

file = csv.DictReader(open('/Users/Donnie/Desktop/NYU Research/Human data table/gnf1h.annot2007.csv', 'rU'), dialect = csv.excel)


csv.field_size_limit(100000000000)

for ProbesetID, Num_matched_probes, RefSeq, UniGene, RIKEN, EntrezGene, Symbol, Description, Ensembl_representative, Cross_hyb_EntrezGeneIDs in file:

	cur.execute("""INSERT INTO Human_GNF1H_Annotation_2  (ProbesetID, Num_matched_probes, RefSeq, 
UniGene, RIKEN, EntrezGene, Symbol, Description, Ensembl_representative, Cross_hyb_EntrezGeneIDs)
VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(ProbesetID, Num_matched_probes, RefSeq, 
UniGene, RIKEN, EntrezGene, Symbol, Description, Ensembl_representative, Cross_hyb_EntrezGeneIDs))

# The code will upload the exact number of values in the tabl but only uploads the column names 
#and not in their corresponding column
