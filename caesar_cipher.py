def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("Caesar Cipher Program")
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (e.g., 3): "))

    if choice == 'encrypt':
        encrypted_message = caesar_encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")
    elif choice == 'decrypt':
        decrypted_message = caesar_decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")
    else:
        print("Invalid choice. Please choose either 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
