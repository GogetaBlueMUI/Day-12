def converstion(arr1):
    intarr=[]
    errorarr=[]
    for i in arr1:
        try:
            value=int(i)
            intarr.append(value)
        except:
            errorarr.append(i)
    print("Converted: ", intarr)
    print("Error list: ", errorarr)
arr1=[]
while True:
    str=input("Enter strings: 'done' to commence ")
    if str=='done':
        break
    arr1.append(str)    
    
converstion(arr1)