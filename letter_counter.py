#No external library needed
#Simple Letter Counter using len()
#This program counts how many letters are in your text

print("=== LETTER COUNTER ===")
text = input("Enter your text: ")

# Count only letters using len()
# Filter the numbers and caracters .isalpha
# Run the text and extract the letters
letters = [char for char in text if char.isalpha()]

#count the numbers of letters inside 
total_letters = len(letters)

print(f"\nYour text: '{text}'")
print(f"Total letters: {total_letters}")
