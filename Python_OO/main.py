from conta import Conta
from datas import Datas

conta = Conta(123, "Weber", 80.0, 0.0)

# print("O nome do Titular é: {}".format(conta.titular))

# conta.extrato()
# conta.depositar(1000.0)
# conta.extrato()
# conta.sacar(200.0)
# conta.extrato()

# d = Datas(17, 1, 2023)
# d.formatada()

conta2 = Conta(123, "Weber", 50.0, 0.0)
# conta.transferencia(30, conta2)
# print(f'O saldo da conta é R$', conta2.get_recuperaSaldo())
# conta2.set_limite(10000.0)
# print("O valor atual do limite é de R$",conta2.get_limite())

# Método Setter
# conta.limite = 4000
# Método Getter
# print(conta.limite)

print(conta.titular)