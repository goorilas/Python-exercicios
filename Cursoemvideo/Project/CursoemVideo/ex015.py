km = float(input('Kilometros percorridos: Km  '))
dias = int(input('Quantos dias foi alugado: '))
diaria_carro = 60
kmrodado = 0.15
print( 'O valor do aluguel do veiculo a ser pago é: {:.2f}' .format(km * kmrodado + diaria_carro * dias))
# ou tbm pode se fazer   pago = (dias * 60) + (km * 0.15), assim tirando a diaria carro e o kmrodado.