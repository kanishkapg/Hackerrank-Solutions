import textwrap

def wrap(string, max_width):
    temp = []
    for i in range(0, len(string), 4):
        temp.append(string[i:(i+max_width)])
        
    return '\n'.join(temp)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)