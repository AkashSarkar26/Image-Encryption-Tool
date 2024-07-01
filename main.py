from image_encryption import aes_encrypt_image, aes_decrypt_image, generate_aes_key

def main():
    key = generate_aes_key()
    print(f"Generated AES key: {key}")

    file_path = input("Enter the image file path to encrypt: ")

    # Encrypt the image
    encrypted_file_path = aes_encrypt_image(file_path, key)
    print(f"Encrypted image saved to: {encrypted_file_path}")

    # Decrypt the image
    decrypted_file_path = aes_decrypt_image(encrypted_file_path, key)
    print(f"Decrypted image saved to: {decrypted_file_path}")

if __name__ == "__main__":
    main()
