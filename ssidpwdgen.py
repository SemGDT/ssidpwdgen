import argparse
from cryptography.fernet import Fernet
import base64
import sys

def generate_fernet_key():
    # Generate a new Fernet key
    return Fernet.generate_key()

def encrypt_data(fernet_key, ssid, wifi_pwd):
    # Create a Fernet cipher using the key
    fernet = Fernet(fernet_key)
    
    # Combine SSID and password as a single string
    data = f"{ssid}:{wifi_pwd}".encode('utf-8')
    
    # Encrypt the data
    encrypted_data = fernet.encrypt(data)
    return encrypted_data

def decrypt_data(fernet_key, encrypted_data):
    # Create a Fernet cipher using the key
    fernet = Fernet(fernet_key)
    
    # Decrypt the data
    decrypted_data = fernet.decrypt(encrypted_data)
    return decrypted_data.decode('utf-8')

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Encrypt your SSID and Wi-Fi password using Fernet encryption.")
    
    # Add arguments for SSID, password, and optional Fernet key
    parser.add_argument("ssid", type=str, help="SSID of the Wi-Fi network.")
    parser.add_argument("wifi_pwd", type=str, help="Wi-Fi password.")
    parser.add_argument("--fernet_key", type=str, help="Optional Fernet key (Base64 encoded). If not provided, a new key will be generated.")

    # Parse arguments
    args = parser.parse_args()

    # Check if ssid and wifi_pwd are provided
    if not args.ssid or not args.wifi_pwd:
        print("Error: SSID and Wi-Fi password must be provided.")
        parser.print_usage()
        sys.exit(1)

    # Use provided Fernet key or generate a new one
    if args.fernet_key:
        try:
            # Decode the provided Fernet key from Base64
            fernet_key = base64.b64decode(args.fernet_key)
            fernet = Fernet(fernet_key)
        except Exception as e:
            print(f"Error: Invalid Fernet key provided. {e}")
            sys.exit(1)
    else:
        # Generate a new Fernet key
        fernet_key = generate_fernet_key()
        fernet = Fernet(fernet_key)

    # Encrypt the SSID and Wi-Fi password
    encrypted_data = encrypt_data(fernet_key, args.ssid, args.wifi_pwd)

    # Encode the Fernet key in Base64 for display
    fernet_key_b64 = base64.b64encode(fernet_key).decode('utf-8')
    encrypted_data_b64 = base64.b64encode(encrypted_data).decode('utf-8')

    # Display the Fernet key and encrypted data in Base64 format
    print("Fernet Key (Base64):", fernet_key_b64)
    print("Encrypted Data (Base64):", encrypted_data_b64)

    # Optionally decrypt the data to verify
    decrypted_data = decrypt_data(fernet_key, encrypted_data)
    print("Decrypted Data:", decrypted_data)

if __name__ == "__main__":
    main()
