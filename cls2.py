plain_text=input("enter plain text:")
key=int(input("enter key value:"))
cipher_text=""
for i in plain_text:
    ordvalue=ord(i)
    ciphervalue=ordvalue+key
    cipher_text+=chr(ciphervalue)
print(cipher_text)
