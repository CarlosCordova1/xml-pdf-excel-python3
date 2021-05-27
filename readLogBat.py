import os
import re
import json
from datetime import datetime
vrutadestino='\\\\...aguakan.mx\\...\\...\\log\\'
buscar='error'
iniciodate='INICIO LOG CADENA BATCH'
findate='Fin Tratamientos Diarios ...'
file_name='BATCH.Log'
jsonval = {}
jsonval["buscar"] = buscar

with os.scandir(vrutadestino) as entries:
    for entry in entries:
        #print(entry.name)
        #print(entry.path)
        if entry.name==file_name:
         jsonval["file"]=entry.name
         jsonval["file_path"] = entry.path
         jsonval["jsoncreate"]=str(datetime.now())
         f = open(entry.path, "r")


         error = re.search(buscar, f.read())
         #print(error)
         if error is not None:
             if error.group()==buscar:
              jsonval["error"] = True
             else:
              jsonval["error"] =False
             #jsonval["file_content"] = error.string
         else:
             jsonval["error"] = False
         f.close()

         #print(x)
         #y = json.dumps(x)
         #print(y)
         #print(f.read())
         contar=1;

         fila={}
         f2 = open(entry.path, "r")
         valida=0
         validafin = 0;
         for line in f2:
            inicio = re.search(iniciodate, line)
            if inicio is not None and inicio.group()== iniciodate:
                valida=contar+4;
             #print('line >' + str(contar))
            fin = re.search(findate, line)
            if fin is not None and fin.group() == findate:
                validafin = contar + 4;
            fila[str(contar)]=line
             #print (line)
            contar=contar+1
         f2.close()
         jsonval["date_inicio"] = fila[str(valida)].replace('\n','');
         jsonval["date_fin"] = fila[str(validafin)].replace('\n', '');
    #jsonval["file_content"]=fila




print(json.dumps(jsonval))
filesalida=vrutadestino+"BATCH-"+jsonval["jsoncreate"].replace('.',':').replace(':','-')+".json"
print(filesalida)
f3 = open(filesalida, "w")
f3.write(str(json.dumps(jsonval)))
f3.close()
