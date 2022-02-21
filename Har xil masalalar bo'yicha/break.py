# while, break operstorlari yordamida ikki sonni qoʻshish dasturi
print(" Muallif: Oʻ.Odiljonov")
rraqam_son=0
natija=0
while True:
	raqam= int(input("Raqam sonni kirting: "))
	natija+=raqam
	raqam_son+=1
	if raqam_son>1:
		print("natija:", natija)
		break