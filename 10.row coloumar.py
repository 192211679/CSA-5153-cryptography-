import math

key = "HACK"

# Encryption
def encryptMessage(msg):
    cipher = ""
    # Track key indices
    k_indx = 0

    msg_len = len(msg)
    msg_lst = list(msg)
    key_lst = sorted(list(key))

    # Calculate column of the matrix
    col = len(key)
    # Calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))

    # Add the padding character '_' in empty cells of the matrix
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)

    # Create Matrix and insert message and padding characters row-wise
    matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]

    # Read matrix column-wise using key
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] for row in matrix])
        k_indx = (k_indx + 1) % col

    return cipher

# Decryption
def decryptMessage(cipher):
    msg = ""
    # Track key indices
    k_indx = 0
    # Track msg indices
    msg_indx = 0

    msg_len = len(cipher)
    msg_lst = list(cipher)

    # Calculate column of the matrix
    col = len(key)
    # Calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))

    # Convert key into list and sort alphabetically
    key_lst = sorted(list(key))

    # Create an empty matrix to store deciphered message
    dec_cipher = []
    for _ in range(row):
        dec_cipher.append([''] * col)

    # Arrange the matrix column wise according to permutation order
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx = (k_indx + 1) % col

    # Convert decrypted msg matrix into a string
    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot handle repeating words.")

    # Remove padding characters ('_')
    null_count = msg.count('_')
    if null_count > 0:
        return msg[:-null_count]

    return msg

# Driver Code
if __name__ == "__main__":
    msg = "Geeks for Geeks"
    cipher = encryptMessage(msg)
    print("Encrypted Message:", cipher)
    decrypted_msg = decryptMessage(cipher)
    print("Decrypted Message:", decrypted_msg)
