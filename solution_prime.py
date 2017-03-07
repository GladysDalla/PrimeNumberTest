def is_prime_number():
	"""finds prime numbers  between range 0 and n"""
	
	for number in range (0,math.sqrt(n)):
		if number > 1:
			for i in range (2,number):
				if (num % i) == 0:
					break
			else:
				print(number)


