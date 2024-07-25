def separate_same_letters(message):
    index = 0
    while index < len(message):
        l1 = message[index]
        if index == len(message) - 1:
            message = message + 'X'
            index += 2
            continue
        l2 = message[index + 1]
        if l1 == l2:
            message = message[:index + 1] + "X" + message[index + 1:]
            index += 2
        else:
            index += 2
    return message

# Example usage
plaintext = "BALLOON"
processed_text = separate_same_letters(plaintext)
print("Processed Text: ", processed_text)
