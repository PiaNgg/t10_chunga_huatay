import libreria

def soltero():
    print("Disfrute su solteria")

def casado():
    print("Usted esta comprometido")


def divorciado():
    print("Sentimos su perdida")
opc=0
max=4
while opc != max:
    print("##### ESTADO #####")
    print("# 1.  SOLTERO ####")
    print("# 2.  CASADO  ####")
    print("# 3.  Divorciado #")
    print("# 4.  Salir    ###")
    print("################")
    opc=libreria.pedir_numero("¿Cual es su estado?",1,4)
    if opc == 1:
        soltero()

    if opc == 2:
        casado()

    if opc == 3:
        divorciado()

print("Gracias por participar")
