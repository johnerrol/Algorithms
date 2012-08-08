def  LinearSearch(Dataset,keyword):
    for Data in Dataset:
        if(Data.lower()==keyword.lower()):
            return True
    return False  
Dataset=["Arc","Ball","Court"]
sentence=["i lost my ball"]
sentence=mylist.stringsplit()
result=LinearSearch(Dataset,"Ball")
print(result)    
