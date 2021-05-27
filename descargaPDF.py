import os
import requests
from time import time
import time
import wget
import cx_Oracle
from multiprocessing import Process
from datetime import datetime
tic = time.process_time()
#print('time tic '+ str(tic))
now = datetime.now()
#print("now =", now)
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Now date and time =", dt_string)

dsn = cx_Oracle.makedsn(host='....aguakan.mx', port=..., sid='...')
conn = cx_Oracle.connect(user='...', password='...', dsn=dsn)

#vrutadestino = '\\\\172.30.40.10\\cfdi_capa\\jcruz\\'
vrutadestino='C:\\Users\\jcruz\\Downloads\\pythontest\\'

def descargarpdf(id,name,finalruta):

    urlfac2 = 'https://www.aguakan.com/fmt/cfd.php?cadena='
    print('nombre - > ' + str(name))
    #wget.download(urlfac2 + str(id) + '&nombre' + str(name), vruta + '/' + str(name) + '.pdf')
    try:
        #myfile = requests.get(urlfac2 + str(id) + '&nombre' + str(name), allow_redirects=True)
        if os.path.exists(finalruta + '/' + str(name) + '.pdf'):
           print("NO creado, ya existe - >  "+ finalruta + '/' + str(name) + '.pdf')
        else:
         myfile = requests.get(urlfac2 + str(id), allow_redirects=True)
         open(finalruta + '/' + str(name) + '.pdf', 'wb').write(myfile.content)
         print("SI creado - >  " + finalruta + '/' + str(name) + '.pdf')
    except:
        print("An exception occurred ")
        print('nombre error - > ' + str(name))




c = conn.cursor()
c.execute('select \'jcruz\\\'|| upper(to_char(periodo,\'yyyy\\\')) ||upper(to_char(periodo,\'mm\'))||\'_\'|| upper(to_char(periodo,\'mon\'))||\'\\\' pathfile, CASE idttypopr  WHEN 1 THEN \'FACTURAS\\\'  WHEN 2 THEN \'NOTASDECREDITOS\\\'   WHEN 103 THEN \'PAGOS\\\'    WHEN 12 THEN \'PAGOS\\\'  ELSE \'NoFound\\\' END carpeta, uuid namefile,app.api_pqcnc_1_0.CREATOKEN (\'\',idtcfd) pdfcadena  from asalinas.JCRUZ_TMP_PDF where edo =0   ')

res = c.fetchall()
contar=0
processes = []
if __name__ == "__main__":
 for row in res:
  #print (row[2], ' - ')
  #a2=c.rowcount
 # print(contar)
  rutalfinal = vrutadestino + row[0] + row[1]


  if not os.path.exists(rutalfinal):
   os.makedirs(rutalfinal)
  #processes.append(Process(target=descargarpdf, args=(row[3],row[2],rutalfinal,)))
 # processes[contar].start()
  descargarpdf(row[3],row[2],rutalfinal)

  contar = contar + 1
  print('Proceso ' + str(contar) + ' lanzado')

#conn.commit()
c.close()
conn.close()


#for process in processes:
   # process.join()

toc = time.process_time()
#print('time toc ' + str(toc))
#print('time tic toc ' + str(toc - tic))


now = datetime.now()
#print("now =", now)
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Now date and time =", dt_string)
