
import pickle
import random

def gerar_frase(modelo, comprimento=16):
    
    palavras_iniciais = list(modelo.keys())
    if not palavras_iniciais:
        return "O modelo está vazio."

    palavra_atual = random.choice(palavras_iniciais)
    frase = [palavra_atual]
    
    for _ in range(comprimento - 1):
        possiveis_seguintes = modelo.get(palavra_atual)
        if not possiveis_seguintes:
            break
        proxima_palavra = random.choice(possiveis_seguintes)
        frase.append(proxima_palavra)
        palavra_atual = proxima_palavra
        
    return " ".join(frase).capitalize() + "."

if __name__ == "__main__":
    arquivo_modelo = "modelo_treinado.pkl"
    
    try:
       
        print(f"Carregando o modelo treinado de '{arquivo_modelo}'...")
        with open(arquivo_modelo, 'rb') as f:
            modelo = pickle.load(f)
        print("Modelo carregado com sucesso! Vamos começar.")
        print("-" * 30)

        # Loop interativo para gerar frases
        while True:
            frase_gerada = gerar_frase(modelo, random.randint(20, 30))
            print(f"> {frase_gerada}")
            
            # Espera a interação do usuário
            entrada = input("\nPressione Enter para gerar outra frase ou digite 'sair': ")
            if entrada.lower() == 'sair':
                break
            print("-" * 30)

    except FileNotFoundError:
        print(f"ERRO: Arquivo de modelo '{arquivo_modelo}' não encontrado!")
        print("Por favor, execute o script 'treinar.py' primeiro para criar o modelo.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")