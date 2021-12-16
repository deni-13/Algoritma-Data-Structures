#kayip basamak

"""

"10-x=4"
x ' i bul tarzi 
1x*11=121---> x kayip basamak
x=1 
x'i bul'
"""

def kayip(string):
    #x bul ---> plan
    #bul = 
    #='den next and back compare by eval
    #return
    
    for i in range(10):
        c=string.replace("x",str(i))
        x=string.index("=")
        if eval(c[:x]) ==eval(c[x+1]):
            return str(i)
        
print(kayip("10-x=4"))
print(kayip("1x-12=144"))


        
        
        