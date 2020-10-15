# ElGamal ÅŸifrelemesini gÃ¶steren Python programÄ±
#!!!output Ã§Ä±ktÄ±sÄ±nÄ±n son deÄŸeri anahtar onu yazarak aÃ§Ä±yoruz diÄŸeri ÅŸifreli dizi halinde tutuluyor!!!!
import random 
from math import pow
from tkinter import *

a = random.randint(2, 10) 

def gcd(a, b): 
	if a < b: 
		return gcd(b, a) 
	elif a % b == 0: 
		return b; 
	else: 
		return gcd(b, a % b) 

# Generating large random numbers 
def gen_key(q): 

	key = random.randint(pow(10, 20), q) 
	while gcd(q, key) != 1: 
		key = random.randint(pow(10, 20), q) 

	return key 

# ModÃ¼ler Ã¼s alma 
def power(a, b, c): 
	x = 1
	y = a 

	while b > 0: 
		if b % 2 == 0: 
			x = (x * y) % c; 
		y = (y * y) % c 
		b = int(b / 2) 

	return x % c 

# asimetrik ÅŸifreleem
def encryption(msg, q, h, g): 

	global en_msg
	en_msg = [] 

	k = gen_key(q)# Private key for sender 
	s = power(h, k, q) 
	p = power(g, k, q) 
	
	for i in range(0, len(msg)): 
		en_msg.append(msg[i]) 

	#print("p deÄŸeri ile aÃ§Ä±yoruz used : ", p) 
	#print("g^ak used : ", s) 
	for i in range(0, len(en_msg)): 
		en_msg[i] = s * ord(en_msg[i]) 
	#print("ÅŸifreli mesaj:",en_msg)
	
	return p
	
	

#burada mormalde p deÄŸerini de geri dÃ¶nÃ¼yordum ama anakhtarla mesajÄ± okuyaÃ§aÄŸÄ±mÄ±z iÃ§in burada geri dÃ¶nmedim.
def decryption(en_msg, p, key, q): 

	dr_msg = [] 
	h = power(p, key, q) 
	for i in range(0, len(en_msg)): 
		dr_msg.append(chr(int(en_msg[i]/h))) 
	
	dmsg = ''.join(dr_msg) 
	return dmsg

# Driver code 

#msg = input("Åifreli mesaj:")
#print("Original Message :", msg) 

q = random.randint(pow(10, 20), pow(10, 50)) 
g = random.randint(2, q) 

key = gen_key(q)# Private key burada public anahtardann oluÅŸturulmuÅŸtur
h = power(g, key, q) 
	
#ÅŸifreleme
#en_msg=encrypt(msg, q, h, g) 
#ÅŸifre Ã§Ã¶zme
#(p)=input("p DEÄERÄ° ELLE YAZALIM:")
#dr_msg = decrypt(en_msg,int(p), key, q) 
#dmsg = ''.join(dr_msg) 
#print("Decrypted Message :", dmsg); 

def setTextInput(widget, text):
    widget.delete(1.0,"end")
    widget.insert(1.0, text)

root = Tk()
root.title("ElGamal")
actions_frame = Frame(root)
input_frame = Frame(root)
output_frame = Frame(root)

input_label = Label(input_frame, text="Input: ")
input_msg = Text(input_frame, height=5, width=100)

output_label = Label(output_frame, text="Output: ")
output_msg = Text(output_frame, height=5, width=100)

encrypt = Button(actions_frame, text="Encrypt", command=lambda: setTextInput(output_msg,encryption(
    input_msg.get("0.0", "128.0"), q,h,g)))
	
decrypt = Button(actions_frame, text="Decrypt", command=lambda: setTextInput(output_msg,decryption(
    en_msg,int(input_msg.get("0.0", "128.0")),key,q )))


input_label.pack(side=TOP)
input_msg.pack(side=LEFT)

encrypt.pack(side=LEFT)
decrypt.pack(side=LEFT)

output_label.pack(side=TOP)
output_msg.pack(side=LEFT)

input_frame.pack()
actions_frame.pack()
output_frame.pack()

root.mainloop()