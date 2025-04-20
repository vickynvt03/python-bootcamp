# Sum of multiples of 3 and 5 below 1000
res = 0
try:
    for i in range(1000):
        if (i % 3 == 0) or (i % 5 == 0):
            res += i
    print(res)
except Exception as e:
    print(f'Error {e}')
        
