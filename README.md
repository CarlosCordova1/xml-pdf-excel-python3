# xml-pdf-excel-python3
simples tareas con python. estableciendo conexion a base de datos oracle

# descarga de xml y pdf
xml.py
descargaPDF.py

# crear excel
CrearExcel.py

# estableciendo conexion a base de datos oracle
dsn = cx_Oracle.makedsn(host='...', port=.., sid='...')
conn = cx_Oracle.connect(user='...', password='...', dsn=dsn)



# crear archivo json   lee archivo.log
readLogBat.py
