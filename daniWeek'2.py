def validasi_isbn(isbn):
    if len(isbn) != 10 or any(c not in "0123456789X" for c in isbn):
        return "Error: Invalid ISBN format."

    ceksum = 0
    for i in range(10):
        value = 10 if isbn[i] == 'X' else int(isbn[i])
        ceksum += (i + 1) * value

    return "Valid ISBN." if ceksum % 11 == 0 else "Invalid ISBN."

isbn = input("Masukkan ISBN-10: ")
print(validasi_isbn(isbn))