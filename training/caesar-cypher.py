def solve_caesar(ciphertext):
    for shift in range(1,26):
        plainttext = []
        for char in ciphertext:
            if 'a' <= char <= 'z':
                base = ord('a')
                decrypted_char = chr((ord(char) - base - shift) % 26 + base)
                plainttext.append(decrypted_char)
            elif 'A' <= char <= 'Z':
                base = ord('A')
                decrypted_char = chr((ord(char) - base - shift) % 26 + base)
                plainttext.append(decrypted_char)
            else:
                plainttext.append(char)

        result = "".join(plainttext)

        marker = " [!] KEMUNGKINAN FLAG" if "picoCTF" in result else ""
        print(f"ROT {shift:2d}: {result}{marker}")

ciphertext_contoh = "cvpbPGS{Eriref1at_g3kg_Ge4afs0ez@g10af_0rn42pq0}"
solve_caesar(ciphertext_contoh)
        
    

