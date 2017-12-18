def my_gcd(a,b):
	if b == 0:
		return a
	else:
		return my_gcd(b, a%b)
def my_gcd2(a,b):
	while a != 0 and b != 0:
		if a>b:
			a = a%b
		else:
			b = b%a
	return max(a,b)
print(my_gcd(625,25))
print(my_gcd2(625,25))

