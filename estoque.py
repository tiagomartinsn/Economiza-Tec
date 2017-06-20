from produto import produtos

class estoque:
    def __init__(self):
        self.listaP = []
        self.total = 0.0

    def cadastrar(self,produto, valor, tipo,quant_estoque):
        if len(self.listaP) == 0:
            pro = produtos(produto, valor, tipo, quant_estoque)
            self.listaP.append(pro)
            print '\n %s cadastrado com sucesso \n' % pro.getProduto()
            print '%d %s(s) cadastrado(s) com sucesso' % (pro.getQuant(), pro.getProduto())
        else:
            existe = False
            for i in range(len(self.listaP)):
                if self.listaP[i].getProduto() == produto:
                    print '%s ja cadastrado no sistema'%produto
                    existe = True
                    break
            if existe == False:
                pro = produtos(produto, valor, tipo, quant_estoque)
                self.listaP.append(pro)
                print '%s cadastrado com sucesso' % pro.getProduto()
                print '%d %s(s) cadastrado(s) com sucesso' % (pro.getQuant(), pro.getProduto())

    def vender (self,produto_vendido):
        total = 0
        existe = False

        teste = False
        for i in range(len(self.listaP)):
            if self.listaP[i].getProduto() == produto_vendido:
                print '==> %s (%s). R$%.2f'%(self.listaP[i].getProduto(),self.listaP[i].getTipo(),self.listaP[i].getValor())
                print " "
                quant_vendido = int(raw_input('Digite a quantidade que deseja vender: '))
                estoque = self.listaP[i].getQuant()
                teste = False
                if quant_vendido <= 0:
                    print 'Valor invalido'
                    teste = True
                    continue
                elif estoque < quant_vendido:
                    print 'Nao e possivel vender pois nao ha %s suficiente'%produto_vendido
                else:
                    estoque -= quant_vendido
                    self.listaP[i].setQuant(estoque)
                    total = quant_vendido * self.listaP[i].getValor()
                    print '==> Total arrecadado: R$%.2f '% total
                existe = True
                break
        if existe == False and teste == False :
            print produto_vendido + ' nao cadastrado(a) no sistema.'
        return total

    def impressao(self,total):
        for i in range(len(self.listaP)):
            print '     %d) %s (%s). R$ %.2f' % ((i+1),self.listaP[i].getProduto(), self.listaP[i].getTipo(), self.listaP[i].getValor())
            print '     Restante: %d'%self.listaP[i].getQuant()
            print '         '
            self.total += self.listaP[i].getValor() * self.listaP[i].getQuant()
        print '     Total arrecadado em vendas: R$%.2f \n ' % total