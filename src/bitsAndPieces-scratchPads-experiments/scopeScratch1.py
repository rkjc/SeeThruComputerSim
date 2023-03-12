# incase anyone has forgotten *cough, cough ... like me* 

zork = 987
blat = 645

def outer():
    def change():
        nonlocal zork
        zork = 333
        print('after in def', zork)
    zork = "wow"
    change()

print('before call', zork)

outer()

print('after call', zork)
