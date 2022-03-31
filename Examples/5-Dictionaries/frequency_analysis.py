"""
Use a dictionary to perform letter frequency analysis
"""

f = open('cipher.txt', 'r')
counts = {}

for line in f:
    line = line.strip()

    for ch in line:
        if ch not in counts:
            counts[ch] = 0
        
        counts[ch] = counts[ch] + 1

print(counts)
