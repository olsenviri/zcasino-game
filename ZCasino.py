import random as aleatoire
import math


recommencer = True;

resultat = 8/3
print(resultat)




while recommencer:

	montantParie = 0;
	#---------------------------------------------------------------


	while montantParie <= 0:
		montantParie = input("Combien voulez vous parier: ");
		montantParie = int(montantParie);

		if montantParie == 0:
			print("veillez parier svp.");
		elif montantParie < 0:
			print("valeur invalide.")



	#----------------------------------------------------------------

	print("vous avez ", montantParie, "$ ");


	numeroChoisi = input("choisissez un numero compris entre 0 et 49: ");
	numeroChoisi = int(numeroChoisi);


	#boucle while pour tester si la valeur saisie par l'utilisateur est 
	#comprise entre 0 et 49
	#--------------------------------------------------


	while (numeroChoisi < 0 or numeroChoisi > 49):
		print("le numero n'est pas valide.");
		numeroChoisi = input("choisissez un numero: ");
		numeroChoisi = int(numeroChoisi);




	#Fin de la verification
	#---------------------------------------------------

	numeroGagnant = aleatoire.randrange(50); #choix du numero gagnant de façon aleatoire


	#----------------------------------------------------

	

	if(numeroChoisi == numeroGagnant):
		print("vous avez gagne ", montantParie*3, " felicitation a vous.");

	else:
		if((numeroChoisi % 2 == 0 and numeroGagnant % 2 == 0) or (numeroChoisi % 2 != 0 and numeroGagnant % 2 != 0)):
			
			print("il ne vous reste plus que: ", math.ceil(montantParie/2), " courage a vous");
					
		else:
			print("desole mon ami, vous avez perdu");	
			
	
	choix = input("voulez vous recommencer oui/non: ");

	if choix != "oui":
		recommencer = False;


#-----------------------------------------------------

print("____FIN__");



		







