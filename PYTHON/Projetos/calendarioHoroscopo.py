dia = int(input("ENTRE com o DIA de ANIVERSARIO: "))
mes = input("ENTRE com o MES de ANIVERSARIO por EXTENSO: ")

if mes == 'dezembro':
	signoAstral = 'Sagitário' if (dia < 22) else 'Capricornio'
elif mes == 'janeiro':
	signoAstral = 'Capricornio' if (dia < 20) else 'Aquario'
elif mes == 'fevereiro':
	signoAstral = 'Aquario' if (dia < 19) else 'Peixes'
elif mes == 'marco':
	signoAstral = 'Peixes' if (dia < 21) else 'Aries'
elif mes == 'abril':
	signoAstral = 'Aries' if (dia < 20) else 'Touro'
elif mes == 'maio':
	signoAstral = 'Touro' if (dia < 21) else 'Gemeos'
elif mes == 'junho':
	signoAstral = 'Gemeos' if (dia < 21) else 'Cancer'
elif mes == 'julho':
	signoAstral = 'Cancer' if (dia < 23) else 'Leao'
elif mes == 'agosto':
	signoAstral = 'Leao' if (dia < 23) else 'Virgem'
elif mes == 'setembro':
	signoAstral = 'Virgem' if (dia < 23) else 'Libra'
elif mes == 'outubro':
	signoAstral = 'Libra' if (dia < 23) else 'Escorpiao'
elif mes == 'novembro':
	signoAstral = 'Escorpiao' if (dia < 22) else 'Sagitario'
print(f'seu SIGNO ASTROLOGICO é: {signoAstral}')