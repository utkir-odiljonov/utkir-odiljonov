# Qog'ozni oldi orqa qilib chop etish usuli
# muallif Odiljonov O'.R.
print("2 betli qog'ozga oldi orqa tarfiga chop etish dasturi \nmuallif: o'.R.Odiljonov")
a=int(input("Umumiy varoqni sonini kirting: "))
s=list(range(1,a+1))
b=s[::2]
c=s[1::2]
c.sort(reverse=True)
print("birinchi bet: ",b)
print("izoh: \nqog'ozni aylantirib bosh qismi bilan printerga joylashtiring")
print("Ikkinchi bet: ",c)
input("Dasturdan chiqish uchun Enter tugmasini bosing! ")