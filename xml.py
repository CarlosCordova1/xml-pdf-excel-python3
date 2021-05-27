import cx_Oracle
import subprocess
import time
tic = time.process_time()
import os
from datetime import datetime
print('time tic '+ str(tic))
now = datetime.now()
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)



dsn = cx_Oracle.makedsn(host='...aguakan.mx', port=.., sid='...')
conn = cx_Oracle.connect(user='...', password='...', dsn=dsn)

vrutadestino='C:\\Users\\jcruz\\Downloads\\pythontest\\'
#vrutadestino='\\\\172.30.40.10\\cfdi_capa\\jcruz\\'



c = conn.cursor()


c.execute('select \'jcruz\\\'|| upper(to_char(datcrt,\'yyyy\\\')) ||upper(to_char(datcrt,\'mm\'))||\'_\'|| upper(to_char(datcrt,\'mon\'))||\'\\\' pathfile, CASE idttypopr  WHEN 1 THEN \'FACTURAS\\\'  WHEN 2 THEN \'NOTASDECREDITOS\\\'   WHEN 103 THEN \'PAGOS\\\'    WHEN 12 THEN \'PAGOS\\\'  ELSE \'NoFound\\\' END carpeta, uuid namefile, CFDI.CFDI3_3.INVOCA(idtcfd) xmlfile from ASALINAS.TMP_CFD ')
res = c.fetchall()
contar=0
for row in res:
 print (row[0], '-')
 #a2=c.rowcount
 contar=contar+1
 print(contar)
 
 rutalfinal=vrutadestino+ row[0]+ row[1]
 if not os.path.exists(rutalfinal):
     os.makedirs(rutalfinal)
 f2 = open(rutalfinal + row[2] + ".xml", "w+",encoding="utf-8")
 f2.write(str(row[3]))
 f2.close()

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
