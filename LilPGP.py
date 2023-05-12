# =================================================================================================
#
# LilPGP
#
# A super-simple Python script with PGP functionality, engineered utilizing ChatGPT.
#
# =================================================================================================

import os
import gnupg
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# =================================================================================================

class LilPGP:
    def __init__(self, master):
        self.master = master
        self.gpg = gnupg.GPG()
        
# =================================================================================================
# GUI Magick

        # Primary interface stuffs
        self.master.title("LilPGP")
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)

        # Secret key section
        self.create_key_frame = tk.LabelFrame(master, text="Create secret key")
        self.create_key_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.name_label = tk.Label(self.create_key_frame, text="Name")
        self.name_label.grid(row=0, column=0, sticky="w", padx=5)
        self.name_entry = tk.Entry(self.create_key_frame, width=25)
        self.name_entry.grid(row=1, column=0, padx=5, pady=5)
        self.email_label = tk.Label(self.create_key_frame, text="Email")
        self.email_label.grid(row=2, column=0, sticky="w", padx=5)
        self.email_entry = tk.Entry(self.create_key_frame, width=25)
        self.email_entry.grid(row=3, column=0, padx=5, pady=5)
        self.passphrase_label = tk.Label(self.create_key_frame, text="Passphrase")
        self.passphrase_label.grid(row=4, column=0, sticky="w", padx=5)
        self.passphrase_entry = tk.Entry(self.create_key_frame, width=25, show="*")
        self.passphrase_entry.grid(row=5, column=0, padx=5, pady=5)
        self.create_key_button = tk.Button(self.create_key_frame, text="Create Key", command=self.create_key)
        self.create_key_button.grid(row=6, column=0, sticky="w", columnspan=2, padx=5, pady=5)
        
        # Export public key section
        self.export_key_frame = tk.LabelFrame(master, text="Export public key")
        self.export_key_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        self.key_listbox = tk.Listbox(self.export_key_frame, width=50)
        self.key_listbox.grid(row=0, column=0, padx=5, pady=5)
        self.export_button = tk.Button(self.export_key_frame, text="Export Key", command=self.export_key)
        self.export_button.grid(row=0, column=1, padx=5, pady=5)
        self.refresh_keys()
        
        # Public key selection section
        self.public_key_frame = tk.LabelFrame(master, text="Select public key")
        self.public_key_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        self.public_key_entry = tk.Entry(self.public_key_frame, width=25)
        self.public_key_entry.grid(row=0, column=0, padx=5, pady=5)
        self.public_key_button = tk.Button(self.public_key_frame, text="Select Key", command=self.select_public_key_file)
        self.public_key_button.grid(row=0, column=1, padx=5, pady=5)

        # Encryption/Decryption section
        self.encryption_frame = tk.LabelFrame(master, text="Encryption/Decryption")
        self.encryption_frame.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
        self.directory_entry = tk.Entry(self.encryption_frame)
        self.directory_entry.grid(row=0, column=0, padx=5, pady=5)
        self.directory_button = tk.Button(self.encryption_frame, text="Select Directory", command=self.browse_directory)
        self.directory_button.grid(row=0, column=1, padx=5, pady=5)
        self.encrypt_button = tk.Button(self.encryption_frame, text="Encrypt Directory", command=self.encrypt_directory)
        self.encrypt_button.grid(row=1, column=0, padx=5, pady=5)
        self.decrypt_button = tk.Button(self.encryption_frame, text="Decrypt Directory", command=self.decrypt_directory)
        self.decrypt_button.grid(row=1, column=1, padx=5, pady=5)
        
        # Feedback message area
        self.message_frame = tk.LabelFrame(master, text="Message Log")
        self.message_frame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.message_area = tk.Text(self.message_frame, height=5)
        self.message_area.pack(fill=tk.BOTH, expand=True)
        
# =================================================================================================
# Display feedback messages
      
    def display_message(self, message):
        self.message_area.insert(tk.END, message + "\n")
        self.message_area.see(tk.END)        

# =================================================================================================
# Create a secret key

    def create_key(self):
            name = self.name_entry.get()
            email = self.email_entry.get()
            passphrase = self.passphrase_entry.get()
            input_data = self.gpg.gen_key_input(key_type="RSA", key_length=2048, name_real=name, name_email=email, passphrase=passphrase)
            key = self.gpg.gen_key(input_data)
            self.refresh_keys()
            self.display_message(f"Key created with fingerprint {key.fingerprint}")

    def refresh_keys(self):
        self.key_listbox.delete(0, tk.END)
        keys = self.gpg.list_keys()
        for key in keys:
            self.key_listbox.insert(tk.END, key['uids'])
            
# =================================================================================================
# Export a public key from a selected secret key

    def export_key(self):
        selected_key = self.key_listbox.get(tk.ANCHOR)
        ascii_armored_public_keys = self.gpg.export_keys(selected_key)
        file_path = filedialog.asksaveasfilename(defaultextension=".asc")
        if file_path:
            with open(file_path, 'w') as f:
                f.write(ascii_armored_public_keys)
            self.display_message(f"Key exported successfully.")
        else:
            self.display_message(f"Export cancelled.")

    def select_public_key_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.public_key_entry.delete(0, tk.END)
            self.public_key_entry.insert(0, file_path)
            
# =================================================================================================
# Selecting, encrypting, and decrypting directories
        
    def browse_directory(self):
        directory = filedialog.askdirectory()
        self.directory_entry.delete(0, tk.END)
        self.directory_entry.insert(0, directory)
   
    def encrypt_directory(self):
        public_key_file = self.public_key_entry.get()
        directory = self.directory_entry.get()

        script_dir = os.path.dirname(os.path.realpath(__file__))
        encrypted_dir = os.path.join(script_dir, 'encrypted')

        if not os.path.isdir(encrypted_dir):
            os.mkdir(encrypted_dir)

        with open(public_key_file, 'r') as f:
            key_data = f.read()
        import_result = self.gpg.import_keys(key_data)
        
        if import_result.count != 1:
            self.display_message(f"Error importing key from {public_key_file}")
            return

        key_id = import_result.fingerprints[0]
        
        for filename in os.listdir(directory):
            with open(os.path.join(directory, filename), 'rb') as f:
                status = self.gpg.encrypt_file(
                    f, recipients=[key_id],
                    output=os.path.join(script_dir, 'encrypted', filename + '.gpg'))

            if status.ok:                
                self.display_message(f"Encryption of {filename} was successful.")
            else:
                self.display_message(f"Encryption of {filename} failed: {status.status}")

    def decrypt_directory(self):
        selected_key = self.key_listbox.get(tk.ANCHOR)[0]
        directory = self.directory_entry.get()

        script_dir = os.path.dirname(os.path.realpath(__file__))
        decrypted_dir = os.path.join(script_dir, 'decrypted')

        if not os.path.isdir(decrypted_dir):
            os.mkdir(decrypted_dir)
        for filename in os.listdir(directory):
            with open(os.path.join(directory, filename), 'rb') as f:
                status = self.gpg.decrypt_file(
                    f, output=os.path.join(script_dir, 'decrypted', filename.replace('.gpg', '')))

            if status.ok:
                self.display_message(f"Decryption of {filename} was successful.")
            else:
                self.display_message(f"Decryption of {filename} failed: {status.status}")
                
# =================================================================================================
# Get on with that main loop

if __name__ == "__main__":
    root = tk.Tk()
    app = LilPGP(root)
    root.mainloop()

# === EOF =========================================================================================
