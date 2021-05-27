import cx_Oracle
import subprocess
import time
import xlsxwriter
tic = time.process_time()
import os
from datetime import datetime
print('time tic '+ str(tic))
now = datetime.now()
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

dsn = cx_Oracle.makedsn(host='....aguakan.mx', port=..., sid='...')
conn = cx_Oracle.connect(user='...', password='...', dsn=dsn)

vrutadestino='C:\\Users\\jcruz\\Downloads\\pythontest\\excel\\'
#vrutadestino='\\\\172.30.40.10\\cfdi_capa\\jcruz\\'

periodo1='202010'
periodo2='202011'
mes='OCTUBRE'
header='Metadatos SAT '+mes+' vs Emision CFDI AGUAKAN'

workbook = xlsxwriter.Workbook(vrutadestino+'F19RQ4_DM_'+mes+'_DHC900607TZ3.xlsx')
worksheet = workbook.add_worksheet(mes)
bold = workbook.add_format({'bold': True})
date_format = workbook.add_format({'num_format': 'dd/mm/yyyy'})
worksheet.write('A1', header, bold)
nrow = 1
col = 0

c = conn.cursor()
c.execute('select  uuid,rfcemisor,rfcreceptor,nombrereceptor,rfcpac,fechaemision,fechacertificacionsat,monto,efectocomprobante,estatus,fechacancelacion, uuid uuidagk,rrfc rfcreceptoragk,nombre mombrereceptoragk,fchemi fechaemisionagk,fchtim fechatimbrado,base0,base16,sub subtotal,iva,tot total,dif diferencia,uso,impagua,ivaagua from APP.F19_DSAT where uso=\'DM\' and fechaemision between to_date(\''+periodo1+'\'||\'01\',\'yyyymmdd\') and to_date(\''+periodo2+'\'||\'01\',\'yyyymmdd\')-1/86400 ')
res = c.fetchall()
contar=0

worksheet.write(nrow, col, 'UUID')
worksheet.write(nrow, col+1, 'RFCEMISOR')
worksheet.write(nrow, col + 2, 'RFCRECEPTOR')
worksheet.write(nrow, col + 3, 'NOMBRERECEPTOR')
worksheet.write(nrow, col+4, 'RFCPAC')
worksheet.write(nrow, col+5, 'FECHAEMISION')
worksheet.write(nrow, col + 6, 'FECHACERTIFICACIONSAT')
worksheet.write(nrow, col + 7, 'MONTO')
worksheet.write(nrow, col+8, 'EFECTOCOMPROBANTE')
worksheet.write(nrow, col + 9, 'ESTATUS')
worksheet.write(nrow, col + 10, 'FECHACANCELACION')
worksheet.write(nrow, col+11, 'UUIDAGK')
worksheet.write(nrow, col+12,'RFCRECEPTORAGK')
worksheet.write(nrow, col + 13, 'NOMBRERECEPTORAGK')
worksheet.write(nrow, col + 14, 'FECHAEMISIONAGK')
worksheet.write(nrow, col + 15, 'FECHATIMBRADO')
worksheet.write(nrow, col + 16, 'BASE0')
worksheet.write(nrow, col + 17, 'BASE16')
worksheet.write(nrow, col + 18, 'SUBTORAL')
worksheet.write(nrow, col + 19, 'IVA')
worksheet.write(nrow, col + 20, 'TOTAL')
worksheet.write(nrow, col + 21, 'DIFERENCIA')
worksheet.write(nrow, col + 22, 'USO')
worksheet.write(nrow, col + 23, 'IMPAAGUA')
worksheet.write(nrow, col + 24, 'IVAAGUA')
nrow += 1

for row in res:
 worksheet.write(nrow, col, row[0])
 worksheet.write(nrow, col+1, row[1])
 worksheet.write(nrow, col + 2, row[2])
 worksheet.write(nrow, col + 3, row[3])
 worksheet.write(nrow, col+4, row[4])
 worksheet.write(nrow, col+5, row[5],date_format)
 worksheet.write(nrow, col + 6, row[6],date_format)
 worksheet.write(nrow, col + 7, row[7])
 worksheet.write(nrow, col+8, row[8])
 worksheet.write(nrow, col + 9, row[9])
 worksheet.write(nrow, col + 10, row[10],date_format)
 worksheet.write(nrow, col+11, row[11])
 worksheet.write(nrow, col+12, row[12])
 worksheet.write(nrow, col + 13, row[13])
 worksheet.write(nrow, col + 14, row[14],date_format)
 worksheet.write(nrow, col + 15, row[15],date_format)
 worksheet.write(nrow, col + 16, row[16])
 worksheet.write(nrow, col + 17, row[17])
 worksheet.write(nrow, col + 18, row[18])
 worksheet.write(nrow, col + 19, row[19])
 worksheet.write(nrow, col + 20, row[20])
 worksheet.write(nrow, col + 21, row[21])
 worksheet.write(nrow, col + 22, row[22])
 worksheet.write(nrow, col + 23, row[23])
 worksheet.write(nrow, col + 24, row[24])


 nrow += 1
 #a2=c.rowcount
 contar=contar+1
 print(contar)

 rutalfinal=vrutadestino #+ row[0]+ row[1]

workbook.close()
c.close()
conn.close()
toc = time.process_time()
print('time toc '+ str(toc))
print('time tic toc '+ str(toc - tic))

now = datetime.now()

print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)
