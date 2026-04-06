"""
Example of hashing passwords using SHS-256 and hashlib
"""

from hashlib import sha256

with open('linuxwords.txt', 'r') as f:
    for line in f:
        line = line.strip()

        hash = sha256(line.encode()).hexdigest()
        print(line, hash)
