from PackNovo.dados import dadospy
from PackNovo.leia.leia import leiavalor

valor = leiavalor('Digite um valor: R$ ')

dadospy.resumo(valor, valorma=80, valorme=35)