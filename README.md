# File Encryption Program

This is a simple Python script that can encrypt and decrypt files in a given folder using the AES encryption algorithm. The script prompts the user for a password to use for encryption or decryption.

## Requirements

To run this program, you'll need to have Python 3 installed on your system. You can download the latest version of Python from the official website: https://www.python.org/downloads/

You'll also need to install some packages. You can do this using pip, the Python package installer, by running the following command in your command prompt or terminal:

```
pip install -r requirements.txt
```

This will install all the dependencies.

## Virtual environment

to create a virtual environment for this program using venv, you can follow these steps:

- Open a command prompt or terminal and navigate to the directory where you want to create the virtual environment.

- Run the following command to create a new virtual environment named venv:

```bash
python -m venv venv
```

This will create a new directory named venv in your current directory, which contains the Python interpreter and other files needed to run the virtual environment.

- Activate the virtual environment by running the following command:

**On Windows:**

```bash
venv\Scripts\activate.bat
```

**On Unix or Linux:**

```bash
source venv/bin/activate
```

This will activate the virtual environment and change your command prompt to indicate that you're now using the virtual environment.

## Usage

- Clone this repository or download the source code.

- Open a terminal or command prompt and navigate to the directory containing the program files.

- Install the required cryptography module by running `pip install -r requirements.txt`.

- Run the program by running `python image_encrypt.py folder_path operation [-p password]` in the terminal or command prompt, where:

- `folder_path`: Path to the folder containing the files to encrypt or decrypt.

- `operation`: The operation to perform. Must be either "encrypt" or "decrypt".

- `-v, --verbose`: (Optional) Enable verbose output.

- The program will process all `PNG` and `JPG` image files in the specified folder, encrypting or decrypting them based on the operation specified.

- When the script is run, it will prompt the user to enter a password for encryption or decryption. The password cannot be empty.

## Examples

To encrypt all the PNG and JPG images in the images folder and enable verbose output:

```
python simple-file-encryptor.py images encrypt -v
To decrypt all the PNG and JPG images in the images folder:
```

```
python simple-file-encryptor.py images decrypt
```

## Acknowledgments

This program was created using the cryptography package, which is maintained by the Python Cryptographic Authority.
