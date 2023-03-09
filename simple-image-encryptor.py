import os
import argparse
from cryptography.fernet import Fernet


def encrypt_file(file_path: str, password: str) -> None:
    """
    Encrypts a file using the Fernet encryption algorithm.

    Args:
        file_path (str): The path to the file to encrypt.
        password (str): The password to use for encryption.

    Returns:
        None
    """

    # create a Fernet object with the password
    key = password.encode()
    fernet = Fernet(key)

    # read the file as bytes
    with open(file_path, 'rb') as f:
        file_bytes = f.read()

    # encrypt the bytes using Fernet
    encrypted_bytes = fernet.encrypt(file_bytes)

    # write the encrypted bytes to a new file with '_encrypted' appended to the filename
    with open(file_path[:-4]+'_encrypted'+file_path[-4:], 'wb') as f:
        f.write(encrypted_bytes)

def decrypt_file(file_path: str, password: str) -> None:
    """
    Decrypts a file that has been encrypted with the Fernet encryption algorithm.

    Args:
        file_path (str): The path to the file to decrypt.
        password (str): The password used for encryption.

    Returns:
        None
    """

    # create a Fernet object with the password
    key = password.encode()
    fernet = Fernet(key)

    # read the encrypted file as bytes
    with open(file_path, 'rb') as f:
        encrypted_bytes = f.read()

    # decrypt the bytes using Fernet
    decrypted_bytes = fernet.decrypt(encrypted_bytes)

    # write the decrypted bytes to a new file with '_decrypted' appended to the filename
    with open(file_path[:-4]+'_decrypted'+file_path[-4:], 'wb') as f:
        f.write(decrypted_bytes)

def main():
    parser = argparse.ArgumentParser(description='Encrypt or decrypt files.')
    parser.add_argument('folder_path', metavar='folder_path', type=str, help='Path to the folder containing the files')
    parser.add_argument('operation', metavar='operation', type=str, choices=['encrypt', 'decrypt'], help='Operation to perform (encrypt or decrypt)')
    parser.add_argument('-p', '--password', type=str, help='Password for encryption')

    args = parser.parse_args()

    # check if a password was provided for encryption
    if args.operation == 'encrypt' and not args.password:
        raise ValueError('Password is required for encryption')

    # iterate over all files in the folder
    for filename in os.listdir(args.folder_path):
        # check if the file is a PNG image
        if filename.endswith('.png') or filename.endswith('.jpg'):
            file_path = os.path.join(args.folder_path, filename)

            # perform encryption or decryption based on user choice
            if args.operation == 'encrypt':
                encrypt_file(file_path, args.password)
            elif args.operation == 'decrypt':
                decrypt_file(file_path, args.password)

if __name__ == '__main__':
    main()