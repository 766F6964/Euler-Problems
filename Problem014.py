def collatz_conjuncture(n): 
	if n % 2 == 0: 
		return n // 2 
	else:
		return 3 * n + 1


def collatz_distance(n, mem={1:1}):
    if n not in mem: 
    	mem[n] = collatz_distance(collatz_conjuncture(n)) + 1
    return mem[n]

print(max(range(1,1000000), key=collatz_distance))