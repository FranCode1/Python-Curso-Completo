# =====================================================================
# EJERCICIO 76: Clase Cuenta_Bancaria
# ---------------------------------------------------------------------
# Crear la clase Cuenta_Bancaria con los atributos privados:
# • __titular
# • __saldo
# El constructor inicializa ambos valores por parametro.
# Metodos:
# • depositar: Recibe un monto y aumenta el saldo
# • retirar: Recibe un monto y descuenta. Solo si hay saldo suficiente.
# • mostrar_saldo: Imprime el saldo =====================================================================

class Cuenta_Bancaria:
    def __init__(self, __titular, __saldo):
        self.__titular = __titular
        self.__saldo = __saldo

    def depositar(self, monto):
        self.__saldo += monto
        print(f"Se han depositado ${self.__saldo} pesos")

    def retirar(self, monto):
        if monto > self.__saldo:
            print("Saldo insuficiente, no puede retirar esa cantidad de dinero")
        else:
            self.__saldo -= monto
            print(f"Usted a retirado ${monto} pesos")

    def mostrar_saldo(self):
        print(f"Hola {self.__titular}, tu saldo es: {self.__saldo}")

cuenta1 = Cuenta_Bancaria("Jose", 345)
cuenta1.depositar(700)
cuenta1.mostrar_saldo()

cuenta1.retirar(400)
cuenta1.retirar(2000)