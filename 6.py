def subtration(arr1):
    size=(len(arr1))
    if size < 2:
        print("Array must have at least two elements to do subtraction.")
        return
    for i in range (size-1):
        sub=arr1[i+1] - arr1[i]
        if arr1[i+1]>arr1[i]:
            print("First digit is larger than the second.") 
        print(f"Result of: {arr1[i+1]} and {arr1[i]} = {sub}")       
arr1=[]
while True:
    value=input("Enter number: 'done' to commence  ")
    if(value=='done'):
        break
    value1=int(value)
    arr1.append(value1)
subtration(arr1)