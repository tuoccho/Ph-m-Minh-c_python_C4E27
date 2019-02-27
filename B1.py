i = int(input("Nhap chieu cao (cm): "))
j = int(input("Nhap can nang (kg): "))
k = i/100
BMI = float(j/k**2)
print("Chi so BMI cua ban la:", BMI )
if BMI < 16:
    print("Severely underweight")
if 16 < BMI < 18.5:
    print("Underweight")
if 18.5 < BMI < 25:
    print("Normal")
if 25 < BMI < 30:
    print("Overweight")
else:
    print("Obese")