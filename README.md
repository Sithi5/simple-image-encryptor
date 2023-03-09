# File Encryption Program

This is a Python program that can encrypt and decrypt files using the cryptography package. It supports encryption and decryption of PNG image files, but can be easily modified to support other file types.

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

- Clone or download the repository to your local machine.

- Open a command prompt or terminal and navigate to the directory containing the Python file.

- Run the following command to start the program:

```bash
python filename.py
```

- Replace filename.py with the name of your Python file.

- The program will prompt you to enter the path of the folder containing the files you want to encrypt or decrypt, whether you want to encrypt or decrypt the files, and for encryption, the password to use for encryption.

- The program will then perform the encryption or decryption on all PNG image files in the specified folder.

## Acknowledgments

This program was created using the cryptography package, which is maintained by the Python Cryptographic Authority.
