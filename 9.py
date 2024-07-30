def split_and_join(input_string, delimiter1, delimiter2):
    # Split the input string by the first delimiter
    words = input_string.split(delimiter1)
    
    # Filter words that meet the condition (length > 3)
    filtered_words = [word for word in words if len(word) > 3]
    
    # Join the filtered words with the second delimiter
    result = delimiter2.join(filtered_words)
    
    return result

# Example usage
input_string = input("Enter a string: ")
delimiter1 = ","
delimiter2 = "-"

# Output the result
print("Result:", split_and_join(input_string, delimiter1, delimiter2))
