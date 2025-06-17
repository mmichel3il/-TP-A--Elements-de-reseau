# -TP-A--Elements-de-reseau

---

## 2.1.4 Questions

### À quel moment la socket côté serveur est-elle bloquante ?
Elle est bloquante lors de serveur.accept() car elle attend une connexion et lors de conn.recv car elle attend les données.

### Que se passe-t-il si le client se connecte avant que le serveur ne soit prêt ? 
Cela plante côté client avec une erreur de type connectionrefusedError: [Errno 111] connexion refused car le serveur n'écoute pas encore sur le port.

### Quelle est la différence entre bind() et listen() ?
bind attend la socket à une adresse IP et un port alors que listen met la socket en mode écoute.

## 2.2.4 Questions
### Pourquoi faut-il une boucle dans le serveur ?
Pour traiter plusieurs messages successifs sans fermer la connexion après le premier échange.

### Que se passe-t-il si on oublie de tester msg == "fin" ?
La boucle continue indéfiniment, et le client doit forcer la fermeture (Ctrl+C ou timeout).

### Est-ce que le serveur peut envoyer plusieurs réponses d'affilée ?
Oui, mais le client doit les lire une par une avec recv() pour éviter des mélanges.

## 2.3.4 Questions

### Le serveur peut-il rester actif après une déconnexion client ?
Oui, car la seule condition d’arrêt est “fin” dans la boucle sans l'exécution de cette condition le serveur reste actif.

### Que faut-il modifier pour accepter plusieurs clients à la suite ?
Il faut que le serveur.accept() soit placé dans la boucle, pour qu’à chaque itération un nouveau client ait la possibilité de se connecter.

### Peut-on imaginer accepter des clients en parallèle ?
Oui, en utilisant des threads (étape 7) ou des processus.

## 2.4.4 Questions

### Comment s'assurer que les deux côtés ne parlent pas en même temps ?
En alternant strictement recv() et send().

### Peut-on rendre cet échange non bloquant ? Comment ?
Oui, avec socket.setblocking(False) et une boucle d'événements (mais complexe).

### Quelle est la meilleure façon de quitter proprement la communication ?
Envoyer un mot-clé comme “fin” qui est utilisé dans le code et fermer les sockets avec un .close().

## 2.5.4 Questions

### Quels sont les risques d'utiliser eval() ? (souvenirs de FONDADEV)
Utiliser eval () dans un serveur permet à n'importe quel client d'exécuter du code Python arbitraire, ce qui expose à des failles critiques de sécurité comme la suppression de fichiers, le vol de données ou le contrôle total du système.

### Comment renvoyer une erreur sans faire planter le serveur ?
Capturer les exceptions avec try/except et envoyer un message d'erreur au client.

## 2.6.5 Questions 

### Pourquoi structurer les messages avec /commande ?
Ça permet au serveur de comprendre clairement ce qu’on veut faire (obtenir de l’aide, quitter, etc.) sans devoir analyser tout le message librement rédigé.

### Comment distinguer facilement les types de messages côté serveur ?
En vérifiant le préfixe ex: if message.startswith("/me").

## 2.7.4 Questions 

### Que se passe-t-il si deux clients envoient des messages en même temps ?
Sans verrou, les données peuvent se mélanger qui par exemple peut mener à une écriture concurrente dans un fichier.

### Peut-on garder un état partagé entre clients ? Est-ce souhaitable ?
Oui, mais il faut des verrous (threading.Lock()). Non parce que ça implique un risque de complexité.

### Que faut-il pour aller vers une vraie messagerie ?
Un système de broadcast (diffusion à tous les clients) et une gestion centralisée des états.

## 2.8.4 Questions

### Pourquoi faut-il protéger certaines sections du code ?
Pour éviter des conditions de course comme exemple, on peut prendre deux threads modifiant une même variable.

### Que risque-t-on si deux clients modifient une même ressource simultanément ?  
Quand deux clients modifient simultanément une même ressource sans synchronisation, on risque une condition de course entraînant la perte de données, des incohérences, ou des violations de règles métier. 
