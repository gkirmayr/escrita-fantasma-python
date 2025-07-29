 Escritor Fantasma - Gerador de Texto Estilo Markov
Um projeto em Python que analisa o estilo de escrita de um texto e gera novas frases que imitam esse estilo, baseado em Cadeias de Markov.

Este projeto foi desenvolvido como um exercício prático de Processamento de Linguagem Natural (PLN). Ele é capaz de aprender os padrões de sequência de palavras de qualquer texto em português (um "corpus") e, em seguida, gerar sentenças novas e pseudo-aleatórias que soam como se tivessem sido escritas pelo autor original.

🚀 Funcionalidades
Módulo de Treinamento (treinar.py): Lê um arquivo de texto grande, processa-o com NLTK e cria um modelo estatístico dos padrões de palavras.

Modelo Persistente: O "cérebro" treinado é salvo em um arquivo (.pkl) usando a biblioteca pickle, evitando a necessidade de retreinar a cada execução.

Módulo de Geração (gerar.py): Carrega o modelo pré-treinado e entra em um modo interativo.

Geração Interativa: Os usuários podem gerar novas frases simplesmente teclando Enter, com a opção de sair digitando 'sair'.

Comprimento de Frase Variável: As frases geradas têm um comprimento aleatório para parecerem mais naturais.

🛠️ Tecnologias Utilizadas
Python 3

NLTK (Natural Language Toolkit): Para tokenização de texto (a quebra inteligente de texto em palavras).

Pickle: Para serialização e desserialização do modelo treinado (salvar e carregar o "cérebro").

⚙️ Como Usar
Siga os passos abaixo para executar o projeto em sua máquina local.

# ✍️ Escritor Fantasma - Gerador de Texto Estilo Markov

> Um projeto em Python que analisa o estilo de escrita de um texto e gera novas frases que imitam esse estilo, baseado em Cadeias de Markov.

Este projeto foi desenvolvido como um exercício prático de Processamento de Linguagem Natural (PLN). Ele é capaz de aprender os padrões de sequência de palavras de qualquer texto em português (um "corpus") e, em seguida, gerar sentenças novas e pseudo-aleatórias que soam como se tivessem sido escritas pelo autor original.

## 🚀 Funcionalidades

* **Módulo de Treinamento (`treinar.py`):** Lê um arquivo de texto grande, processa-o com NLTK e cria um modelo estatístico dos padrões de palavras.
* **Modelo Persistente:** O "cérebro" treinado é salvo em um arquivo (`.pkl`) usando a biblioteca `pickle`, evitando a necessidade de retreinar a cada execução.
* **Módulo de Geração (`gerar.py`):** Carrega o modelo pré-treinado e entra em um modo interativo.
* **Geração Interativa:** Os usuários podem gerar novas frases simplesmente teclando Enter, com a opção de sair digitando 'sair'.
* **Comprimento de Frase Variável:** As frases geradas têm um comprimento aleatório para parecerem mais naturais.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **NLTK (Natural Language Toolkit):** Para tokenização de texto (a quebra inteligente de texto em palavras).
* **Pickle:** Para serialização e desserialização do modelo treinado (salvar e carregar o "cérebro").

## ⚙️ Como Usar

Siga os passos abaixo para executar o projeto em sua máquina local.

### Pré-requisitos

* Python 3.x instalado
* `pip` (gerenciador de pacotes do Python)

### Instalação e Configuração

1.  **Baixe o código:**
    Baixe os arquivos (`treinar.py`, `gerar.py`) para uma pasta em seu computador.

2.  **Crie um Ambiente Virtual (Recomendado):**
    É uma boa prática isolar as dependências do projeto. No terminal, dentro da pasta do projeto, execute:
    ```bash
    # Cria o ambiente virtual
    python -m venv venv
    # Ativa o ambiente (Windows)
    .\venv\Scripts\activate
    # Ativa o ambiente (Mac/Linux)
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    Com o ambiente virtual ativado, instale as bibliotecas listadas no `requirements.txt` com um único comando:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Baixe os dados do NLTK:**
    Você só precisa fazer isso uma vez. Execute o seguinte comando no terminal:
    ```bash
    python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"
    ```

### Execução

O projeto é dividido em duas etapas:

**Etapa 1: Treinar o Modelo**

Primeiro, você precisa treinar o modelo com algum texto.

* Coloque um arquivo de texto (ex: `corpus.txt`) na pasta do projeto.
* No script `treinar.py`, certifique-se de que a variável `arquivo_corpus` aponta para o seu arquivo.
* Execute o script de treinamento:
    ```bash
    python treinar.py
    ```
    Isso irá ler o corpus e criar o arquivo `modelo_treinado.pkl`.

**Etapa 2: Gerar Frases**

Uma vez que o modelo está treinado, você pode gerar frases quantas vezes quiser:

* Execute o script de geração:
    ```bash
    python gerar.py
    ```
* O programa carregará o modelo e exibirá a primeira frase.
* Pressione **Enter** para gerar uma nova frase ou digite **`sair`** para encerrar.

## 📁 Estrutura do Projeto
