def fast_power(a,n):
	if n == 0:
		return 1
	elif n%2 == 1:
		return a*fast_power(a, n-1)
	else: n%2 == 0
		return fast_power(a*a, n//2)
print(fast_power(2, 3))
