def recursao(numero):
	# uma FUNÇÃO RECURSIVA CHAMA ela MESMA ate que a CONDIÇÃO seja ATINGIDA.
	if numero == 1:	# PONTO de PARADA da RECURSÃO
		return numero	# RESULTADO da FUNÇÃO
	#
	#
	return numero + recursao(numero - 1)

''' OUTRAS APLICAÇÕES '''
def mdc(alto, baixo):
	if baixo == 0:
		return alto
	return mdc(baixo, alto%baixo)


def mmc(baixo, alto):
	return int(baixo / mdc(baixo, alto)) * alto

if __name__ == "__main__":
	print(f"FUNÇÃO EXEMPLO: {recursao(5)}")
	print(f"Maior Divisor Comum: {mdc(98, 56)}")
	print(f"Minimo Multiplo Comum: {mmc(15, 20)}")