#kelime karistirma

#ankara--> kaarna ---> True False turns


def HarfKar(str1,str2):
    #str2 ' deki harfe erisim'
    #check str1
    #true or false?
    
    for i in str2:
        if i not in str1:
            return False
        
        return True
        
print(HarfKar("ankara","karana"))




#%%karistiran yazalim:
"""import random     
def kar(str1):
   
    return random.shuffle(str1)

print(kar("kar"))

it's error!!!
"""



a="istanbul"
b=list(a)
random.shuffle(b)
fin="".join(b)
print(fin)

#fonk- format

def kars(stra):
    b=list(stra)
    random.shuffle(b)
    fin="".join(b)
    return fin

print(kars("berlin"))
    
    
    
    
    
        
        
            