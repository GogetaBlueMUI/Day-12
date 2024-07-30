def check(s):
    cleaned=""
    for char in s:
        if char.isalnum():
            cleaned+=char
    palindrome=True
    empty=""
    for char in s:
        empty=char+empty
    if empty==s:
        palindrome=True
    else:
        palindrome=False
    frequency = {}
    for char in cleaned:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    print(f"Palindrome status:{palindrome}   Frequencies: {frequency}")
str=input("Enter a string: ")
check(str)