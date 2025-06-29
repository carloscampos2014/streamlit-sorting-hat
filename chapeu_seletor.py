import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Chapéu Seletor de Hogwarts",
    page_icon="🧙‍♂️",
    layout="centered"
)

# --- LÓGICA E CONTEÚDO ---

def calcular_resultado(respostas):
    """Calcula a casa com base nas respostas do usuário."""
    pontos = {"Grifinória": 0, "Sonserina": 0, "Corvinal": 0, "Lufa-Lufa": 0}

    # Lógica de pontuação para cada pergunta
    if respostas["q1"] == "Coragem":
        pontos["Grifinória"] += 2
    elif respostas["q1"] == "Ambição":
        pontos["Sonserina"] += 2
    elif respostas["q1"] == "Sabedoria":
        pontos["Corvinal"] += 2
    elif respostas["q1"] == "Lealdade":
        pontos["Lufa-Lufa"] += 2

    if respostas["q2"] == "A Floresta Proibida":
        pontos["Grifinória"] += 2
        pontos["Sonserina"] += 1
    elif respostas["q2"] == "A Seção Restrita da biblioteca":
        pontos["Corvinal"] += 2
        pontos["Sonserina"] += 1
    elif respostas["q2"] == "As cozinhas de Hogwarts":
        pontos["Lufa-Lufa"] += 2
    elif respostas["q2"] == "A Sala Precisa":
        pontos["Grifinória"] += 1
        pontos["Corvinal"] += 1

    if respostas["q3"] == "Glória":
        pontos["Sonserina"] += 2
        pontos["Grifinória"] += 1
    elif respostas["q3"] == "Sabedoria":
        pontos["Corvinal"] += 2
    elif respostas["q3"] == "Amor":
        pontos["Lufa-Lufa"] += 2
        pontos["Grifinória"] += 1
    elif respostas["q3"] == "Poder":
        pontos["Sonserina"] += 2

    # Encontra a casa com a maior pontuação
    casa_selecionada = max(pontos, key=pontos.get)
    return casa_selecionada, pontos

def exibir_resultado(casa):
    """Exibe o brasão e a descrição da casa selecionada."""
    casas_info = {
        "Grifinória": {
            "brasao": "./imagens/Grifinoria.jpeg",
            "descricao": "Parabéns! Você pertence à Grifinória, a casa dos bravos de coração, onde a ousadia, o nervo e o cavalheirismo prevalecem. Sua coragem é a sua maior virtude!"
        },
        "Sonserina": {
            "brasao": "./imagens/Sonserina.jpeg",
            "descricao": "Parabéns! Você pertence à Sonserina, a casa dos astutos e ambiciosos. Você usa de qualquer meio para atingir os fins que estabeleceu e valoriza a grandeza."
        },
        "Corvinal": {
            "brasao": "./imagens/Corvinal.jpeg",
            "descricao": "Parabéns! Você pertence à Corvinal, a casa das mentes mais aguçadas. Para os de grande espírito e saber, a inteligência e a criatividade são tesouros."
        },
        "Lufa-Lufa": {
            "brasao": "./imagens/LufaLufa.jpeg",
            "descricao": "Parabéns! Você pertence à Lufa-Lufa, onde seus membros são justos e leais. Pacientes, sinceros e sem medo da dor, a dedicação é sua marca registrada."
        }
    }
    info = casas_info[casa]
    st.header(f"Sua casa é... {casa}!")
    st.image(info["brasao"], width=200)
    st.success(info["descricao"])
    st.balloons()


# --- INTERFACE DO USUÁRIO ---

st.title("🧙‍♂️ Chapéu Seletor de Hogwarts")
st.markdown("Responda às perguntas com sinceridade para descobrir a qual casa você pertence.")

respostas = {}

# Pergunta 1
st.subheader("1. Qual qualidade você mais valoriza em si mesmo?")
respostas["q1"] = st.radio(
    "Escolha uma opção:",
    ("Coragem", "Ambição", "Sabedoria", "Lealdade"),
    key="q1",
    label_visibility="collapsed"
)

# Pergunta 2
st.subheader("2. Se pudesse explorar qualquer lugar em Hogwarts, qual seria?")
respostas["q2"] = st.radio(
    "Escolha uma opção:",
    ("A Floresta Proibida", "A Seção Restrita da biblioteca", "As cozinhas de Hogwarts", "A Sala Precisa"),
    key="q2",
    label_visibility="collapsed"
)

# Pergunta 3
st.subheader("3. Qual dos seguintes você preferiria que as pessoas associassem a você após sua morte?")
respostas["q3"] = st.radio(
    "Escolha uma opção:",
    ("Glória", "Sabedoria", "Amor", "Poder"),
    key="q3",
    label_visibility="collapsed"
)

st.write("---")

# Botão para iniciar a seleção
if st.button("O Chapéu Seletor decide agora!"):
    with st.spinner("Hmm, difícil, muito difícil... Vejo muita coragem... uma mente brilhante também... há talento... e uma sede de provar seu valor... mas onde devo colocá-lo?"):
        casa_final, pontuacao = calcular_resultado(respostas)
        exibir_resultado(casa_final)