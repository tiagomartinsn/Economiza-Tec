from estoque import estoque

esto = estoque()
totalBalanco = 0.0
totalarrecadado = 0.0

while True:
    print '= = = = Bemvindo(a) ao EconomizaTec = = = = \n'
    print 'Digite a apcao desejada:'
    print 'Cadastrar um Produto: 1 '
    print 'Vender um Produto: 2'
    print 'Imprimir Balanco: 3'
    print 'Sair: 4'
    try:
        opcao = int(raw_input('Opcao: '))
    except:
        print 'Valor invalido, tente novamente'
        continue
    if opcao == 1:
        while True:
            print '= = = = Cadastro de Produtos = = = = \n'
            nome_produto = raw_input('Digite o nome do produto: ')
            try:
                valor_produto = float(raw_input('Digite o preco unitario do produto: '))
                if valor_produto <= 0:
                    print '\n Valor invalido \n'
                    continue
            except:
                print '\n Valor invalido, tente novamente \n'
                continue
            tipo_produto = raw_input('Digite o tipo do produto: ')
            try:
                estoque = int(raw_input('Digite a quantidade no estoque: '))

                if estoque <= 0:
                    print 'Valor invalido'
                    continue
            except:
                print 'Valor invalido, tente novamente'
                continue

            esto.cadastrar(nome_produto, valor_produto, tipo_produto,estoque)
            print " "
            novo_cadastro = raw_input('Deseja cadastrar outro produto ?')
            if novo_cadastro.upper() == 'SIM':
                continue
            else:
                break
    elif opcao == 2:
        while True:
            print '= = = = Venda de Produtos = = = = \n'
            nome_pro_vend = raw_input('Digite o nome do produto: ')

            totalBalanco += esto.vender(nome_pro_vend)

            print " "
            nova_venda = raw_input('Deseja vender outro produto ?')
            if nova_venda.upper() == 'SIM':
                continue
            else:
                break
    elif opcao == 3:
        while True:
            print '= = = = Impressao de Balanco = = = = \n'
            print 'Produtos cadastrados: \n '
            esto.impressao(totalBalanco)
            nova_consulta = raw_input('Deseja realizar outra consulta ?')
            if nova_consulta.upper() == 'SIM':
                continue
            else:
                break
    elif opcao == 4:
        break
    elif opcao not in (1,2,3,4):
        print 'Valor invalido, tente novamente'
        continue