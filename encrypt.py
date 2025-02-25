import cv2
import os
from tkinter import messagebox

def int_to_bits(num, length):
    """Convert an integer to a list of bits."""
    return [int(b) for b in format(num, f'0{length}b')]

def str_to_bits(s):
    """Convert a string to a list of bits."""
    return [int(b) for char in s for b in format(ord(char), '08b')]

def embed_data(img, data_bits):
    """Embed data bits into the image using LSB technique."""
    flat = img.flatten()
    if len(data_bits) > len(flat):
        raise ValueError("Data too large to embed!")
    for i, bit in enumerate(data_bits):
        flat[i] = (flat[i] & 254) | bit  # Set the least significant bit
    return flat.reshape(img.shape)

def encrypt(secret, code):
    """Encrypt the secret message into the image."""
    folder = r"C:\Users\Home\Downloads\steganography tool"
    img_path = os.path.join(folder, "mypic.jpg")
    
    print(f"Looking for image at: {img_path}")  # Debugging output
    if not os.path.exists(img_path):
        print("Image not found!")  # Debugging output
        return messagebox.showerror("Error", "Input image not found!")
    
    image = cv2.imread(img_path)
    if image is None:
        return messagebox.showerror("Error", "Failed to load image!")
    
    if not secret or not code:
        return messagebox.showerror("Error", "Secret message and passcode are required!")
    
    # Create header: [16 bits for code length] + [code] + [32 bits for message length] + [secret]
    header = (
        int_to_bits(len(code), 16) +
        str_to_bits(code) +
        int_to_bits(len(secret), 32) +
        str_to_bits(secret)
    )
    
    try:
        encoded = embed_data(image, header)
    except ValueError as e:
        return messagebox.showerror("Error", str(e))
    
    output_path = os.path.join(folder, "encryptedpic.png")
    cv2.imwrite(output_path, encoded)
    messagebox.showinfo("Success", f"Encryption complete! Output saved to: {output_path}")