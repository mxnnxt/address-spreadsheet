import xlwt
import string
import random
from random import getrandbits
#user input
times = int(input("Enter the number of times you would like to jig: "))
addy1 = str(input("Enter Address 1: "))
city = str(input("Enter City: "))
state = str(input("Enter State (ex. NY) : "))
area = str(input("Enter Zip Code: "))
country = str(input("Enter Country (ex. US) : "))
phone = input("Phone Number Prefix: ")

book = xlwt.Workbook(encoding="utf-8")
#create sheet
sheet1 = book.add_sheet("Sheet 1")
#create columns
sheet1.write(0, 0, "First Name")
sheet1.write(0, 1, "Last Name")
sheet1.write(0, 2, "Address Line 1")
sheet1.write(0, 3, "Address Line 2")
sheet1.write(0, 4, "City")
sheet1.write(0, 5, "State")
sheet1.write(0, 6, "ZIP")
sheet1.write(0, 7, "Country")
sheet1.write(0, 8, "Phone")

#start under column titles
i=2
#write data
for i in range(times):
	i = i+1
	#firstname
	names = ["Beck","Glenn","Becker","Carl","Beckett","Samuel","Beddoes","Mick","Beecher","HenryWard","Beethoven","Ludwigvan","Begin","Menachem","Bell","Alexander","Graham","Belloc","Hilaire","Bellow","Saul","Benchley","Robert","Benenson","Peter","BenGurion","David","Benjamin","Walter","Benn","Tony","Bennington","Chester","Benson","Leana","Bent","Silas","Bentsen","Lloyd","Berger","Ric","Bergman","Ingmar","Berio","Luciano","Berle","Milton","Berlin","Irving","Berne","Eric","Bernhard","Sandra","Berra","Yogi","Berry","Halle","Berry","Wendell","Bethea","Erin","Bevan","Aneurin","Bevel","Ken","Biden","Joseph","Bierce","Am","Brose","Biko","Steve","Billings","Josh","Biondo","Frank","Birrell","Augustine","Black","Elk","Blair","Ro","Bert","Blair","Tony","Blake","William","Blakey","Art","Blalock","Jolene","Blanc","Mel","Blanc","Raymond","Blanchet","Cate","Blix","Hans","Blood","Rebecca"]
	firstName = names[random.randint(0, 99)]
	sheet1.write(i, 0, firstName)
	#lastname
	lastName = names[random.randint(0, 99)]
	sheet1.write(i, 1, lastName)
	#address line 1
	size = 4
	chars1 = string.ascii_uppercase + string.digits
	chars2 = ''.join(random.choice(chars1) for _ in range(size))
	addy2 = chars2+" "+addy1
	sheet1.write(i, 2, addy2)
	#address line 2
	numbers = random.sample(range(10), 4)
	num1 = str((''.join(map(str, numbers))))
	size1 = 4
	chars3 = string.ascii_uppercase + string.digits
	chars4 = ''.join(random.choice(chars3) for _ in range(size1))
	addy3 = chars4+" "+"APT "+num1
	sheet1.write(i, 3, addy3)
	#City
	sheet1.write(i, 4, city)
	#state
	sheet1.write(i, 5, state)
	#zip
	sheet1.write(i, 6, area)
	#country
	sheet1.write(i, 7, country)
	#phone
	number5 = random.sample(range(10), 7)
	num2 = str((''.join(map(str, number5))))
	phone_num = phone+num2
	sheet1.write(i, 8, phone_num)


print("SUCCESSFULLY SAVED TO SPREADSHEET")
book.save("trial.xls")