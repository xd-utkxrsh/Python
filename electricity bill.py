#program to calculate electricity bill
eb=int(input("Enter electricity units: "))

if eb>=1 and eb<=100:
    print(eb*1.5,"\n\n\n")
elif eb>=101 and eb<=200:
    print(eb*2.5,"\n\n\n")
elif eb>=201 and eb<=300:
    print(eb*4,"\n\n\n")
elif eb>=301 and eb<=350:
    print(eb*5,"\n\n\n")
elif eb>350:
    print(eb*15,"\n\n\n")
else:
    print("Enter correct units.\n\n\n")

#program to calculate bmi with inputs in pounds and inches
weight=float(input("enter weight in pounds: "))
height=float(input("Enter height in inches: "))
wkg=weight*0.45359237
hm=height*0.0254
bmi=wkg/hm*hm
if bmi<18.5:
    print("Underweight","\n\n\n")
elif bmi<25:
    print("Normal","\n\n\n")
elif bmi<30:
    print("Overweight","\n\n\n")
else:
    print("Obese","\n\n\n")