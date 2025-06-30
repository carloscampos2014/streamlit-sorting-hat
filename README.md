# 🧙‍♂️ Chapéu Seletor de Hogwarts com Streamlit

Este é um aplicativo web interativo inspirado no Chapéu Seletor do universo Harry Potter. O objetivo é descobrir, por meio de um quiz, a qual casa de Hogwarts (Grifinória, Lufa-Lufa, Corvinal ou Sonserina) o usuário pertence, com base em suas respostas.

O projeto foi desenvolvido como um exercício prático de Python e Streamlit, demonstrando como criar aplicações web rápidas, dinâmicas e divertidas.

---

## ✨ Funcionalidades

- **Quiz Personalizado:** Perguntas baseadas nos valores e características das casas de Hogwarts.
- **Sistema de Pontuação:** Cada resposta soma pontos para uma ou mais casas, determinando a afinidade do usuário.
- **Resultado Interativo:** Exibição do brasão, nome e descrição da casa sorteada, tornando a experiência mais imersiva.
- **Interface Intuitiva:** Layout simples, responsivo e fácil de usar, criado com Streamlit.

---

## 🛠️ Tecnologias Utilizadas

- **[Python](https://www.python.org/):** Linguagem principal do projeto.
- **[Streamlit](https://streamlit.io/):** Framework para desenvolvimento de interfaces web de forma rápida e interativa.

---

## 🚀 Como Executar o Projeto Localmente

Siga os passos abaixo para rodar o Chapéu Seletor em sua máquina:

1. **Clone o repositório:**
```bash
git clone https://github.com/carloscampos2014/streamlit-sorting-hat.git
    cd streamlit-sorting-hat
```
2. **(Opcional) Crie um ambiente virtual:**
```bash
python -m venv venv
# Ative o ambiente virtual:
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
```
3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```
4. **Execute o aplicativo:**
```bash
streamlit run chapeu_seletor.py
```
5. **Acesse no navegador:**
    Abra [http://localhost:8501](http://localhost:8501) para interagir com o quiz.

---

## 📁 Estrutura dos Arquivos

- `chapeu_seletor.py`: Código principal do aplicativo Streamlit.
- `perguntas.py`: Lista de perguntas e lógica de pontuação.
- `requirements.txt`: Dependências do projeto.
- `README.md`: Este arquivo de instruções.
- `LICENSE`: Licença do projeto.

---

## ❓ Dúvidas ou Sugestões

Fique à vontade para abrir uma _issue_ ou enviar um _pull request_ com melhorias, correções ou sugestões.

---

## 📄 Licença

Distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.
