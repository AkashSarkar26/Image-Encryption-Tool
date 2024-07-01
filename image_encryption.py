from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os
from PIL import Image
import io

# Function to read image as bytes
def read_image(file_path):
    with open(file_path, 'rb') as f:
        return f.read()

# Function to write bytes as image
def write_image(file_path, data):
    with open(file_path, 'wb') as f:
        f.write(data)

# AES Encryption
def aes_encrypt_image(file_path, key):
    data = read_image(file_path)
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    iv = cipher.iv
    encrypted_data = iv + ct_bytes
    write_image(file_path + ".enc", encrypted_data)
    return file_path + ".enc"

# AES Decryption
def aes_decrypt_image(file_path, key):
    with open(file_path, 'rb') as f:
        ciphertext = f.read()
    iv = ciphertext[:16]
    ct = ciphertext[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    decrypted_file_path = file_path.replace('.enc', '.dec')
    write_image(decrypted_file_path, pt)
    return decrypted_file_path

# Generate random key for AES
def generate_aes_key():
    return get_random_bytes(16)
