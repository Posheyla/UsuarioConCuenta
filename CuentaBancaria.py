class CuentaBancaria:
    lista_cuenta=[]
    def __init__(self, nombre="n/a", tasa_interes=0.01, balance=0.0): 
        self.nombre = nombre
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.lista_cuenta.append(self)

    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("Fondos insuficientes: cobrando una tarifa de ${}".format(self.balance))
            self.balance = 0
        return self

    def mostrar_info_cuenta(self):
        print("{}: ${}".format(self.nombre,self.balance))
        return self

    def generar_interes(self):
        if self.balance>0:
            self.balance = self.balance + self.balance * self.tasa_interes
        else:
            print("No tiene dinero en su cuenta")
        return self
    
    @classmethod
    def imprimir_info_cuenta(cls):
        for i in cls.lista_cuenta:
            i.mostrar_info_cuenta()

class Usuario:
    lista_usuario=[]
    def __init__(self, name="N/A", email="N/A"):
        self.name = name
        self.email = email
        self.cuenta = CuentaBancaria()
        Usuario.lista_usuario.append(self)

    def hacer_deposito(self, amount):	
        self.cuenta.deposito(amount)
        return self

    def hacer_retiro(self, cantidad):
        self.cuenta.retiro(cantidad)
        return self

    def mostrar_balance_usuario(self):
        print("Usuario: {}, {}: {}".format(self.name,self.cuenta.nombre,self.cuenta.balance))
        return self

    def transferir_dinero(self, other_user, valor):
        self.cuenta-=valor
        other_user.cuenta+=valor
        return self

    @classmethod
    def imprimir_info_usuarios(cls):
        for x in cls.lista_usuario:
            x.mostrar_balance_usuario()