frutas = {'Granadilla':11000, 'Papaya':1800, 'Melon':1500, 'Uva':8500, 'Piña':6000, 'Fresa':10700, 'Naraja':5000, 'Kiwi':10000}
fruta = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, 'cops')
else: 
    print("Lo siento, la fruta", fruta, "no está disponible.")