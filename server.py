import socket

#serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#serveur.bind(("", 63000))
#serveur.listen(1)

#print("Serveur en attente de connexion...")

#conn, addr = serveur.accept()
#print(f"Connexion établie avec {addr}")

#Etape 1

#message = conn.recv(1024).decode()
#print(f"Reçu du client : {message}")

#conn.send("Bonjour client !".encode())

#conn.close()
#serveur.close()
#print("Connexion fermée.")

#Etape 3

#while True:  # boucle d'échange avec ce client
#   	msg = conn.recv(1024).decode()  # reçoit un message
#   	if msg == "fin":
#       	print("Client a demandé l'arrêt du serveur.")
#       	conn.close()
#       	serveur.close()
#       	print("Serveur arrêté.")
#       	exit()
#else:
#    	print(f"Message reçu: {msg}")
#    	conn.send(msg.encode())  # renvoie le même message (Echo)

#Etape4


#while True:  # boucle d'échange avec ce client
#   	msg = conn.recv(1024).decode()  # reçoit un message
#   	if msg == "fin":
 #      	print("Client a demandé l'arrêt du serveur.")
  #     	conn.close()
   #    	serveur.close()
	#   	print("Serveur arrêté.")
 	#  	exit()
  	# else:
   	# print(f"Message reçu: {msg}")
#   	reponseServer = input("Entre un message :")
 #  	conn.send(reponseServer.encode())  
  # 	if reponseServer == "fin":
   #    	conn.close()
	#   	serveur.close()
 	#  	print("Serveur arrêté.")
  	# 	exit()

#Etape5

#while True:
#  	expression = conn.recv(1024).decode()
 # 	if expression == "fin":
 #       	print("Fin de connexion.")
 #       	conn.close()
 #       	serveur.close()
 #       	print("Serveur arreté.")
 #       	exit()    
 # 	else:
 #    	print(f"Expression reçue : {expression}")
 #    	try:
 #        	result = eval(expression)
 #        	conn.send(str(result).encode())   
 #    	except Exception as e:
 #        	conn.send(f"Erreur : {e}".encode())


#conn.close()
   # print("Connexion fermée.")

#Etape6


#pseudo = conn.recv(1024).decode()
#print(f"Pseudo reçu : {pseudo}")

#while True:
#    	message = conn.recv(1024).decode()
   	 

#    	parts = message.split(" ", 1)
#    	commande = parts[0]
#    	contenu = parts[1] if len(parts) > 1 else ""

 #   	if commande == "/me":
 #       	conn.send(f"* {pseudo} {contenu}".encode())

  #  	elif commande == "/all":
  #      	conn.send(f"[{pseudo}] {contenu}".encode())

   # 	elif commande == "/bye":
	#    	conn.send(f"À bientôt {pseudo}".encode())
 	#   	break

  	#  elif commande == "/help":
   	# 	aide = (
    	#    	"/me <action> : décrit une action\n"
     	#   	"/all <message> : envoie un message général\n"
      	#  	"/bye : quitter la session\n"
       	# 	"/help : afficher ce message d’aide"
       	# )
        	#conn.send(aide.encode())

   	# else:
    	#	conn.send("Commande inconnue. Tape /help pour la liste.".encode())

#ETAPE7

import threading

#def gerer_client(conn, addr):
 #   print(f"Client connecté depuis {addr}")

  #  while True:
   # 	try:
	#    	msg = conn.recv(1024).decode()
       	 
 	#   	if msg.lower() == "fin":
 	#       	conn.send("Connexion fermée.".encode())
 	#       	break

  	#  	print(f"Message reçu de {addr} : {msg}")
   	# 	conn.send(f"Echo : {msg}".encode())

   	# except ConnectionResetError:
    	#	break

   # conn.close()
   # print(f"Connexion fermée avec {addr}")

# Lancement du serveur
#serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#serveur.bind(("", 63000))
#serveur.listen(5)
#print("Serveur en écoute sur le port 63000...")

#while True:
 #   conn, addr = serveur.accept()
 #   threading.Thread(target=gerer_client, args=(conn, addr)).start()

#ETAPE8    


# Ressource partagée
messages = []

# Verrou pour protéger l'accès à la liste
lock = threading.Lock()

def gerer_client(conn, addr):
	print(f"Client connecté depuis {addr}")
	conn.send("Bienvenue, tapez vos messages. Envoyez 'fin' pour quitter.\n".encode())

	while True:
    	try:
        	msg = conn.recv(1024).decode()
        	if not msg:
            	break

        	if msg.lower() == "fin":
            	conn.send("Connexion terminée.\n".encode())
            	break

        	# Ajout sécurisé du message
        	with lock:
            	messages.append(f"{addr} : {msg}")
            	print(f"Ajouté à la liste : {addr} : {msg}")

        	conn.send("Message reçu et stocké.\n".encode())

    	except ConnectionResetError:
        	break

	conn.close()
	print(f"Connexion fermée avec {addr}")

# Lancement du serveur
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(("", 63000))
serveur.listen(5)
print("Serveur en écoute sur le port 63000...")

while True:
	conn, addr = serveur.accept()
	threading.Thread(target=gerer_client, args=(conn, addr)).start()


