# Tales from the `crypt`

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

Recall that a hash function is any operation that takes an input bit sequence (which may be of arbitrary length) and converts it to a fixed-size output. You can think of the hash function output as being a "summary" for its input data. Hashing is an important concept that occurs throughout computer science: in the implementation of hash table data structures, in verifying the integrity of file transfers, and in digital signatures, among other applications.

There are many different hash functions that operate in different ways. Every Java class has a method called `hashCode` which can be used to compute a hash code from an object's data. The default `hashCode` is based on the object's memory address, but a class can also define its own `hashCode` that's appropriate for its own data ([see here](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html#hashCode()) for the `String` class documentation).

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

possible combinations. Therefore, long, truly random passwords are always strong.

However, weak passwords are significantly easier to crack. For example, if we consider eight character passwords using lowercase letters, there are only

26<sup>8</sup> = 208827064576

That's still a lot, but it's possible to **precompute** every hash for those passwords and store them on a disk using a [rainbow table](https://en.wikipedia.org/wiki/Rainbow_table), a special data structure used to efficiently store pre-computed password hashes.

### Dictionary attacks

For the most part, though, attackers don't even need to resort to brute force attacks. Normal users rarely pick complex passwords and the same general passwords tend to show up repeatedly on different systems. The classic, of course, is simply setting your password to `password`, but smarter users still tend to choose passwords that are based on common words, short phrases, or cultural tropes.

For example, you might think that a password like `2Timothy3:16` is strong, because it's relatively long with a mixture of characters, digits, and symbols, but it's actually incredibly weak. Passwords based on Bible verses, popular band names, characters, or movie quotes are easy to crack because users tend to pick from a relatively small number of choices in each category. Popular word combinations like `bluesky` or `pumpkinspice` are also likely to be chosen by many users, so they also make weak passwords.

A **dictionary attack** starts with a list of candidate passwords, which might be based on real passwords leaked from other systems, and then tests each one. In a large `shadow` file, it's likely that many users will have picked passwords that are already in the dictionary.

An attacker can get more passwords for low cost by applying **mangling rules** to the passwords in the dictionary. For example, taking a short phrase and appending a number (e.g., `pumpkinspice1`) is a common heuristic, but it's easy to take each password in the dictionary and generate ten variations with a digit appended. Capitalizing the first letter of a password is an easy mangle (only one character needs to change), as are common substitutions, as shown in this famous xkcd:

<img src="https://imgs.xkcd.com/comics/password_strength.png" width="40%" />


## The Actual Project

Write a program named `crack.c` that can perform dictionary-based password cracking. Your program will use the `words` file included in the project workspace as its dictionary and the built-in C `crypt` function to calculate hashes, which we'll discuss in more detail below. In addition, your program needs to support two mangling options:

- Toggling the case of the first letter in a dictionary word
- Appending each of the digits 0-9 to a word and testing each of the resulting passwords
