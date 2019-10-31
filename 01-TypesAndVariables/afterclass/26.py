height = int(input("Podaj wzrost w cm: "))
weight = int(input("Podaj wagę w kg: "))
height = height/100
result = weight/ (height ** 2)

#If sequence
if result < 18.5:
    status = "Underweight"
if result < 25 and result > 18.5:
    status = "Normal"
if result > 25 and result < 30:
    status = "Overweight"

#Showing result
print (f"Wskaźnik BMI: {result} ({status})")