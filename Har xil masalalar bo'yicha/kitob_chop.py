print("2 betli varroqni chop etish dasturi. \nmuallif:Oʻ.Odiljonov \nizoh: chop etiladigan varoqlar soni juft boʻlishi lozim!")
a=int(input("Chop etadigan varoq necha bet : "))
s=list(range(1,a+1))
b=s[::2]
c=s[1::2]
c.sort(reverse=True)
print("Birinchi bet:", b, "\n'[]'' ikki qavisdan tashqari barcha raqamlarni belgilab  ctrl+c bilan nusxa oling!")
print("\nizoh: Qogʻozni aylantirib bosh qismi bilan oʻzgartirmasda printerga joylashtiring!")
print("Ikkinch bet: ", c ,"\n'[]'' ikki qavisdan tashqari barcha raqamlarni belgilab  ctrl+c bilan nusxa oling!")
input("\ndasturdan chiqish uchun Enterni bosing! ")

