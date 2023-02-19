import os
import pyaes

## open encrypt file
file_name = "teste.txt.ransomwaretroll"
file = open(file_name,"rb")
file_data = file.read()
file.close()

## key of decrypt
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remove encrypt file
os.remove(file_name)

## create decrypt file
new_file = "teste.txt"
new_file = open(f'{new_file}',"wb")
new_file.write(decrypt_data)
new_file.close()
