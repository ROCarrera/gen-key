import secrets

# Input the length of the key
key_length = int(input("Enter the length of the key: "))
generated_key = secrets.token_urlsafe(key_length)
print("The generated key is: ", generated_key)
