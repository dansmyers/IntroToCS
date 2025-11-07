# Bits and Bytes

## Transistors

A computer is an *electronic programmable calculating machine*. At a base level, any operation a computer can perform is executed by
electrical signals passing through circuits that implement logical operations. These circuits are built from *transistors*.

You can think of a transistor as a switch.

``` 
           power
             |
             |
             |  collector
          ---
  base   |
---------|
         |
          ---
             |
             v  emitter
             |
             |
           ground
```

When current is applied to the base terminal, the transistor switches "on" and allows current to flow from the collector to the 
emitter.

Multiple transistors can combine together to create circuits that implement the basic logical operations AND, OR, and NOT. 
These basic functions can be further combined to design complex circuits that add, compare, switch, store, and perform all of the 
other tasks that are required for computation.

We won't actually study the design of digital logic circuits in the course &mdash; Dr. Carrington covers logic design as part of 
Applied Discrete Mathematics. For now, we'll just accept (using our powers of abstraction) that we have the capability to create the 
basic physical hardware of a computer.

## Bits

We can recognize two basic states in any digital logic circuit:
  
  1. The *presence* of a significant electrical voltage
  2. The *absence* of any significant electrical voltage

This recognition gives rise to the concept of a *binary digit* or ***bit***.

A single bit represents a basic unit of information having only two possible values, which we'll label as 0 (representing falseness or
absence) and 1 (representing truth or presence).

The meaning of "significant electrical voltage" depends on the technology used to implement the system's logic gates. It's common for 
a logical level of 0 to be represented by a voltage close to 0 and for a logical level of 1 to be represented by a voltage of +3.5 V.

## Everything is Bits

**Any information in a computer system, regardless of its source, type, or use is represented as a sequence of bits**.

Numbers, text strings, program instructions, images, audio, video, web pages, spreadsheets, databases, and all other kinds of
information used by computer programs must ultimately be encoded as sequences of bits.

This truth has an important corollary: the meaning of any particular string of bits depends on its context. For 
example, the 32-bit sequence

```
01100101011001100110011101101000
```

could represent a single signed `int`, or an unsigned `int`, or four `char` values, or two `short` values, or a machine language
instruction, or a `float`. The interpretation of the bit string depends upon the context in which it's used.

## Bits and Powers of 2

Suppose that you have a grouping of *N* bits. How many distinct combinations can that grouping represent? Each bit may take one of two
values, 0 or 1, so there are two choices for each of the *N* positions.

  - A single bit can encode two values (0 and 1)
  - Two bits can encode four values (00, 01, 10, and 11)
  - Three bits can encode eight values (000, 001, 010, 011, 100, 101, 110, and 111)
  
In general, an *N* bit sequence can represent *2^N* distinct values.

Here are all the powers of 2 from 0 to 20:

```
2^0 = 1
2^1 = 2
2^2 = 4
2^3 = 8
2^4 = 16
2^5 = 32
2^6 = 64
2^7 = 128
2^8 = 256
2^9 = 512
2^10 = 1024
2^11 = 2048
2^12 = 4096
2^13 = 8192
2^14 = 16384
2^15 = 32768
2^16 = 65536
2^17 = 131072
2^18 = 262144
2^19 = 524288
2^20 = 1048576
```

For back-of-the-envelope calculations, it's helpful to remember that 2^10 is a little larger than 1000 and that 2^20 is a little 
larger than 1 million (slightly less than 5% larger, in fact). This pattern holds at higher values, although it becomes less accurate:
2^30 is about 7.5% larger than 1 billion and 2^40 is about 10% larger than 1 trillion.

## Bytes and Larger Units

Everything may be bits, but it's inconvenient to work with individual 0/1 values. Therefore, CPUs always access and manipulate larger 
groups of bits.

The most important unit is the **byte**, which is defined to be 8 bits. A single byte can encode 256 distinct values. In C, the
`char` data type represents a single 8-bit byte.

Early computers had variable concepts of how large a byte should be, often using size of a single text 
character as the basic unit of access. The industry didn't standardize on the 8-bit byte until IBM introduced the successsful
System/360 mainframe in the 1960's.

A four-bit grouping is called a *nibble*...because it's half of a byte! 

Thank you. I'll be here all week. Tip your waitstaff!

No, seriously. It really is called a nibble. I didn't make that up.

**Kilo, Mega, Giga, Tera and the Rest of the Gang**

If you walk a kilometer you've walked 1000 meters. The prefix *kilo-*, in normal scientific usage, indicates 1000 of a basic unit 
&mdash; kilograms, kilowatts, etc.

Computer engineers decided, however, to use the prefix *kilo-* represent 2^10 (1024). Therefore, a kilobyte (KB) is 1024 bytes, *not* 
1000. This could be justified because computer design and powers of 2 are intimately linked.

The same rule applies to the standard higher prefixes:

 - a megabyte (MB) is 2^20 bytes
 - a gigabyte (GB) is 2^30 bytes
 - a terabyte (TB) is 2^40 bytes
 - a petabyte (PB) is 2^50 bytes
 - an exabyte (EB) is 2^60 bytes
 - a zettabyte (ZB) is 2^70 bytes
 - a yottabyte (YB) is 2^80 bytes

Recall that 2^20 is about 5% larger than 1 million, 2^30 is about 7.5% larger than 1 billion, and 2^40 is almost 10% larger than 1 
trillion.

For context, a typical modern system might have 2, 4, or 8 GB of main memory avaiable. A consumer-grade hard disk is about 1 TB. 
Large-scale datacenters, like the kind used at Google and Facebook, may store petabytes of information.

**Nothing Is Easy**

Beyond the fundamental confusion of using definitions that are different from the rest of the scientific world, there are a few 
complications in working with bits and bytes that you need to be aware of.

  1.  Bits vs. Bytes. In most cases, a lowercase *b* in a unit indicates that it represents *bits* instead of *bytes*. Bit-based units
  of Kb, Mb, or Gb are typically used for data transfer rates, while byte-based units are used for file sizes and storage capacities. 
  For example, you might transfer a 1 MB web page over a 10 Mb/s ethernet link. Generations of students have forgotten this fact and 
  failed their networking exams!

  2. In the late 1990's, the International Electrotechnical Commission (IEC), a standards body, got fed up with the whole "kilo- is 
  1024" thing and introduced new units to refer to power-of-2 based groupings. In their system, 2^10 bytes is a *kibibyte* (KiB), 2^20
  is a *mebibyte* (MiB), and 2^30 is a *gibibyte* (GiB). 
   
  These units never really caught on with most of the industry&mdash;partly because "kibibyte" is just a ridiculously twee thing to 
  say&mdash;but you'll see them from time to time on StackOverflow and other Internet resources.
  
  3. *The capitalist system is lying to you*. Storage manufactuers have long labeled their products using the standard 1000-based SI 
  units. A disk labeled and sold as "1 TB" might hold 1 trillion bytes, but that's about 10% smaller than a true 2^40 byte TB.

  This interaction of marketing terms and technical device sizing can get quite convoluted. For example, the old 1.44 MB floppy disks
  held neither 1.44 * 2^20 bytes nor 1.44 million bytes. Their actual storage capacity was 1.44 thousand KB, that is, 1440 * 2^10
  bytes. You could also call it 1.44 kilokibibytes if you prefer that, you rascal.
