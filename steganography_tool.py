import tkinter as tk
from tkinter import ttk, messagebox
import cv2
import os
from encrypt import encrypt
from decrypt import decrypt

# -------- GUI Setup --------
root = tk.Tk()
root.title("Steganography Tool")
root.geometry("500x400")
root.resizable(True, True)
root.configure(bg='#2e2e2e')

style = ttk.Style(root)
style.theme_use('clam')
for widget in ['TFrame', 'TNotebook']:
    style.configure(widget, background='#2e2e2e')
style.configure('TLabel', background='#2e2e2e', foreground='white')
style.configure('TButton', background='#3e3e3e', foreground='white')
style.configure('TEntry', fieldbackground='#3e3e3e', foreground='white')
style.configure('TNotebook.Tab', background='#3e3e3e', foreground='white')
style.map('TNotebook.Tab', background=[('selected', '#1e1e1e')])

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# --- Encryption Tab ---
enc_tab = ttk.Frame(notebook, padding="20")
notebook.add(enc_tab, text="Encryption")
ttk.Label(enc_tab, text="Secret Message:").grid(row=0, column=0, sticky="w", pady=5)
enc_secret_message_entry = ttk.Entry(enc_tab, width=50)
enc_secret_message_entry.grid(row=1, column=0, pady=5)
ttk.Label(enc_tab, text="Passcode:").grid(row=2, column=0, sticky="w", pady=5)
enc_passcode_entry = ttk.Entry(enc_tab, width=50, show="*")
enc_passcode_entry.grid(row=3, column=0, pady=5)

def encrypt_message():
    """Retrieve inputs and call the encrypt function."""
    secret = enc_secret_message_entry.get().strip()  # Remove leading/trailing whitespace
    code = enc_passcode_entry.get().strip()  # Remove leading/trailing whitespace

    # Input validation
    if not secret or not code:
        messagebox.showerror("Error", "Both secret message and passcode are required!")
        return

    # Optional: Check for maximum length (example: 100 characters)
    if len(secret) > 100:
        messagebox.showerror("Error", "Secret message is too long! Maximum length is 100 characters.")
        return

    # Call the encrypt function
    encrypt(secret, code)

ttk.Button(enc_tab, text="Encrypt", command=encrypt_message).grid(row=4, column=0, pady=20)

# --- Decryption Tab ---
dec_tab = ttk.Frame(notebook, padding="20")
notebook.add(dec_tab, text="Decryption")
ttk.Label(dec_tab, text="Enter Passcode:").grid(row=0, column=0, sticky="w", pady=5)
dec_passcode_entry = ttk.Entry(dec_tab, width=50, show="*")
dec_passcode_entry.grid(row=1, column=0, pady=5)

def decrypt_message():
    """Retrieve passcode and call the decrypt function."""
    passcode = dec_passcode_entry.get().strip()
    if not passcode:
        messagebox.showerror("Error", "Passcode is required for decryption!")
        return
    decrypt(passcode)

ttk.Button(dec_tab, text="Decrypt", command=decrypt_message).grid(row=2, column=0, pady=20)

# Start the GUI event loop
root.mainloop()