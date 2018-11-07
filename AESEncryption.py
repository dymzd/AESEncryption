import sys
import base64
from Crypto.Cipher import AES
from Crypto import Random


if(len(sys.argv) < 5 or len(sys.argv) > 5):
    print("Please use the following format for this program")
    print("AESEncryption.py test.txt -e outputfile.txt PublicKey")
    print("-e for Encryption -d for Decryption")
else:
    if((".txt" or ".text") not in (sys.argv[1] and sys.argv[3] )):
        print("This program only supports text file encryption. Please Try again.")
    else:
        if(sys.argv[2] != '-e' and sys.argv[2] != ('-d') ):
            print("Please use the following format for this program")
            print("AESEncryption.py test.txt -e PublicKey")
            print("-e for Encryption -d for Decryption")
        else:
            key = sys.argv[4]
            #obj = pyaes.AESModeOfOperationCTR(key)
            file_object  = open(sys.argv[1],"r")
            output_file = open(sys.argv[3],"a+")
            if(sys.argv[2] == '-e'):
                for line in file_object:
                    iv = Random.new().read( AES.block_size )
                    obj = AES.new(sys.argv[4], AES.MODE_CBC, iv)
                    print(line)
                    #line = line.encode('utf-8')
                    ciphertext = base64.b64encode(iv + obj.encrypt(line))
                    ciphertext = ciphertext.decode()

                    print(ciphertext)
                    output_file.write("%s \n" % ciphertext)
                file_object.close()
                output_file.close()
            elif(sys.argv[2] == '-d'):
                for line in file_object:
                    enc = base64.b64decode(line)
                    iv = enc[:16]
                    obj = AES.new(sys.argv[4], AES.MODE_CBC, iv)
                    print(line)
                    #line = line.encode('utf-8')
                    ciphertext = obj.decrypt(enc[16:])
                    #ciphertext = ciphertext.decode('utf-8')
                    ciphertext = ciphertext.decode()
                    print(ciphertext)
                    output_file.write("%s \n" % ciphertext)
                file_object.close()
                output_file.close()



