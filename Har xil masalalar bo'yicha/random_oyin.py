import random

name=["Sardor",
			"Bahtiyor",
			"Alisher",
			"Anvar", 
			"Karim",
			"Oʻtkor"]
gams=["Karta oʻynayapdi",
			"Chillik oʻynayapdidi"
			"Futboll oʻynayapdi", 
			"Gʻaltak tepyapdi",
			"Ariqda suzmoqda",
			"Karate bilan shugʻullanmoqda"]

a=random.randint(0, len(name))
s=random.randint(0, len(gams))
print(name[a],"-" , gams[s])
			