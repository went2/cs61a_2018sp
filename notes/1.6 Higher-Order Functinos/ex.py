"""  Newton's Method """

def find_zero(f, df):
	def near_zero(x):
		return approx_eq(f(x), 0)
	return improve(newton_update(f, df), near_zero)

def newton_update(f, df):
	def update(x):
		return x - f(x) / df(x)
	return update

def power(x, n):
	product, k = 1, 0
	while k < n:
		product, k = product * x, k + 1
	return product

def root(n, a):
	def f(x):
		return power(x, n) - a
	def df(x):
		return n * power(x, n-1)
	return find_zero(f, df)

def improve(update, close, guess=1):
	k = 0
	while not close(guess) and k <= 100:
		guess = update(guess)
		k += 1
	return guess

def approx_eq(x, y, tolerance=1e-14):
	return abs(x-y) < tolerance






