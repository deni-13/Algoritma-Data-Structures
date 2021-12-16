#array rotasyonu

#a=[2,3,4,5]
#out: 4523
#ilk eleman index kabul et ve indexe git ordan dvm ve don

# def arrayRotation(str1):
#     list_str1 = str1.split(",")
#     list_first_element = list_str1[0]
#     list_first_element = int(list_first_element)
#     list_first_part = list_str1[:list_first_element]
#     list_last_part = list_str1[list_first_element:]
#     new_list = list_last_part + list_first_part
#     new_list = "".join(new_list)
#     return new_list
 
# str1 = input("list:")
# print(arrayRotation(str1)) 


#%%

#array baslangic bul
#output array bul
#while ve counter

bos=[]
def rot(l):
    global bos
    for i in l:
        bos.append(l[0])
    
        
        
# print(rot([2,3,56]))

#%%
def myFunc(arr):
    firstElem = arr[0]
    length = len(arr)
    rightSide = arr[firstElem:length]
    leftSide = arr[:firstElem]
    rightSide.extend(leftSide)
    result = "".join(map(str, rightSide))
    print(result)
print(myFunc([1,3,5,7]))