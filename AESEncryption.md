File: AESEncryption.py
Author: Daiya Masuda
Created on: Nov 7th 
Python Interpretor: 3.7
Libraries: pyCrypto (import Crypto) https://pypi.org/project/pycrypto/
           sys (import sys)
           base64 ( import base64)
Description: This program allows you to encrypt/decrypt a text file (.txt or .text) with a secret key.
Usage: python3 AESEncryption.py test.txt -e outputfile.txt PublicKey
    argv[1] = name of input file. eg. inputfile.txt (Input has to be a length of 16*n)
    argv[2] = -e or -d (-e for encryption -d for decryption)
    argv[3] = name of output file. eg. outputfile.text
    argv[4] = publickey has to be length of 16*n


