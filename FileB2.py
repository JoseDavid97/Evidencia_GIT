#archivo de prueba git
#Jose David Libreros Muñoz
#Desarrollo de software - Grupo 1
#Convenio: ParqueSoft.TI - Alcaldia de Cali

strw = input()
strw = strw.split()

strw2=[]
for i in range(int(strw[0]),int(strw[1])+1):
    strw2.append(str(i))

print(' '.join(strw2))