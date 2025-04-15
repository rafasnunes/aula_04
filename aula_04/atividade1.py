''''''

valor_compra = float(input('Entre com o valor da compra: R$ '))

if (valor_compra > 250.0):
    valor_desconto = (valor_compra * 0.16)
    print('Desconto aplicado: R$', valor_desconto)
    print('Total da Compra: R$', valor_compra - valor_desconto)
else:
    (print('Total a pagar: R$', valor_compra))

