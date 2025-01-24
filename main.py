# read file into python and print to terminal
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
 #   print (file_contents)
    print ("--- Begin report of books/frankenstein.txt ---")
    words = file_contents.split()
    print (len(words))
    count_chars = file_contents.lower()    
    char_count = {}
    for char in count_chars:
        if char.isalpha():  # This ensures we count only alphabetic characters
            if char in char_count:
                char_count[char] += 1  # Increment count if the character is already in the dictionary
            else:
                char_count[char] = 1  # Initialize count if the character is not in the dictionary


    for c in char_count:
        print(f"the '{c}' character was found {char_count[c]} times")
    print ("--- End report ---")



main()