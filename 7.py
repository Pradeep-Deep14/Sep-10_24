L=[1,1,2,2,3,3,4]
element_count={}

def count_of_elements(L):
    for i in L:
        if i in element_count:
            element_count[i]+=1
        else:
            element_count[i]=1
    return element_count

element_count=count_of_elements(L)

for element,count in element_count.items():
    print(f"The count of {element}: {count}")