from conta import Conta
from datas import Datas

conta = Conta(123, "Weber", 80.0, 1000.0)

#print("O nome do Titular é: {}".format(conta.titular))

#conta.extrato()
#conta.depositar(1000.0)
#conta.extrato()
#conta.sacar(200.0)
#conta.extrato()

#d = Datas(17, 1, 2023)
#d.formatada()

conta2 = Conta(123, "Weber", 50.0, 1000.0)

conta.transferencia(30, conta2)

conta.extrato()
conta2.extrato()