# Tales from the Crypt

<img src="https://www.budsartbooks.com/wp-content/uploads/2021/05/ectfc01-tales-from-the-crypt-book_2.jpg" width="400px" />


## Description

In this project, you'll write your own dictionary-based **password cracker** using Python's `hashlib`.

Your cracking program will take as its input a shadow password file (discussed in detail below) consisting of usernames and their associated password hashes, along with a dictionary of candidate passwords. The program should determine the true password for each user by calculating the hash of each entry in the candidate file, then comparing those hashes to the entries stored in the shadow password file.


## Password Management

### Early password files
Back in the former days, UNIX systems stored all users' passwords in a special file called `/etc/passwd`. When a user needed to perform an action that required authentication, like logging in, the system would prompt the user to enter a password, then compare what was entered to the true password stored in the `passwd` file.

However, these early systems stored passwords **in cleartext**. That is, they just stored every user's real password in a text file, like this:

```
dmyers:password1234
```

The `passwd` file did have some protections: it was only readable by `root`, the special system superuser account. Despite that, storing cleartext passwords is obviously a big security risk, because any program that *did* gain the ability to read `/etc/passwd` (for example, by performing a *privilege escalation* attack to gain root access) would immediately know every user's real password.

### Shadow password files

Modern systems do not store users' cleartext passwords. Instead, the system stores a ***hash*** of the user's password in a special file named `/etc/shadow`, the *shadow password file*.

Recall that a hash function is any operation that takes an input bit sequence (which may be of arbitrary length) and converts it to a fixed-size output. You can think of the hash function output as being a "summary" for its input data. Hashing is an important concept that occurs throughout computer science: in the implementation of hash table data structures, in verifying the integrity of file transfers, and in digital signatures, among other applications. There are many different hash functions that operate in different ways. The most important class are the cryptographic hash functions, including the *Secure Hash Algorithm* (SHA) family.

With a shadow file containing password hashes, the basic authentication flow works like this:

- Prompt the user to enter a password
- Compute the hash of the entered password
- Compare to the stored hash in the `shadow` file
- If the two hashes match, the user has entered the correct password with high probability, so allow the action

### Password cracking

<img src="https://imgs.xkcd.com/comics/how_hacking_works_2x.png" width="35%" />

What if the `shadow` file is compromised? This is not great, but it isn't as bad as leaking users' real passwords. An attacker who manages to obtain the `shadow` file would know the **hash** of each user's password, but not the real passwords themselves.

Therefore, the attacker faces a reverse-engineering problem: given the hash of a user's password, find a **real input password** that can be used to generate that hash. This might be easy for simple hash functions, but real password systems use strong **cryptographic hash functions** that are **one-way**.  That is, there's no way to invert a strong hash function to recover the input for a given hash, so the attacker's only choice is to **try many different inputs** until finding one that produces the desired output.

The simplest approach is to launch a **brute-force** attack by generating all possible candidate passwords and testing each one. This is guaranteed to eventually succeed, but is usually impractical. For example, if we consider a 10 character password that may contain uppercase and lowercase letters and the ten digits 0-9, there are

62<sup>10</sup> = 839299365868340224

possible combinations. Long, truly random passwords are always strong.

However, weak passwords are significantly easier to crack. For example, if we consider eight character passwords using lowercase letters, there are only

26<sup>8</sup> = 208827064576

That's still a lot, but it's possible to **pre-compute** every hash for those passwords and store them on a disk using a [rainbow table](https://en.wikipedia.org/wiki/Rainbow_table), a special data structure used to efficiently store password hashes. Given a large stolen list of password hashes, an attacker will likely be able to quickly find many weak passwords that are easy to decrypt.

### Dictionary attacks

For the most part, though, attackers don't even need to resort to brute force attacks. Normal users rarely pick complex passwords and the same general passwords tend to show up repeatedly on different systems. The classic is simply setting your password to `password`, but smarter users still tend to choose passwords that are based on common words, short phrases, or cultural tropes.

For example, you might think that the password `2Timothy3:16` is strong, because it's relatively long with a mixture of characters, digits, and symbols, but it's actually incredibly weak. Passwords based on Bible verses, band names, characters, or movie quotes are easy to crack because users tend to pick from a relatively small number of choices in each category. Popular word combinations like `bluesky` or `pumpkinspice` are also likely to be chosen by many users, so they also make weak passwords.

A **dictionary attack** starts with a list of candidate passwords, which might be based on real passwords leaked from other systems, and then tests each one. In a large `shadow` file, it's likely that many users will have picked passwords that are already in the dictionary.

An attacker can get more passwords for low cost by applying **mangling rules** to the passwords in the dictionary. For example, taking a short phrase and appending a number (e.g., `pumpkinspice1`) is a common heuristic, but it's easy to take each password in the dictionary and generate ten variations with a digit appended. Capitalizing the first letter of a password is an easy mangle (only one character needs to change), as are common substitutions, as shown in this famous xkcd:

<img src="https://imgs.xkcd.com/comics/password_strength.png" width="500px" />


## The Actual Project

Write a program named `crack.py` that can perform dictionary-based password cracking. Use the `linuxwords.txt` file in this repository as your dictionary and crack the hashes given in the `shadow` file.

Your program should perform the following steps:

- Open `linuxwords.txt` and read all of the words it contains into a list
- Open `shadow` and loop through its lines
- For each line, extract the hashed password, discussed in more detail below
- Calculate the hash of every candidate password and compare it against the shadow hash
- When you find a match, print out the real password

## The `shadow` File

When you examine the `shadow` file, you'll see a set of lines like the following:
```
user0:7f8cafc8690f2707d1b7e8a40a59d8299e1af8f862576ba896acaca287fd4006:maniac
user1:5aa3e4036d46c374523a43159305eea18235138321e694dba7c97ae780f2c329:needled
user2:b21302f2a70e32198d6cd4df82d927daa86db4905d9e2b4bde59b06ca929dc58:aromatic
user3:fd9254cc4b3eb78759ae2cba12f76417ea01db87df167ab8a28a065de79d71b5:flossing
user4:662ff72da787dcd27487a6325a65e00ccdf29813939d41659caba78f76bdceb7:reconfigured
user5:ef55d6f38a6966b1d620df4dd41078125cb99ccac145e765b06ca6fb09dfd68f:proceeded
```
Each line contains three fields separated by colons:

- The user name: `user0`, `user1`, etc. These are just placeholders and you won't use them at all in your program

- The user's hashed password. This is the thing you care about.

- The **real password**. This is provided so you can check the output of your program, but **you can't use it in your solution**. This wouldn't be in a real shadow password file.

You'll need to break each line into its three parts, then extract the middle part. There is a method called `split` that is helpful:
```
# Loop through the lines of the shadow file
for line in f:
    line = line.strip()

    # Split the line using : as the separator, returns a list of strings
    fields = line.split(':')

    # The hash is the middle item
    hash = fields[1]

    # Now check the hash against all of the candidate passwords
```

## Hashing

To calculate hashes use the `sha256` function from the `hashlib` library. Import it at the top of your program.
```
from hashlib import sha256
```
SHA-256 is one of the most important cryptographic hash functions. It's widely used in practice, including in the Bitcon blockchain. For reasons you'll get to investigate below, however, it's actuallly not a good choice for real password hashing.

Here's an example (given to you `hash_example.py`) that loops through `linuxwords.txt` and prints every candidate password and its hash:
```
with open('linuxwords.txt', 'r') as f:
    for line in f:
        line = line.strip()

        hash = sha256(line.encode()).hexdigest()
        print(line, hash)
```

- The `sha256` function takes a chunk of binary data as input. `line.encode()` converts the current line to a binary format so `sha256` can operate on it.

- The output of the SHA algorithm is a 256-bit hash value. The `hexdigest` method converts this raw binary output into a human-readable form so you can interact with it as a string.

## Tips

This project doesn't require that much code, but it's conceptually complex. Develop incrementally and make sure you understand the purpose of the program before you start writing a lot of code.

- Look at and run `hash_example.py`. Make sure you're comfortable with the general concept of hashing a string.

- Write the first part of `crack.py` to loop through `linuxwords.txt` and put the words into a list.

- Then open and loop through the lines of `shadow`. Use `split` to extract the password hash from each line.

- Now write the inner loop that compares the shadow hash against the hash of every candidate password.

- **Every entry has a match**! If you can't find it, then your program is missing something.

Happy cracking!
