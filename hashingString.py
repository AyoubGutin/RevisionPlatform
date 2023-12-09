import hashlib

password = "password123"
passwordHash = hashlib.md5(password.encode())
hash_as_string = passwordHash.hexdigest()
print(hash_as_string)
