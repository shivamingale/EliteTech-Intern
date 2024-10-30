from PIL import Image
import numpy as np

def encrypt_image(image_path, shift_value, output_path):
    image = Image.open(image_path)
    image_data = np.array(image)

    # Encrypt by shifting pixel values
    encrypted_data = (image_data + shift_value) % 256  # Ensures values stay in 0-255 range
    encrypted_image = Image.fromarray(encrypted_data.astype('uint8'))
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, shift_value, output_path):
    image = Image.open(image_path)
    image_data = np.array(image)

    # Decrypt by reversing the shift
    decrypted_data = (image_data - shift_value) % 256
    decrypted_image = Image.fromarray(decrypted_data.astype('uint8'))
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

def main():
    print("Image Encryption Tool")
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt an image: ").strip().lower()
    image_path = input("Enter the path to the image: ")
    shift_value = int(input("Enter a shift value (e.g., 50): "))
    output_path = input("Enter the path for the output image: ")

    if choice == 'encrypt':
        encrypt_image(image_path, shift_value, output_path)
    elif choice == 'decrypt':
        decrypt_image(image_path, shift_value, output_path)
    else:
        print("Invalid choice. Please choose either 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
