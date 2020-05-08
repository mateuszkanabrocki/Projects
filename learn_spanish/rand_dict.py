#!/usr/bin/env python3

# á
# é
# í
# ú
# ñ
# ü
# ¡
# ¿

import os
from secrets import choice # probably more random then random.choice
from sys import argv

script_name, function_name = argv

sentencias = {
	'Jaki dzisiaj dzień? Mamy listopad/jesień/4 listopada': '¿Que dia es hoy? Estamos en noviembre./en otoño./ Es el 4 de noviembre.',
	'Kiedy masz urodziny? Mam urodziny 5 czerwca': '¿Cuándo es tu cumpleaños? Tengo cumpleaños el 5 de junio./El 5 junio es mi cumpleaños'
}

dias_dict = {
	'poniedziałek': 'el lunes',
	'wtorek': 'el martes',
	'środa': 'el miércoles',
	'czwartek': 'el jueves',
	'piątek': 'el viernes',
	'sobota': 'el sábado',
	'niedziela': 'el domingo'
	}

meses_dict = {
	'styczeń': 'el enero',
	'luty': 'el febrero',
	'marzec': 'el marzo (marso)',
	'kwiecień': 'el abril',
	'maj': 'el mayo',
	'czerwiec': 'el junio (hunio)',
	'lipiec': 'el julio (hulio)',
	'sierpień': 'el agosto',
	'wrzesień': 'el septiembre',
	'październik': 'el octubre',
	'listopad': 'el noviembre',
	'grudzień': 'el diciembre'
}

estaciones_dict = {
	'wiosna': 'el primavera',
	'lato': 'el verano (berano)',
	'jesień': 'el otoño (otonio)',
	'zima': 'el invierno (inbierno)'
}

numeros_dict = {
	'0': 'cero (Sero)',
	'1': 'uno',
	'2': 'dos',
	'3': 'tres',
	'4': 'quatro',
	'5': 'cinco',
	'6': 'seis',
	'7': 'siete',
	'8': 'ocho',
	'9': 'nueve',
	'10': 'diez',
	'11': 'once',
	'12': 'doce',
	'13': 'trece',
	'14': 'catorce',
	'15': 'quince',
	'16': 'dieciséis',
	'17': 'diecisiete',
	'18': 'dieciocho',
	'19': 'diecinueve',
	'20': 'veinte'
}

palabras_dict = {
	'wieża': 'el torro',
	'dom': 'la casa',
	'port': 'el puerto',
	'drzwi': 'la porta',
	'okno': 'la ventana',
	'sufit': 'el techo',
	'podłoga': 'el piso',
	'lampa': 'la lampara',
	'łóżko': 'la cama',
	'samochód': 'el coche',
	'dzisiaj': 'hoy',
	'jutro': 'mañana',
	'wczoraj': 'ayer[ayer]'
}

# verbs = [
# 	'ser',
# 	'estar',
# 	'ir'
# ]

ser = { # być
	'name': 'ser',
	'yo': 'soy',
	'tu': 'eres',
	'el/ella': 'es',
	'nosotros/as': 'somos',
	'vosotros/as': 'sois',
	'ellos/ellas': 'son'
}

estar = { # być
	'name': 'estar',
	'yo': 'estoy',
	'tu': 'estás',
	'el/ella': 'está',
	'nosotros/as': 'estamos',
	'vosotros/as': 'estáis',
	'ellos/ellas': 'están'
}

ir = { #iść
	'name': 'ir',
	'yo': 'voy',
	'tu': 'vas',
	'el/ella': 'va',
	'nosotros/as': 'vamos',
	'vosotros/as': 'vais',
	'ellos/ellas': 'van'
}

tener = { #mieć
	'name': 'tener',
	'yo': 'tengo',
	'tu': 'tienes',
	'el/ella': 'tiene',
	'nosotros/as': 'tenemos',
	'vosotros/as': 'tene^is',
	'ellos/ellas': 'tienen'
}

# hacer = {
# 	'name': 'hacer',
# 	'yo': 'hago',
# 	'tu': 'haces'
# 	'el/ella': 'hace',
# 	'nosotros/as': 'hacemos',
# 	'vosotros/as': 'hace^is',
# 	'ellos/ellas': 'hacen'
# }

# poder = {
# 	'name': 'poder',
# 	'yo': 'puedo',
# 	'tu': 'puedes'
# 	'el/ella': 'puede',
# 	'nosotros/as': 'podemos',
# 	'vosotros/as': 'pode^is',
# 	'ellos/ellas': 'pueden'
# }

# saber = {
# 	'name': 'saber',
# 	'yo': 'se^',
# 	'tu': 'sabes'
# 	'el/ella': 'sabe',
# 	'nosotros/as': 'sabemos',
# 	'vosotros/as': 'sabe^is',
# 	'ellos/ellas': 'saben'
# }

# poner = {
# 	'name': 'poner',
# 	'yo': 'pongo',
# 	'tu': 'pones'
# 	'el/ella': 'pone',
# 	'nosotros/as': 'ponemos',
# 	'vosotros/as': 'pone^is',
# 	'ellos/ellas': 'ponen'
# }

# haber = {
# 	'name': 'haber',
# 	'yo': 'he',
# 	'tu': 'has'
# 	'el/ella': 'ha',
# 	'nosotros/as': 'hemos',
# 	'vosotros/as': 'habe^is',
# 	'ellos/ellas': 'han'
# }

# decir = {
# 	'name': 'decir',
# 	'yo': 'digo',
# 	'tu': 'dices'
# 	'el/ella': 'dice',
# 	'nosotros/as': 'decimos',
# 	'vosotros/as': 'decis',
# 	'ellos/ellas': 'dicen'
# }

# querer = {
# 	'name': 'querer',
# 	'yo': 'quiero',
# 	'tu': 'quieres'
# 	'el/ella': 'quiere',
# 	'nosotros/as': 'queremos',
# 	'vosotros/as': 'quere^is',
# 	'ellos/ellas': 'quieren'
# }

# hablar = {
# 	'name': 'hablar',
# 	'yo': 'hablo',
# 	'tu': 'hablas'
# 	'el/ella': 'habla',
# 	'nosotros/as': 'hablamos',
# 	'vosotros/as': 'habla^is',
# 	'ellos/ellas': 'hablan'
# }

# dar = {
# 	'name': 'dar',
# 	'yo': 'doy',
# 	'tu': 'das'
# 	'el/ella': 'da',
# 	'nosotros/as': 'damos',
# 	'vosotros/as': 'dais',
# 	'ellos/ellas': 'dan'
# }

# ver = {
# 	'name': 'ver',
# 	'yo': 'veo',
# 	'tu': 'ves'
# 	'el/ella': 've',
# 	'nosotros/as': 'vemos',
# 	'vosotros/as': 'veis',
# 	'ellos/ellas': 'ven'
# }

# comer = {
# 	'name': 'comer',
# 	'yo': 'como',
# 	'tu': 'comes'
# 	'el/ella': 'come',
# 	'nosotros/as': 'comemos',
# 	'vosotros/as': 'come^is',
# 	'ellos/ellas': 'comen'
# }

# tomar = {
# 	'name': 'tomar',
# 	'yo': 'tomo',
# 	'tu': 'tomas'
# 	'el/ella': 'toma',
# 	'nosotros/as': 'tomamos',
# 	'vosotros/as': 'toma^is',
# 	'ellos/ellas': 'toman'
# }

# vivir = {
# 	'name': 'vivir',
# 	'yo': 'vivo',
# 	'tu': 'vives'
# 	'el/ella': 'vive',
# 	'nosotros/as': 'vivimos',
# 	'vosotros/as': 'vivis',
# 	'ellos/ellas': 'viven'
# }

# necesitar = {
# 	'name': 'necesitar',
# 	'yo': 'necesito',
# 	'tu': 'necesitas'
# 	'el/ella': 'necesita',
# 	'nosotros/as': 'necesitamos',
# 	'vosotros/as': 'necesita^is',
# 	'ellos/ellas': 'necesitan'
# }

# quedar = {
# 	'name': 'quedar',
# 	'yo': 'quedo',
# 	'tu': 'quedas'
# 	'el/ella': 'queda',
# 	'nosotros/as': 'quedamos',
# 	'vosotros/as': 'queda^is',
# 	'ellos/ellas': 'quedan'
# }

# venir = {
# 	'name': 'venir',
# 	'yo': 'vengo',
# 	'tu': 'vienes'
# 	'el/ella': 'viene',
# 	'nosotros/as': 'venimos',
# 	'vosotros/as': 'venis',
# 	'ellos/ellas': 'vienen'
# }

# next_verb = {
# 	'name': 'next',
# 	'yo': 'x',
# 	'tu': 'x'
# 	'el/ella': 'x',
# 	'nosotros/as': 'x',
# 	'vosotros/as': 'x',
# 	'ellos/ellas': 'x'
# }

verbos_dict = {
	'1': ser,
	'2': estar,
	'3': ir,
	'4': tener
	# '5': hacer,
	# '6': poder,
	# '7': saber,
	# '8': poner,
	# '9': haber,
	# '10': decir,
	# '11': querer,
	# '12': hablar,
	# '13': dar,
	# '14': ver,
	# '15': comer,
	# '16': tomar,
	# '17': vivir,
	# '18': necesitar,
	# '19': quedar,
	# '20': venir
}


def play(dict_esp, title='----------', verbs_conjugation=0):
	if verbs_conjugation:
		del dict_esp['name']
	choices_esp = list(dict_esp.keys())
	while True:
		os.system('clear')
		choice_esp = choice(choices_esp)
		print('--', title, '--\n>', choice_esp)
		input('> ')
		print('>',dict_esp[choice_esp])
		input("")

def verbos_conjugation():
	os.system('clear')
	# choose verb you want to learn
	print("Choose verb you want to practise or",
	"press ENTER to practise all verbs at once:")
	# print list of verbs
	# for counter, verb in enumerate(verbs):
	# 	print(counter, verb)
	for key, value in verbos_dict.items():
		print(key, value['name'])
	# verb = verbs[input('> ')]
	verb = verbos_dict[input('> ')]
	play(verb, 1)


def main():
	if function_name == 'verbos':
		verbos_conjugation()
	elif function_name == 'palabras':
		play(palabras_dict, 'palabras')
	elif function_name == 'sentencias':
		play(sentencias_dict, 'sentencias')
	elif function_name == 'dias':
		play(dias_dict, 'los dias de la semana')
	elif function_name == 'meses':
		play(meses_dict, 'los meses')
	elif function_name == 'estaciones':
		play(estaciones_dict, 'los estaciones del año')
	elif function_name == 'numeros':
		play(numeros_dict, 'numeros')
	else:
		pass

main()

# USE like this:
# ./rand_dict.py seasons


# TODO
# dodać czasownik ser i estar jednocześnie, nad zapytaniem bezokolicznik print
# 20 najpopularniejszych czasowników - bezokoliczniki, odmiana, zdania
# wyświetlanie czego możemy się uczyć wraz z instrukcją jak włączyć daną powtórkę
# zamiast losowania mieszanie kopii listy  po każdym  jej przejściu lub bardziej randomowe losowanie
# add ser, estar, it odmiana - 1 funkcja
# z wyborem czasownika do odmiany, wyjśćie, wybór innego lub od razu
# funkcja dodawania nowych czasowników
