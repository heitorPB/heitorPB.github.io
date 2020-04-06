---
author: Heitor
categories: [random]
localimage:
language: [english]
layout: post
tags: [linux, random]
title: Random numbers from /dev/urandom in Bash
---

In a GNU/Linux distributions, there are special files (`/dev/random` and
`/dev/urandom`) to access the kernel's random number generator. But how
do we get random numbers from them in a bash script?

If we try to `cat` them we get random things:

~~~ julia
$ cat /dev/random
XB>7;Mq'\'$,dH՞ՈT=H}0]eS19Ѡ
Hd9)7ܢVO'y.ۧMW^C
~~~

Something a bit weirder happens with `/dev/urandom`: it continues vomiting
characters at you until you stop it with `Ctrl + C`.

What's the difference between `/dev/random` and `/dev/urandom`? Lets check the
manpage for `urandom`, as of Linux 5.5:


       The  random number generator gathers environmental noise from device driv‐
       ers and other sources into an entropy pool.  The generator also  keeps  an
       estimate  of  the  number of bits of noise in the entropy pool.  From this
       entropy pool, random numbers are created.

       When read, the /dev/urandom device returns random bytes using a pseudoran‐
       dom number generator seeded from the entropy pool.  Reads from this device
       do not block (i.e., the CPU is not yielded), but can incur an  appreciable
       delay when requesting large amounts of data.

       The  /dev/random  device  is a legacy interface which dates back to a time
       where  the  cryptographic  primitives  used  in  the   implementation   of
       /dev/urandom  were  not  widely trusted.  It will return random bytes only
       within the estimated number of bits of fresh noise in  the  entropy  pool,
       blocking if necessary.  /dev/random is suitable for applications that need
       high quality randomness, and can afford indeterminate delays.

       When the entropy pool is empty, reads from /dev/random  will  block  until
       additional  environmental  noise  is  gathered.

From this, we get that:

- the Kernel maintains a pool of entropy from random things that happens in the
  computer.
- both special files use this entropy pool to seed a PRNG.
- `/dev/random` waits until there are enough randomness to output something.
- `/dev/urandom` is preferred.
- both files gives us _bytes_.

We now need a tool to read a specific number of bytes from those files and
convert it to something human readable. And here comes `od`[^od], a Unix
command to display data in several formats. The default is octal, hence the
name `od`: _octal dump_.

With this uttility we can read `N` bytes from a file and display it in a
specified format. For example, here's the dump of `Hello World":

``` julia
$ echo Hello World | od
0000000 062510 066154 020157 067527 066162 005144
0000014
```

The first column is the offset, and then the octal representation of that line.
So, the second line of the output means: starting at the offset `0000014` we
have nothign, i.g. there are 14 (in octal, or 12 in decimal) characters in that
string.

It looks like `od` does not know how to count. There are 11 chars in `Hello
World`! Lets see each char individually (`-c`) in octal (`-b`):

``` julia
echo "Hello World" | od -cb
0000000   H   e   l   l   o       W   o   r   l   d  \n
        110 145 154 154 157 040 127 157 162 154 144 012
0000014
```

Sweet, it counted the line ending as well.

`od` can also read `N` bytes from a source and display it in a speficied
format. So, to read 4 bytes from `/dev/urandom`, display it as an unsigned
integer without the offset column:

``` julia
$ od -vAn -N4 -t u4 < /dev/urandom
  402803061
```





[SOMETHING ABOUT FLOATS]

[CONCLUSIOn]


*[PRNG]: pseudorandom number generator
[^od]: [Gnu Coreutils](https://www.gnu.org/software/coreutils/manual/html_node/od-invocation.html)

### TODO

- get rid of this entire section. The file ends with the footnotes and shit,
  but before this fucking section
- nice text
- hemmingWay check and grammar check and shit like that
- **last** things to do:
  - check for nice title
  - rename file: `_posts/yyyy-mm-dd-title.md` or
    `_posts/yyyy-mm-dd-title/date-title.md`
  - add the first image to the "image" YAML tag
  - check categories and tags and language and YAML shit
  - if new tag: add it to the template also!
  - review first paragraph: first paragraph should be small and summarize everything