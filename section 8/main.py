alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, original_text, shift_amount):
    result = ""
    if direction == 'decode':
        shift_amount *= -1
    
    for letter in original_text:
        if letter not in alphabet:
            result += letter
        else:
            shifted_amount = alphabet.index(letter)
            shifted_amount = shifted_amount + shift_amount
            shifted_amount %= len(alphabet)
            result += alphabet[shifted_amount]
    print(f"Your {direction}d result is: {result}\n")

is_continue = True

while is_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type your message here: \n").lower()
    shift = int(input("Type the shift number: \n"))

    caesar(direction, text, shift)
    answer = input("Do you want to stop the program? y / n\n").lower()
    if answer == 'y':
        is_continue = False