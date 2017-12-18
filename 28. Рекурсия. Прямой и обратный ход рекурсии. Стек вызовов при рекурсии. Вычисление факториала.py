#
def factor(n):
	return 1 if n == 0 else factor(n - 1)*n
print(factor(5))