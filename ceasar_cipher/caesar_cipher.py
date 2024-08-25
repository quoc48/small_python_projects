try:
    import pyperclip    # pyperclip copies text to the clipboard.
except ImportError:
    pass    # If pyperclip is not installed, do nothing. It's so big deal.

# Every possible symbol that can be encrypted/decrypted:
# (!) You can add numbers and punctuation marks to encrypt those
# symbol as well.

SYMBOLS = 'ABCDEFGHIJKLMNOPOQRSTUVWXYZ'

# Let the user enter if they are encrypting or decrypting:
while True:     # Keep asking until the user enters e or d.
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d.')

# Let the user enter key to use:
while True: # Keep asking until the user enters a valid key.
    maxKey = len(SYMBOLS) - 1
    print(f'Please enter the key (0 to {maxKey}) to use.')
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 < int(response) < len(SYMBOLS):
        key = int(response)
        break

# Let user enter the message to encrypt/decrypt:
print('Enter the message to {}'.format(mode))
message = input('> ')

# Caesar cipher only works on uppercase letters:
message = message.upper()

# Stores the encrypt/decrypt form of the message:
translated = ''

# Encrypt/Decrypt each symbol in the message:
for symbol in message:
    if symbol in SYMBOLS:
        # Get the encrypt (or decrypt) number for this symbol.
        num = SYMBOLS.find(symbol)  # Get the number of the symbol.
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        # Handle the wrap-around if num is large than length of
        # SYMBOLS or less than 0:
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        # Add encrypted/decrypted number's symbol to translated:
        translated = translated + SYMBOLS[num]
    else:
        # Just add the symbol without encrypting/decrypting:
        translated = translated + symbol

# Display the encrypt/descrypt string to the screen:
print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard.'.format(mode))
except:
    pass    # Do nothing if pyperclip wasn't installed.


