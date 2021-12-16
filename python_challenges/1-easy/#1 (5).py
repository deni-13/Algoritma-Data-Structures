#kelime tersi
#en basic *-->
def kel(a):
    return a[::-1]
print(kel("istanbul"))


#%%
def tersi(f):
    ters="" #bos str ile toplamak baska bir yontem!

    ters=ters+f[::-1]
    return ters
print(tersi("istanbul"))
        



#%% 2.methodla ayni
def tersim(a):
    return "".join(reversed(a))


print(tersim("istanbul"))


    
