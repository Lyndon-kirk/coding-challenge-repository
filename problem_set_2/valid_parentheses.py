def isValid(symbol: str):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    for s in symbol:
        if s in bracket_map:
            top_element = stack.pop() if stack else '#'
            if bracket_map[s] != top_element:
                return False
        else:
            stack.append(s)

    return not stack #returns true if stack is empty

def main(): 
    #Tests
    input_string1 = "([])"
    input_string2 = "([]"
    input_string3 = "()[]{}"
    #call function
    result1 = isValid(input_string1)
    result2 = isValid(input_string2)
    result3 = isValid(input_string3)
    
    print(f"Input: {input_string1}, Output: {result1}")  # Output: True
    print(f"Input: {input_string2}, Output: {result2}")  # Output: False
    print(f"Input: {input_string3}, Output: {result3}")  # Output: True

main()
