def create_matrix_from(key):
    # Initialize a 3x3 matrix filled with 0s
    m = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            m[i][j] = ord(key[3 * i + j]) % 65
    return m

def encrypt(P, K):
    C = [0, 0, 0]
    for i in range(3):
        C[i] = (K[i][0] * P[0] + K[i][1] * P[1] + K[i][2] * P[2]) % 26
    return C

def hill(message, K):
    cipher_text = []
    for i in range(0, len(message), 3):
        P = [0, 0, 0]
        for j in range(3):
            if i + j < len(message):
                P[j] = ord(message[i + j]) % 65
        C = encrypt(P, K)
        for j in range(3):
            cipher_text.append(chr(C[j] + 65))
    return "".join(cipher_text)

def matrix_inverse(K):
    # Calculate the determinant of K
    det = K[0][0] * (K[1][1] * K[2][2] - K[1][2] * K[2][1]) \
          - K[0][1] * (K[1][0] * K[2][2] - K[1][2] * K[2][0]) \
          + K[0][2] * (K[1][0] * K[2][1] - K[1][1] * K[2][0])
    
    # Calculate the determinant modulo 26
    det = det % 26
    
    # Find the multiplicative inverse of det modulo 26
    det_inv = None
    for i in range(26):
        if (det * i) % 26 == 1:
            det_inv = i
            break
    
    if det_inv is None:
        raise ValueError("Matrix is not invertible")
    
    # Calculate the adjugate matrix
    adj = [[0] * 3 for _ in range(3)]
    adj[0][0] = (K[1][1] * K[2][2] - K[1][2] * K[2][1]) % 26
    adj[0][1] = (K[0][2] * K[2][1] - K[0][1] * K[2][2]) % 26
    adj[0][2] = (K[0][1] * K[1][2] - K[0][2] * K[1][1]) % 26
    adj[1][0] = (K[1][2] * K[2][0] - K[1][0] * K[2][2]) % 26
    adj[1][1] = (K[0][0] * K[2][2] - K[0][2] * K[2][0]) % 26
    adj[1][2] = (K[0][2] * K[1][0] - K[0][0] * K[1][2]) % 26
    adj[2][0] = (K[1][0] * K[2][1] - K[1][1] * K[2][0]) % 26
    adj[2][1] = (K[0][1] * K[2][0] - K[0][0] * K[2][1]) % 26
    adj[2][2] = (K[0][0] * K[1][1] - K[0][1] * K[1][0]) % 26
    
    # Calculate K_inv as (det_inv * adj) % 26
    K_inv = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            K_inv[i][j] = (det_inv * adj[j][i]) % 26
    
    return K_inv

if __name__ == "__main__":
    message = "MYSECRETMESSAGE"
    key = "RRFVSVCCT"
    K = create_matrix_from(key)
    print("Key Matrix:")
    for row in K:
        print(row)
    
    cipher_text = hill(message, K)
    print('Cipher text:', cipher_text)
    
    try:
        K_inv = matrix_inverse(K)
        print("Inverse Key Matrix:")
        for row in K_inv:
            print(row)
        
        plain_text = hill(cipher_text, K_inv)
        print('Plain text:', plain_text)
    except ValueError as e:
        print("Error:", e)
