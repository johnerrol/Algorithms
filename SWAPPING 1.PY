Dataset=["ABS-CBN","GMA","RNP"]
IndexToSwap1=0
IndexToSwap2=2

temp=Dataset[IndexToSwap1]
Dataset[IndexToSwap1]=Dataset[IndexToSwap2]
Dataset[IndexToSwap2]=temp



print(Dataset)
