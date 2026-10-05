if __name__ == '__main__':
    s = input()
    
    # 1. Alphanumeric check
    found = False
    for i in s:
        if i.isalnum():
            found = True
            break
    print(found)
    
    # 2. Alphabetical check
    found = False
    for i in s:
        if i.isalpha():
            found = True
            break
    print(found)
    
    # 3. Digit check
    found = False
    for i in s:
        if i.isdigit():
            found = True
            break
    print(found)
    
    # 4. Lowercase check
    found = False
    for i in s:
        if i.islower():
            found = True
            break
    print(found)
    
    # 5. Uppercase check
    found = False
    for i in s:
        if i.isupper():
            found = True
            break
    print(found)
