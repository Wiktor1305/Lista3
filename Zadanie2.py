import base64

def encrypt_base64(text):
    text_bytes = text.encode('utf-8')
    encoded_text = base64.b64encode(text_bytes)
    return encoded_text.decode('utf-8')

#Przykład:
original_text = "Wiktor_Skowronski"
print(original_text)
encrypted_text = encrypt_base64(original_text)
print(encrypted_text)

#Odszyfrowanie:
decoded_text = base64.b64decode(encrypted_text).decode('utf-8')
print(decoded_text)