import cv2
import os
from tkinter import messagebox

def bits_to_int(bits):
    return int("".join(str(b) for b in bits), 2)

def bits_to_str(bits):
    return "".join(chr(int("".join(str(b) for b in bits[i:i+8]), 2)) for i in range(0, len(bits), 8))

def decrypt(passcode):
    """Decrypt the hidden message from the image."""
    folder = r"C:\Users\Home\Downloads\steganography tool"
    img_path = os.path.join(folder, "encryptedpic.png")
    
    if not os.path.exists(img_path):
        return messagebox.showerror("Error", "Encrypted image not found!")
    
    image = cv2.imread(img_path)
    if image is None:
        return messagebox.showerror("Error", "Failed to load encrypted image!")
    
    flat = image.flatten()
    
    # Retrieve passcode length (first 16 bits)
    p_len = bits_to_int([flat[i] & 1 for i in range(16)])
    start = 16
    embedded_code = bits_to_str([flat[i] & 1 for i in range(start, start + p_len * 8)])
    start += p_len * 8
    
    # Retrieve secret message length (next 32 bits)
    s_len = bits_to_int([flat[i] & 1 for i in range(start, start + 32)])
    start += 32
    secret = bits_to_str([flat[i] & 1 for i in range(start, start + s_len * 8)])
    
    if passcode == embedded_code:
        messagebox.showinfo("Decryption Result", secret)