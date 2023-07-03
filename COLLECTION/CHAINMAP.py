from collections import ChainMap

a = {1: 'tech', 2: 'language'}  # dictionary record
b = {3: 'ML', 4: 'python'}

a1 = ChainMap(a, b)  # single view for multiple mapping

print(a1)
