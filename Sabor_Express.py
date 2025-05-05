import os

restaurantes = [
    {'nome': 'Praça', 'Categoria': 'Japonesa', 'Ativo': False},
    {'nome': 'Pizza Suprema', 'Categoria': 'Pizza', 'Ativo': True},
    {'nome': 'Pizza Hut', 'Categoria': 'Italiana', 'Ativo': False}]

def exibir():
    exibr_subtitulo('Sabor Express')

def exibr_subtitulo(texto):
    print('=' * 50)
    print(f'{texto}'.center(50))
    print('=' * 50)

def finalizar():
    exibr_subtitulo('Finalizando o Programa')

def opcao_invalida():
    print('Opção invalida\n')
    menu_principal()

def menu_principal():
    input('\nDigite uma tecla para voltar ao Menu inicial: ')
    main()

def opcoes():
    print('''[1] Cadastrar Restaurante
    [2] Listar Restaurante 
    [3] Alternar estado do restaurante
    [4] Sair''')

def cadastrar_restaurante():
    '''Essa função cadastra um novo restaurante'''
    exibr_subtitulo('Cadastrar Restaurante')
    nome_restaurante = input('Nome do Restaurante: ')
    categoria = input(f'Categoria do {nome_restaurante}: ')
    dados_restaurante = {'nome': nome_restaurante, 'Categoria': categoria, 'Ativo': False}
    restaurantes.append(dados_restaurante) #adicona um novo restautante na lista
    print(f'{nome_restaurante} cadastrado com sucesso\n')
    menu_principal()

def listar_restaurante():
    '''Essa função lista todos os restaurantes cadastrados'''
    exibr_subtitulo('Listando Restaurante')

    #Criando subtitulo na tabela
    print(f'{'Nome do Restaurante'.ljust(21)} | {'Categoria'.ljust(21)} | {"Ativo"}')
    print('='*55)
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['Categoria']
        ativo = 'Ativado' if restaurante['Ativo'] else 'Desativado'
        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    menu_principal()

def estado_restaurante():
    '''Essa função altera o estado de um restaurante'''
    exibr_subtitulo('Alterando o estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['Ativo'] = not restaurante['Ativo']

            if restaurante['Ativo']:
                print(f'O Restaurante {nome_restaurante} foi ativado com sucesso')
            else:
                print(f'O Restaurante {nome_restaurante} foi desativado com sucesso')
            break
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    menu_principal()

def escolher_opcoes():
    try:
        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            cadastrar_restaurante()
        elif opcao == 2:
            listar_restaurante()
        elif opcao == 3:
            estado_restaurante()
        elif opcao == 4:
            finalizar()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir()
    opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()