# Frequency Analysis

<img src="https://upload.wikimedia.org/wikipedia/commons/c/c2/Danc-01.jpg" width="300px" />


## Description

Sir Arthur Conan Doyle wrote "The Adventure of the Dancing Men" in 1905. In it, Sherlock Holmes receives a request for help from a man whose wife has been receiving strange messages. The notes appear to contain only drawings of dancing stick figures, but leave her inexplicably terrified.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Dancing_men.svg/692px-Dancing_men.svg.png" width="50%" />

Holmes realizes that the stick men are actually a code. Each different figure corresponds to one letter of the alphabet and the flags mark the boundaries between words. Holmes breaks the code and learns the truth...which you'll have to learn for yourself by reading the story

The Dancing Men are an example of a **substitution cipher**: one of the simplest techniques for encoding secret messages. In this scheme, each letter in the **plaintext message** is mapped to a different letter of the alphabet (or another symbol, as in the Dancing Men) to yield the **ciphertext message**. Knowing the substitutions allows the encryption to be reversed.

For example,the coded message `GHHGDB GH EGJM` could be deciphered as `ATTACK AT DAWN` by substituting

- A for G
- T for H
- C for D
- K for B
- D for E
- W for J
- M for N.

Although substitution ciphers are easy to implement, they are insecure, because they’re vulnerable to **frequency analysis attack**. This is the method Holmes uses to break the Dancing Men cipher in the story.

The letters of English words are not randomly distributed: *e* is the most common (about 13% of occurrences), followed by *t* (9%) and then *a* (8%). Letters *q* and *z* each account for less than 1% of occurrences in common English text.

Therefore, given a large body of text that’s been encoded using a substitution cipher, the most frequently occurring letter is likely to be *e*, with the second most frequently occurring *t*, and so forth. Even when the correspondence between encrypted and decrypted letter frequencies is not exact, frequency analysis often yields enough information about the message to make decryption possible.

In this project, your mission is to use frequency analysis to decipher a message that I’ve encoded using a substitution cipher. Use frequency analysis to determine the letter frequencies in the enciphered text. Then, using a table of standard English letter frequencies, decrypt the ciphertext to produce the plaintext output.

## Input File

The enciphered message is in the file `cipher.txt`. It contains the opening text of a famous work of literature. The punctuation, spaces, and capitalization of the text have been left intact and both capital and lowercase letters have been encrypted using the same substitutions.


## Tips

Write two programs:

- `frequency_analysis.py` to scan the ciphered text file and count the number of occurrences of each character. Use a dictionary to store the counts and our previous letter-counting example as a starting point. Print out the frequency of occurrence of each character.

- `decode.py` to translate the ciphered text file and print the deciphered version. Use a dictionary to store the mapping for each ciphertext letter to its plaintext counterpart (you'll need to code the mappings in this dictionary **by hand** as part of the program).

Note that the letter frequencies you obtain in step 1 may not perfectly map to the frequencies of letters in ideal English language text. You may need to do a little bit of experimentation to find the right mappings and perform the decryption; this is part of the process. **You do not need to (and probably can't) determine the correct mappings automatically**. This project is as much of a puzzle as it is a programming task.

**Uppercase and lowercase letters**. The ciphertext contains both uppercase and lowercase letters. I recommend converting each line of text to lowercase before you perform frequency analysis, so that you obtain complete counts for every letter. You can use the string's `.lower()` method to convert a line to all lowercase letters:

```
# Example of converting text to lower case

str = 'HELLO ,WORLD.'
str.lower()
print(str)  # prints 'hello, world.'
```

Spaces and punctuation are not enciphered, so you don't need to analyze them.

**Deciphering the code**. In your deciphering program, manually create a dictionary that stores the letter decryptions you derived from the first step.

```
decodings = {}

decodings['a'] =      # Put the decrypted letter for lowercase 'a' here
decodings['A'] =      # Capital letters have the same mappings as lowercase

# Complete the rest of the dictionary for all letter decodings
```

Write a loop that reads each line of the cipher file, then loops through the letters on each line. As you read each letter, look it up in the `decodings` dictionary and output its corresponding unencrypted letter.
