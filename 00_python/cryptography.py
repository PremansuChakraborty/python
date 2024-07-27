def encrypt(message, key): 
	encrypted=""

	for i in range(len(message)):

#Applying XOR operation between message character and key character 
		encrypted_char=chr(ord(message[i])^ord(key[i%len(key)]))

		encrypted += encrypted_char 
	return encrypted

def decrypt(encrypted, key):

	decrypted=""
	for i in range(len(encrypted)):
#Applying XOR operation between encrypted character and key character 
		decrypted_char=chr(ord(encrypted[i])^ ord(key[i%len(key)]))

		decrypted += decrypted_char

	return decrypted
	
# Example usage

message =input("enter your message: ")

key ="Secretg g'c5 33s6yr k"

#Encrypt the message

print("Initial message:", message) 
encrypted_message= encrypt(message, key) 
print("Encrypted message:", encrypted_message)



#Decrypt the encrypted messagit initge

decrypted_message= decrypt(encrypted_message, key) 
print("Decrypted message:", decrypted_message)

# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/PremansuChakraborty/python.git
# git push -u origin main