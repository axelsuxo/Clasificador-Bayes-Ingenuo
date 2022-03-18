#!/usr/bin/env python
# Este archivo usa el encoding: utf-8

HAM="practica deportes hoy fue practica deportes evento deportes secreto deportes es hoy deportes cuesta dinero"
SPAM="oferta es secreto click link secreto link deportes secreto"

HAM=HAM.split()
SPAM=SPAM.split()

vocabulario=12

def contarPalabra(palabra, lista):
	cont=0
	for p in lista:
		if p==palabra:
			cont+=1
	return cont

def calculaProbClase(mensaje, clase):
	m=mensaje.split()
	#Calcular probabilidades de SPAM de cada palabra del mensaje
	probSPAM=(len(SPAM)+3)/(len(SPAM)+len(HAM)+6)
	probPalabraSPAM=[]
	for palabra in m:
		tmp=(contarPalabra(palabra,SPAM)+1)/(len(SPAM)+vocabulario)
		probPalabraSPAM.append(tmp)
	probAcumSPAM=1
	for prob in probPalabraSPAM:
		probAcumSPAM = probAcumSPAM*prob
	#Calcular probabilidades de HAM de cada palabra del mensaje
	probHAM=(len(HAM)+3)/(len(SPAM)+len(HAM)+6)
	probPalabraHAM=[]
	for palabra in m:
		tmp=(contarPalabra(palabra,HAM)+1)/(len(HAM)+vocabulario)
		probPalabraHAM.append(tmp)
	probAcumHAM=1
	for prob in probPalabraHAM:
		probAcumHAM = probAcumHAM*prob
	if clase=="SPAM":
		probSPAMMensaje=(probSPAM*probAcumSPAM)/((probSPAM*probAcumSPAM)+(probHAM*probAcumHAM))
		return probSPAMMensaje
	elif clase=="HAM":
		probHAMMensaje=(probHAM*probAcumHAM)/((probSPAM*probAcumSPAM)+(probHAM*probAcumHAM))
		return probHAMMensaje
	else:
		print("Se esta tratando de calcular la probabilidad de una clase que no existe")

mensaje="secreto es hoy"
print("mensaje=", mensaje)
print("Probabilidad de SPAM= ", calculaProbClase(mensaje, "SPAM"))
print("Probabilidad de HAM= ", calculaProbClase(mensaje, "HAM"))
