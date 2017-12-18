def hanoi(n, i=1, j=2):
	if n == 1:
		print('переставить 1', 'блин с', i, 'на', j, 'стержень')
	else:
		hanoi(n - 1, i, 6 - i - j)
		print('переставить', n, 'блин с', n - 1, i, 'на', j, 'стержень')
		hanoi(n - 1, 6 - i - j, j)

hanoi(7)