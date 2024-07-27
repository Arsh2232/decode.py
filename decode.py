def decode(numbers, message_file):
    # Initialize an empty dictionary to store words corresponding to numbers
    word_dict = {}

    # Read the contents of the file
    with open(message_file) as file:
        # Iterate through each line of the pyramid
        for line in file:
            # Split each line into number and word
            num, word = line.strip().split()
            # Convert number to integer
            num = int(num)
            # Store the word in the dictionary with the number as key
            word_dict[num] = word

    # Initialize an empty list to store the decoded words
    decoded_words = []

    # Iterate through the numbers entered by the user
    for num in numbers:
        # Check if the number is in the word dictionary
        if num in word_dict:
            # Append the word corresponding to the number to the decoded words list
            decoded_words.append(word_dict[num])

    # Join the decoded words into a single string
    decoded_message = ' '.join(decoded_words)

    return decoded_message

# Get user input
#for instance, enter 63 35 82
user_input = input("Enter numbers separated by spaces: ").strip().split()
# Convert user input to a list of integers becacuse even though split method return a list, items in it are still strings
user_numbers = [int(num) for num in user_input]

# Test the function with the user's input and the provided example file
print(decode(user_numbers, "letters.txt"))  # Replace "message_file.txt" with the actual path to your input file