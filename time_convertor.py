#time convertor.
a = int(input("Enter 1  for seconds ,press 2 for minutes and for hours press 3 "))
time = int(input("Enter the tme as per your choise"))
if a == 1:
    hrs = time/3600
    mint = time/60
    print("the time in hours will be ",hrs,"\n"" the time in minutes will be",mint)
elif a == 2:
    hrs = time/60
    sec = time*60
    print("the time in hours will be :",hrs,"\n the time in seconds will be : ",sec)
else :
    mint = time*60
    sec = time*3600
    print("the time in minutes will be :",mint,"\n the time in second will be :",sec)
