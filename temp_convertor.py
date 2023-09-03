# temperature convertor.
a = int(input("Enter 1 for celsius , press 2 fyor fahrenheit and for kelvin press 3"))
temp = int(input("Enter the temperature as perour choise : "))
if  a == 1:
    kel = 273+temp
    feh = 9/5*temp +32
    print("the temperature in kelvin will be : ",kel,"\n the temperature in fahreheit will be : ",feh)
elif a == 2 :
    celc = (temp - 32)*5/9
    kel = 273 + celc
    print("the temperature in celsius will be :",celc,"\n the temperature in kelvin will be : ",kel)
else :
    celc = temp - 273
    feh = 9/5*celc + 32
    print("the tmperature in celsius wll be :",celc,"\n the temperature n faheenheit will be :",feh)
    
