if __name__ == '__main__':
    s = input()
    
    # 1. Alphanumeric check
    print(any(i.isalnum() for i in s))
    
    # 2. Alphabetical check
    print(any(i.isalpha() for i in s))
    
    # 3. Digit check
    print(any(i.isdigit() for i in s))
    
    # 4. Lowercase check
    print(any(i.islower() for i in s))
    
    # 5. Uppercase check
    print(any(i.isupper() for i in s))