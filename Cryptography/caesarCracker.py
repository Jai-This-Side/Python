def caesarBruteForce(cipherText):
    for key in range(1, 26):
        decrypted = ""

        for char in cipherText:
            if char.isalpha():
                shift = key
                base = ord('A') if char.isupper() else ord('a')
                decrypted += chr((ord(char)- base - shift)%26 + base)

            else:
                decrypted += char

        print(f"key{key:2}: {decrypted}")

cipherText = "wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj"
caesarBruteForce(cipherText)