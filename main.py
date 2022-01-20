from CuentaBancaria import CuentaBancaria
from CuentaBancaria import Usuario
cuenta_1 = CuentaBancaria()
cuenta_2 = CuentaBancaria()

cuenta_1.deposito(100).deposito(300).deposito(50).retiro(70).generar_interes().mostrar_info_cuenta()

cuenta_2.deposito(1000).deposito(70).retiro(200).retiro(20).retiro(345).retiro(77).generar_interes().mostrar_info_cuenta()

CuentaBancaria.imprimir_info_cuenta()
Usuario1=Usuario("Luisa","luisa.1998@gmail.com")
Usuario2=Usuario("Luisa","luisa.1998@gmail.com")
Usuario1.cuenta=CuentaBancaria("CuentaDeAhorro",0.01,100)
Usuario2.cuenta=CuentaBancaria("CuentaDeCredito",0.01,0)
Usuario1.hacer_deposito(100)
Usuario2.hacer_deposito(300)

Usuario1.imprimir_info_usuarios()
