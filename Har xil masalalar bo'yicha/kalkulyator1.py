print("calculate programs (+,-,*,/,^,%,//) ishora kirting!\ndasturdan chiqish uchun ''stop' deb yozing!  \nmuallif: Odiljonov  O'.R.")
while True:
    ishora=input("Ishorani kirting: ")
    x=int(input("Birinch sonni kirting: "))
    y=int(input("Ikkinchi sonni kirting: "))
    if ishora=="+":
        s=x+y
        print(f"javob: {x}+{y}={s}" )
    elif ishora=="-":
        s=x-y
        print(f"javob: {x}-{y}={s}" )
    elif ishora=="*":
        s=x*y
        print(f"javob: {x}x{y}={s}" )
    elif ishora=="/":
        s=x/y
        print(f"javob: {x}/{y}={s}" )
    elif ishora=="^":
        s=x**y
        print(f"javob: {x}^{y}={s}" )
    elif ishora=="//":
        s=x//y
        print(f"javob: {x}//{y}={s}  sonning butun qiymati" )
    elif ishora=="%":
        s=x%y
        print(f"javob: {x}%{y}={s} sonning qoldiq qiymati " )
    elif ishora=='stop':
        break
print("Iltimos (+,-,*,/,^,%,//) belgilarni kirting aks holda dasturga qaytadan murojat qilishingizga to'g'ri keladi.")
       
