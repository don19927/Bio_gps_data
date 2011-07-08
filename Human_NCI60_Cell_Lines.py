import pymysql

conn = pymysql.connect(user='root',passwd="",db='bio_gps')


cur = conn.cursor()

cur.execute("""CREATE TABLE Human_NCI60_Cell_Lines (gene_pod varchar(255), huh_7 decimal(11,3),
huh_7 decimal(11,3), HEK293 decimal(11,3), HEK293 decimal(11,3), HL60 decimal(11,3), 
HL60 decimal(11,3),	HEK_293T decimal(11,3), HEK_293T decimal(11,3), DU145 decimal(11,3), 
ACHN decimal(11,3), EKVX decimal(11,3),	HS578T decimal(11,3), IOSE80 decimal(11,3),	M14	decimal(11,3),
MCF7 decimal(11,3), OVCAR8 decimal(11,3), RXF393 decimal(11,3), SKMEL2 decimal(11,3), 
SN12C decimal(11,3), A172 decimal(11,3), A172 decimal(11,3), LN18 decimal(11,3), LN18 decimal(11,3),
astrocytes decimal(11,3), astrocytes decimal(11,3),	U20S decimal(11,3),	U20S decimal(11,3),
SNB19 decimal(11,3), GM97 decimal(11,3), GM133 decimal(11,3), GM1600 decimal(11,3),	
GM2313 decimal(11,3), GM2345 decimal(11,3),	GM2493 decimal(11,3), UO31 decimal(11,3),
_786 decimal(11,3), A204 decimal(11,3), A361 decimal(11,3), A498 decimal(11,3), A549 decimal(11,3),
ACC3 decimal(11,3), ALVA31 decimal(11,3), CAKI1 decimal(11,3), CCRT decimal(11,3), CEM decimal(11,3),
COLO205 decimal(11,3),	DLD1 decimal(11,3),	HCC2998 decimal(11,3),	HCT116 decimal(11,3),	
HCT116 decimal(11,3), HCT15 decimal(11,3), HELA decimal(11,3),	HEPG2 decimal(11,3), HOP62 decimal(11,3),
HOP92 decimal(11,3), HSG decimal(11,3), HT1080 decimal(11,3), IGROV1 decimal(11,3),	JURKAT decimal(11,3),
K562 decimal(11,3), KM12 decimal(11,3), LNCAP decimal(11,3), LOX_IMVI decimal(11,3),
MALME_3M decimal(11,3),	MD_MB231 decimal(11,3),	MDA_MB435 decimal(11,3), MOLT4 decimal(11,3),	
NCI_H226 decimal(11,3),	NCI_H23 decimal(11,3),	NCI_H23 decimal(11,3), NCI_H322M decimal(11,3),	
NCI_460	decimal(11,3), NCVADR_RES decimal(11,3), OVCAR3 decimal(11,3), OVCAR4 decimal(11,3),
OVCAR5 decimal(11,3), PANC1 decimal(11,3), RL7 decimal(11,3), RPMI_8226 decimal(11,3),
RS11846	decimal(11,3), SAOS2 decimal(11,3),	SF268 decimal(11,3), SF295 decimal(11,3), 
SF539 decimal(11,3), SHSYSY_pos_RA decimal(11,3), SHSYSY_RA decimal(11,3), SKMEL28 decimal(11,3),
SKMEL5 decimal(11,3), SKOV3 decimal(11,3), SNB75 decimal(11,3),	SR decimal(11,3), SW620 decimal(11,3),
T24 decimal(11,3), T3M4 decimal(11,3), TK10 decimal(11,3), U251 decimal(11,3), UACC257 decimal(11,3),
UACC62 decimal(11,3), ZR75_1 decimal(11,3), NCI_H226 decimal(11,3),	U87 decimal(11,3), U87 decimal(11,3),
U118 decimal(11,3), U118 decimal(11,3), U138 decimal(11,3), U138 decimal(11,3), 
HEK_293_T_rex decimal(11,3), HEK_293_T_rex decimal(11,3), HT29 decimal(11,3))""")