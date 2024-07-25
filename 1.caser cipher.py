def encrypt_text(plaintext, n):
    ans = ""
    # iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]
        # check if space is there then simply add space
        if ch == " ":
            ans += " "
        # check if a character is uppercase then encrypt it accordingly
        elif ch.isupper():
            ans += chr((ord(ch) + n - 65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly
        elif ch.islower():
            ans += chr((ord(ch) + n - 97) % 26 + 97)
        else:
            # if character is neither uppercase nor lowercase (e.g., punctuation), keep it unchanged
            ans += ch
    return ans

# Example usage:
plaintext = "HELLO EVERYONE"
n = 1
print("Plain Text is : " + plaintext)
print("Shift pattern is : " + str(n))
print("Cipher Text is : " + encrypt_text(plaintext, n))
