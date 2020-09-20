#!/usr/bin/python3
#chiffrage
public_key = key.publickey()
enc_data = public_key.encrypt(b"""bonjour c'est un message secret""", 32)
	

