#Archivo de prueba para git
#Jose David Libreros Muñoz
#Desarrollo de Software - Grupo 1
#Convenio: ParqueSoft.TI - Alcaldia de Cali

entrada1 = int(input("Escribe un número: "))
entrada2 = int(input("Escribe otro número: "))

print()
print(f"{entrada1} + {entrada2} = {entrada1+entrada2}")
print(f"{entrada1} - {entrada2} = {entrada1-entrada2}")
print(f"{entrada1} x {entrada2} = {entrada1*entrada2}")

if entrada2!=0:
    print(f"{entrada1} / {entrada2} = {entrada1/entrada2}")