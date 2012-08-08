def  LinearSearch(Dataset,keyword):
    for Data in Dataset:
        if(Data==keyword):
            return True
    return False  
Dataset=["Are","Ball","Court"]
result=LinearSearch(Dataset,"Ball")
print(result)

    
