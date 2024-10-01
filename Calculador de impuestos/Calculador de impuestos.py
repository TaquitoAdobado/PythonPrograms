#Calculador de impuestos

income = float(input("Introduce el ingreso anual: ")) #Escribe ingreso anual

if income <= 85528: #Si ingreso anual es menor igual a 85528
	tax = income * 0.18 - 556.02 # impuesto = 18% de ingreso menos 556.02
	
else: #Si ingreso anual es mayor a 85528
    tax = 14839.2 + ((income - 85528) * 0.32) #Impuesto = 14829.2 +32% del excedente de 85228

if tax < 0: #Si el impuesto es menor a 0
    tax = 0 #Impuesto = 0 , no paga impuestos
    
tax = round(tax, 0) #Redondeamos impuesto

print("El impuesto es:", tax, "pesos")


#Si ingresamos 10,000 el impuesto debe ser 1244.0 pesos
#Si ingresamos 100,000 el impuesto debe ser 19470.0 pesos
#Si ingresamos 1,000 el impuesto debe ser 0.0 pesos
#Si ingresamos -100 el impuesto debe ser 0.0 pesos
