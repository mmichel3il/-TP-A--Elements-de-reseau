import socket

#etape1
#client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client.connect(("localhost", 63000))  # ou l'IP du serveur si sur 2 machines


#client.send("Bonjour serveur !".encode())


#reponse = client.recv(1024).decode()
#print(f"Reçu du serveur : {reponse}")


#client.close()

#etape3

# Création de la socket client
#client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client.connect(("localhost", 63000))  # ou l'IP du serveur

#print("Connecté au serveur. Tapez 'fin' pour arrêter.")

#while True:
#	message = input("Entrez un message : ")  # <- input ici pour taper les messages

#	client.send(message.encode())  # Envoi du message

#	if message == "fin":
#    	print("Fermeture de la connexion demandée.")
#    	break

#	reponse = client.recv(1024).decode()  # Réponse du serveur
#	print("Serveur :", reponse)

#client.close()  # Fermeture de la socket client

#etape4

# Création de la socket client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 63000))  # ou l'IP du serveur

print("Connecté au serveur. Tapez 'fin' pour arrêter.")

#while True:
#	message = input("Client : ")  # <- input ici pour taper les messages

 #   client.send(message.encode())  # Envoi du message

  #  if message == "fin":
	#	print("Fermeture de la connexion demandée.")
   # 	break

   # reponse = client.recv(1024).decode()  # Réponse du serveur
   # print("Serveur :", reponse)
   # if reponse == "fin":
	#   print("Serveur arrêté.\nFermeture de la connexion.")
 	#  break
#client.close()  # Fermeture de la socket client

#etape5

#while True:
#	expr = input("Entrez une expression : ")
#	client.send(expr.encode())
#
#	if expr == "fin":
#    	break
#
#	result = client.recv(1024).decode()
#	print("Résultat :", result)

#client.close()

#etape6


# réception de la demande de pseudo

#pseudo = input("Ton pseudo : ")
#client.send(pseudo.encode())

#while True:
 #   msg = input("Client > ")
#	client.send(msg.encode())

#	if msg.startswith("/bye"):
#    	print("Déconnexion demandée.")
#    	break

#	reponse = client.recv(1024).decode()
#	print("Serveur >", reponse)

#client.close()

#etape7et8

while True:
	msg = input("Vous > ")
	client.send(msg.encode())

	if msg.lower() == "fin":
    	break

	reponse = client.recv(1024).decode()
	print("Serveur >", reponse)

client.close()
print("Connexion fermée.")



