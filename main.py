# Nessa aula usamos o Console do Python para criar os objetos e chamar seus métodos.
# Abaixo um exemplo dos chamados feitos.

from conta import Conta


conta1 = Conta(123, "Nico", 55.0, 1000.0)
conta1.extrato()
conta1.saca(55)
conta1.extrato()
conta1.deposita(100)
conta1.extrato()
conta1.saca(1500)
conta1.extrato()

conta2 = Conta(321, "Marco", 100.0, 1000.0)
conta1.extrato()
conta2.extrato()
conta2.transfere(50.0, conta1)
conta1.extrato()
conta2.extrato()