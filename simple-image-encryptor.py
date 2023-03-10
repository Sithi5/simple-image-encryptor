from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import os
import argparse
import getpass
from logger.Logger import Logger

logger = Logger(level="INFO", display_date=False, colors=True, display_levels=True)

def encrypt_file(file_path: str, password: str, verbose: bool = False) -> None:
    """
    Encrypts a file using the Fernet encryption algorithm.

    Args:
        file_path (str): The path to the file to encrypt.
        password (str): The password to use for encryption.

    Returns:
        None
    """
    if verbose:
        logger.info(f"Encrypting file: {file_path}")

    # generate a salt for PBKDF2 key derivation
    salt = get_random_bytes(16)

    # derive a 256-bit key using PBKDF2
    key = PBKDF2(password, salt, dkLen=32)

    # generate a random initialization vector for AES encryption
    iv = get_random_bytes(16)

    # create an AES cipher object with the derived key and initialization vector
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # read the file as bytes
    with open(file_path, "rb") as f:
        file_bytes = f.read()

    # pad the file bytes to a multiple of 16 bytes
    padded_file_bytes = file_bytes + b"\0" * (16 - len(file_bytes) % 16)

    # encrypt the padded file bytes using AES
    encrypted_bytes = cipher.encrypt(padded_file_bytes)


    # Get the directory path
    directory_path = os.path.dirname(file_path)

    # Create the encrypted directory if it does not exist
    encrypted_directory_path = os.path.join(directory_path, 'encrypted')
    if not os.path.exists(encrypted_directory_path):
        os.makedirs(encrypted_directory_path)


    # create a new file name by appending '_encrypted' to the original file name
    encrypted_file_path = os.path.join(directory_path, 'encrypted', os.path.basename(file_path)[:-4]+'_encrypted'+file_path[-4:])

    # write the salt, initialization vector, and encrypted bytes to a new file with '_encrypted' appended to the filename
    with open(encrypted_file_path, "wb") as f:
        f.write(salt)
        f.write(iv)
        f.write(encrypted_bytes)


def decrypt_file(file_path: str, password: str, verbose: bool = False) -> None:
    """
    Decrypts a file that has been encrypted with the AES encryption algorithm.

    Args:
        file_path (str): The path to the file to decrypt.
        password (str): The password used for encryption.

    Returns:
        None
    """
    if verbose:
        logger.info(f"Decrypting file: {file_path}")

    # read the salt, initialization vector, and encrypted bytes from the file
    with open(file_path, "rb") as f:
        salt = f.read(16)
        iv = f.read(16)
        encrypted_bytes = f.read()

    # derive the key from the password and salt using PBKDF2
    key = PBKDF2(password, salt, dkLen=32)

    # create an AES cipher object with the derived key and initialization vector
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # decrypt the encrypted bytes using AES
    decrypted_bytes = cipher.decrypt(encrypted_bytes)

    # unpad the decrypted bytes by removing any trailing null bytes
    unpadded_decrypted_bytes = decrypted_bytes.rstrip(b"\0")

    # Get the directory path
    directory_path = os.path.dirname(file_path)

    # Create the encrypted directory if it does not exist
    decrypted_directory_path = os.path.join(directory_path, 'decrypted')
    if not os.path.exists(decrypted_directory_path):
        os.makedirs(decrypted_directory_path)


    # create a new file name by appending '_encrypted' to the original file name
    decrypted_file_path = os.path.join(directory_path, 'decrypted', os.path.basename(file_path)[:-4]+'_decrypted'+file_path[-4:])


    # write the decrypted bytes to a new file with '_decrypted' appended to the filename
    with open(decrypted_file_path, "wb") as f:
        f.write(unpadded_decrypted_bytes)


def main():
    parser = argparse.ArgumentParser(description="Encrypt or decrypt files.")
    parser.add_argument(
        "folder_path",
        metavar="folder_path",
        type=str,
        help="Path to the folder containing the files",
    )
    parser.add_argument(
        "operation",
        metavar="operation",
        type=str,
        choices=["encrypt", "decrypt"],
        help="Operation to perform (encrypt or decrypt)",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output",
    )

    args = parser.parse_args()

    # prompt user to enter a password for encryption
    if args.operation == "encrypt":
        password = getpass.getpass(prompt="Enter a password for encryption: ")
        while not password:
            password = getpass.getpass(
                prompt="Password cannot be empty. Enter a password for encryption: "
            )
    else:
        password = getpass.getpass(prompt="Enter the password for decryption: ")
        while not password:
            password = getpass.getpass(
                prompt="Password cannot be empty. Enter the password for decryption: "
            )

    # iterate over all files in the folder
    for filename in os.listdir(args.folder_path):
        # check if the file is a PNG image
        if filename.endswith(".png") or filename.endswith(".jpg"):
            file_path = os.path.join(args.folder_path, filename)

            # perform encryption or decryption based on user choice
            if args.operation == "encrypt":
                encrypt_file(file_path=file_path, password=password, verbose=args.verbose)
            elif args.operation == "decrypt":
                decrypt_file(file_path=file_path, password=password, verbose=args.verbose)


if __name__ == "__main__":
    main()
