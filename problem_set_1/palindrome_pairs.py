def is_palindrome(s: str):
    # Check if the string is a palindrome
    return s == s[::-1]

def palindrome_pairs(words: list):
    result = []
    #lambda function to map the word
    word_map = {word: i for i, word in enumerate(words)}

    # Check for palindrome pairs
    for i, word in enumerate(words):
        for j in range(len(word) + 1):
            # Split the word into left and right parts
            left = word[:j]
            right = word[j:]

            # Check if left part is a palindrome
            if is_palindrome(left):
                reverse_right = right[::-1]
                if reverse_right in word_map and word_map[reverse_right] != i:
                    result.append([word_map[reverse_right], i])

            # Check if right part is a palindrome
            if j < len(word) and is_palindrome(right):
                reverse_left = left[::-1]
                if reverse_left in word_map and word_map[reverse_left] != i:
                    result.append([i, word_map[reverse_left]])

    return result

def main():
    # Example tests
    input_words1 = ['night', 'time', 'morning']
    input_words2 = ['bat', 'tab']
    input_words3 = ['hello', 'olleh', 'goodbye']

    result1 = palindrome_pairs(input_words1)
    result2 = palindrome_pairs(input_words2)
    result3 = palindrome_pairs(input_words3)

    print(result1)  # output: [] (no palindrome pairs)
    print(result2)  # output: [[1, 0], [0, 1]] 
    print(result3)  # output: [[1, 0], [0, 1]] 

main()
