import pymysql
import csv

conn = pymysql.connect(user='root',passwd="",db='bio_gps')


cur = conn.cursor()

cur.execute(





"""INSERT INTO Human_GNF1H_Annotation (ProbesetID, Num_matched_probes, RefSeq,
UniGene, RIKEN,	EntrezGene,	Symbol, Description, Ensembl_representative, Cross_hyb_EntrezGeneIDs)""")


for row in csvreader
	insert_statemnt = """INSERT INTO

