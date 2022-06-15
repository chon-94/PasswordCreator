# PasswordCreator
 Creador de Claves

    caracteres = list(string.ascii_letters + string.digits + "!@#$%^&*()-_=?+")

    def generadorAleatorioCLaves():

        cc = int(input("Introduzca la cantidad de caracteres: "))

        random.shuffle(caracteres)
        
        clave = []
        for i in range(cc):
            clave.append(random.choice(caracteres))

        random.shuffle(clave)

        print("".join(clave))

    generadorAleatorioCLaves()