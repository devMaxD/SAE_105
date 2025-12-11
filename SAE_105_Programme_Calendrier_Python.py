#!/usr/bin/env python
# -*-coding: utf-8 -*
# // Code épuré qui propose une version claire
# // informations listées à la verticale en fonction de l'ordre des valeurs proposées en entrée
entetes = [
     u'BEGIN\n' 		# //valeur1
     u'DTSTAMP\n'		# //valeur2
     u'DTSTART\n'		# //valeur3
     u'DTEND\n'			# //valeur4
     u'SUMMARY\n'		# //valeur5
     u'LOCATION\n'		# //valeur6
     u'DESCRIPTION\n'	# //valeur7
     u'UID\n'			# //valeur8
     u'CREATED\n'		# //valeur9
     u'LAST-MODIFIED\n'	# //valeur10	
     u'SEQUENCE\n'		# //valeur11
     u'END\n',			# //valeur12


]

valeurs = [
     [u'\nVEVENT\n' u'20251210T214451Z\n' u'20251205T090000Z\n'u'20251205T110000Z\n'u'SAE1.05\n'],
     [u'G_011_AMPHI\n'u'RT1-S1\nLACAN DAVID\n'u'ADE60323032352d3230323653542d455449454e4e452d32323839322d302d30\n'u'19700101T000000Z\n'u'20251210T214451Z\n'],
     [u'2142073524']
]

# // La valeur d'entée 'Begin' va renvover à la valeur 'VEVENT' dans la partie 'valeurs' etc.
# // Ordre des valeurs en entrée respecté pour l'attribution des valeurs correspondantes.

f = open('monFichier.csv', 'w')
ligneEntete = ";".join(entetes) + "\n"
f.write(ligneEntete)
for valeur in valeurs:
     ligne = ";".join(valeur) + "\n"
     f.write(ligne)
# // Code testé, un nouveau fichier "monFichier.CSV" se crée dans le Block notes
# // Fichier crée dans l'emplacement C:\Users\Admin
f.close()