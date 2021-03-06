def euler21():
	
	# Returns the sum of the divisors of n 
	def sumDivs(n):
		return sum([i for i in range(1, n) if n % i == 0])

	# Returns a tuple containing the sumDivs(n) and n if sumDivs(sumDivs(n)) is equal to n, otherwise (None, None)
	def amicable(n):
		total = sumDivs(n)
		return total if sumDivs(total) == n else None

	# Initialize seen list, keeps track of all amicable numbers we have seen in the past
	seen = []
	total = 0

	# Loop through all numbers in the range [0, 10000)
	for i in range(10000):
		x = amicable(i)
		# Problem specifies that x cannot equal y, also if x is None, then the number is not amicable
		if x != None and x != i:
			# Do not add repeats to the total
			if x not in seen:
				# Add numbers to total and to list of seen numbers
				total += x + i
				seen.extend([x, i])
	return total
