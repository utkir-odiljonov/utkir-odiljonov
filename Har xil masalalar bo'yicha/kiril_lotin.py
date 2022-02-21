import iuliia
print("muallif:Oʻ.R.Odiljonov(@lion_user86")
while True:
	kirl_text=input("Кирил алифбосида матн киртинг: ")
	lotin_text=iuliia.translate(kirl_text, schema=iuliia.ICAO_DOC_9303)
	print(lotin_text)