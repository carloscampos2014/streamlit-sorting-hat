import streamlit as st
import time

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Chapéu Seletor de Hogwarts",
    page_icon="🧙‍♂️",
    layout="centered"
)

# --- ESTRUTURA DE DADOS DAS PERGUNTAS ---
# Organizar as perguntas desta forma torna o código muito mais limpo.
perguntas = [
    {
        "pergunta": "Qual qualidade você mais valoriza em si mesmo?",
        "opcoes": ("Coragem", "Ambição", "Sabedoria", "Lealdade"),
        "pontos": {
            "Coragem": {"Grifinória": 2},
            "Ambição": {"Sonserina": 2},
            "Sabedoria": {"Corvinal": 2},
            "Lealdade": {"Lufa-Lufa": 2}
        }
    },
    {
        "pergunta": "Se pudesse explorar qualquer lugar em Hogwarts, qual seria?",
        "opcoes": ("A Floresta Proibida", "A Seção Restrita da biblioteca", "As cozinhas de Hogwarts", "A Sala Precisa"),
        "pontos": {
            "A Floresta Proibida": {"Grifinória": 2, "Sonserina": 1},
            "A Seção Restrita da biblioteca": {"Corvinal": 2, "Sonserina": 1},
            "As cozinhas de Hogwarts": {"Lufa-Lufa": 2},
            "A Sala Precisa": {"Grifinória": 1, "Corvinal": 1, "Lufa-Lufa": 1}
        }
    },
    {
        "pergunta": "Qual dos seguintes você preferiria que as pessoas associassem a você após sua morte?",
        "opcoes": ("Glória", "Sabedoria", "Amor", "Poder"),
        "pontos": {
            "Glória": {"Grifinória": 1, "Sonserina": 2},
            "Sabedoria": {"Corvinal": 2},
            "Amor": {"Lufa-Lufa": 2, "Grifinória": 1},
            "Poder": {"Sonserina": 2}
        }
    },
     {
        "pergunta": "Você encontra uma carteira perdida na rua. O que você faz?",
        "opcoes": ("Procura uma identificação para devolver ao dono.", "Leva a uma autoridade, como a polícia.", "Pega o dinheiro e deixa a carteira.", "Ignora e segue seu caminho."),
        "pontos": {
            "Procura uma identificação para devolver ao dono.": {"Lufa-Lufa": 2, "Grifinória": 1},
            "Leva a uma autoridade, como a polícia.": {"Corvinal": 2, "Lufa-Lufa": 1},
            "Pega o dinheiro e deixa a carteira.": {"Sonserina": 2},
            "Ignora e segue seu caminho.": {} # Sem pontos
        }
    }
]

# --- FUNÇÕES AUXILIARES ---
def exibir_resultado(casa):
    """Exibe o brasão e a descrição da casa selecionada."""
    casas_info = {
        "Grifinória": {
            "brasao": "https://i.imgur.com/tS2vY_d.png",
            "descricao": "Parabéns! Você pertence à Grifinória, a casa dos bravos de coração, onde a ousadia, o nervo e o cavalheirismo prevalecem. Sua coragem é a sua maior virtude!"
        },
        "Sonserina": {
            "brasao": "https://i.imgur.com/m26gC_d.png",
            "descricao": "Parabéns! Você pertence à Sonserina, a casa dos astutos e ambiciosos. Você usa de qualquer meio para atingir os fins que estabeleceu e valoriza a grandeza."
        },
        "Corvinal": {
            "brasao": "https://i.imgur.com/dAzpY_d.png",
            "descricao": "Parabéns! Você pertence à Corvinal, a casa das mentes mais aguçadas. Para os de grande espírito e saber, a inteligência e a criatividade são tesouros."
        },
        "Lufa-Lufa": {
            "brasao": "https://i.imgur.com/BDei8_d.png",
            "descricao": "Parabéns! Você pertence à Lufa-Lufa, onde seus membros são justos e leais. Pacientes, sinceros e sem medo da dor, a dedicação é sua marca registrada."
        }
    }
    info = casas_info[casa]
    st.header(f"Sua casa é... {casa}!")
    st.image(info["brasao"], width=200)
    st.success(info["descricao"])
    st.balloons()
    time.sleep(3) # Pausa para os balões aparecerem bem

# --- INICIALIZAÇÃO DO SESSION STATE ---
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
    st.session_state.scores = {"Grifinória": 0, "Sonserina": 0, "Corvinal": 0, "Lufa-Lufa": 0}

# --- LÓGICA PRINCIPAL DO APP ---
st.title("🧙‍♂️ Chapéu Seletor de Hogwarts")

# Verifica se o quiz já terminou
if st.session_state.question_index < len(perguntas):
    # Pega a pergunta atual
    idx = st.session_state.question_index
    pergunta_atual = perguntas[idx]

    st.subheader(f"Pergunta {idx + 1}/{len(perguntas)}")
    st.write(f"### {pergunta_atual['pergunta']}")

    # Cria o radio button para as opções
    # A chave (key) é importante para o Streamlit identificar o widget
    resposta = st.radio(
        "Escolha sua resposta:",
        pergunta_atual['opcoes'],
        key=f"q{idx}"
    )

    # Botão de próxima pergunta
    if st.button("Próxima Pergunta"):
        # Calcula os pontos da resposta escolhida
        pontos_da_resposta = pergunta_atual['pontos'].get(resposta, {})
        for casa, ponto in pontos_da_resposta.items():
            st.session_state.scores[casa] += ponto

        # Avança para a próxima pergunta
        st.session_state.question_index += 1
        st.rerun() # Re-executa o script para mostrar a próxima pergunta

else:
    # Se o quiz terminou, mostra o resultado
    st.write("### O Chapéu Seletor ponderou suas respostas...")
    
    with st.spinner("Hmm, difícil, muito difícil... mas já sei onde colocá-lo..."):
        time.sleep(3) # Simula o pensamento do chapéu

    # Encontra a casa com a maior pontuação
    casa_final = max(st.session_state.scores, key=st.session_state.scores.get)
    exibir_resultado(casa_final)

    # Botão para recomeçar o quiz
    if st.button("Fazer o teste novamente"):
        # Reseta o estado da sessão
        st.session_state.question_index = 0
        st.session_state.scores = {"Grifinória": 0, "Sonserina": 0, "Corvinal": 0, "Lufa-Lufa": 0}
        st.rerun()