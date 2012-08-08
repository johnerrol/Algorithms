def  LinearSearch(Dataset,keyword):
    for Data in Dataset:
        if(Data.lower()==keyword.lower()):
            return True
    return False  
Dataset=["Arc","Ball","Court"]
result=LinearSearch(Dataset,"Ball")
print(result)    
