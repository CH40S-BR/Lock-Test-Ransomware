import base64

def colorir(texto, cor):
    cores = {
        "vermelho": "\033[91m",
        "amarelo": "\033[93m",
        "verde": "\033[92m",
        "azul": "\033[94m",
        "reset": "\033[0m",
    }
    return f"{cores.get(cor, '')}{texto}{cores['reset']}"

print(colorir(r"""
 _     ____  ____  _  __  
/ \   /  _ \/   _\/ |/ /  
| |   | / \||  /  |   /               .-""-.     
| |_/\| \_/||  \__|   \              / .--. \
\____/\____/\____/\_|\_\            / /    \ \       
                                    | |    | |
 _____  _____ ____  _____           | |.-""-.|
/__ __\/  __// ___\/__ __\         ///`.::::.`\
  / \  |  \  |    \  / \          ||| ::/  \:: ;
  | |  |  /_ \___ |  | |          ||; ::\__/:: ;
  \_/  \____\\____/  \_/           \\\ '::::' /
                                    `=':-..-'`
""", "vermelho"))

def criptografar_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'rb') as file:
        conteudo = file.read()

    arquivo_criptografado = base64.b64encode(conteudo)

    with open(caminho_arquivo, 'wb') as file:
        file.write(arquivo_criptografado)

def descriptografar_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'rb') as file:
        arquivo_criptografado = file.read()

    arquivo_descriptografado = base64.b64decode(arquivo_criptografado)
    
    with open(caminho_arquivo, 'wb') as file:
        file.write(arquivo_descriptografado)

def exibir_menu():
    print(colorir("+-----------------------------+", "vermelho"))
    print(colorir("|       LOCK-TEST MENU       |", "vermelho"))
    print(colorir("+-----------------------------+", "vermelho"))
    print(colorir("| [1] Criptografar arquivo   |", "amarelo"))
    print(colorir("| [2] Descriptografar arquivo|", "amarelo"))
    print(colorir("| [0] Sair                   |", "amarelo"))
    print(colorir("+-----------------------------+", "vermelho"))
    return input(colorir("Escolha uma opção: ", "verde"))

while True:
    opcao = exibir_menu()
    if opcao == "1":
        criptografar_arquivo("archive.txt")
        print(colorir("ARQUIVO CRIPTOGRAFADO COM SUCESSO!\n", "verde"))
    elif opcao == "2":
        descriptografar_arquivo("archive.txt")
        print(colorir("ARQUIVO DESCRIPTOGRAFADO COM SUCESSO!\n", "verde"))
    elif opcao == "0":
        print(colorir("Encerrando o programa. Até logo!", "azul"))
        break
    else:
        print(colorir("Opção inválida. Por favor, escolha novamente.\n", "vermelho"))