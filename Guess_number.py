while True:	
	try:
		import random
		print("Atspėk skaičių nuo x iki y")
		x = int(input("Parašyk x: "))
		y = int(input("Parašyk y: "))
		while True:
			m = random.randint(x, y)
			i = 1
			while True:
				z = int(input("Tavo spėjimas: "))
				if m == z:
					print("Sveikinu atspėjus iš",i,"karto")
					break
				elif m < z:
					print("Skaičius yra mažesnis")
					i += 1
				elif m > z:
					print("Skaičius yra didesnis")
					i += 1
	except ValueError:
		print("Įrašyk sveikąjį skaičių")
