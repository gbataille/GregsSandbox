def test(*a, **b):
	print(a)
	print(b)

test(1,2,'a', 8, 'f', A=5, toto='tutu')
