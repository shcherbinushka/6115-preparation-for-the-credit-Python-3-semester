def fib_2(n):
	fib1 = 1
	fib2 = 1
	i = 2
	while i < n:
		fib_sum = fib1 + fib2
		fib1, fib2 = fib2, fib_sum
		i += 1
	return fib_sum

def fib(n):
	if n < 2:
		return n
	else:
		return fib(n-1) + fib(n-2)

print (fib(8), fib_2(8))