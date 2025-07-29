
import nltk
import pickle
from collections import defaultdict

def aprender_padroes(texto):
    
    modelo = defaultdict(list)
    palavras = nltk.word_tokenize(texto.lower(), language='portuguese')
    
    for i in range(len(palavras) - 1):
        palavra_atual = palavras[i]
        proxima_palavra = palavras[i + 1]
        modelo[palavra_atual].append(proxima_palavra)
    
    return modelo

if __name__ == "__main__":
    arquivo_corpus = "corpus.txt"
    arquivo_modelo = "modelo_treinado.pkl" 
    
    try:
        print(f"Lendo o arquivo de corpus '{arquivo_corpus}'...")
        with open(arquivo_corpus, 'r', encoding='utf-8') as f:
            texto = f.read()
            
        print("Iniciando o treinamento do modelo...")
        modelo = aprender_padroes(texto)
        
        print(f"Treinamento concluído! Salvando o modelo em '{arquivo_modelo}'...")
        
        with open(arquivo_modelo, 'wb') as f:
            pickle.dump(modelo, f)
            
        print("Modelo salvo com sucesso!")

    except FileNotFoundError:
        print(f"ERRO: Arquivo de corpus '{arquivo_corpus}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")