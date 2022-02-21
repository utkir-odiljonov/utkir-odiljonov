from num2words import num2words

print("#Sizga xohlagan tilingizda ushbu raqamni  qanday yozilishi kerakligini ko'rsatib beradi. Ishlatib ko'ring ushbu kodni.")
def num2words_Function():
    ism=input("ismingiz: ")
    number=int(input('Ixtiyoriy sonni kiriting:'))
    language= int(input('Biror bir tilni oldidagi raqmini tanlang: \n1=>en=>English: \n2=>ru=>Rossiya: \n3=>es=>Ispan: \n4=>uz=> Uzbek: \n>>>'))
    if language==1:
        converter_number=num2words(number,lang='en')
        print(converter_number)

    if language==2:
        converter_number=num2words(number, lang='ru')
        print(converter_number)
    
    if language==3:
        converter_number=num2words(number, lang='es')
        print(converter_number)
    else:
        print(f"{ism} Hozir oʻzbekchasi ham chiqadi deb oʻyladizmi? \n yoʻq chiqmaydi. Sabab siz hali ham dasturlashni  oʻqimasdan yuribsiz ku. Yangiyoʻldan ham chiqsin") 
 
        


num2words_Function()

