DADOS_QUIZ = [
    {
        "pergunta": "Qual qualidade você mais valoriza em si mesmo?",
        "opcoes": ("Coragem", "Ambição", "Sabedoria", "Lealdade"),
        "pontos": {
            "Coragem": {"Grifinória": 2},
            "Ambição": {"Sonserina": 2},
            "Sabedoria": {"Corvinal": 2},
            "Lealdade": {"Lufa-Lufa": 2},
        },
    },
    {
        "pergunta": "Se pudesse explorar qualquer lugar em Hogwarts, qual seria?",
        "opcoes": (
            "A Floresta Proibida",
            "A Seção Restrita da biblioteca",
            "As cozinhas de Hogwarts",
            "A Sala Precisa",
        ),
        "pontos": {
            "A Floresta Proibida": {"Grifinória": 2, "Sonserina": 1},
            "A Seção Restrita da biblioteca": {"Corvinal": 2, "Sonserina": 1},
            "As cozinhas de Hogwarts": {"Lufa-Lufa": 2},
            "A Sala Precisa": {"Grifinória": 1, "Corvinal": 1, "Lufa-Lufa": 1},
        },
    },
    {
        "pergunta": "Qual dos seguintes você preferiria que as pessoas associassem a você após sua morte?",
        "opcoes": ("Glória", "Sabedoria", "Amor", "Poder"),
        "pontos": {
            "Glória": {"Grifinória": 1, "Sonserina": 2},
            "Sabedoria": {"Corvinal": 2},
            "Amor": {"Lufa-Lufa": 2, "Grifinória": 1},
            "Poder": {"Sonserina": 2},
        },
    },
    {
        "pergunta": "Você encontra uma carteira perdida na rua. O que você faz?",
        "opcoes": (
            "Procura uma identificação para devolver ao dono.",
            "Leva a uma autoridade, como a polícia.",
            "Pega o dinheiro e deixa a carteira.",
            "Ignora e segue seu caminho.",
        ),
        "pontos": {
            "Procura uma identificação para devolver ao dono.": {
                "Lufa-Lufa": 2,
                "Grifinória": 1,
            },
            "Leva a uma autoridade, como a polícia.": {"Corvinal": 2, "Lufa-Lufa": 1},
            "Pega o dinheiro e deixa a carteira.": {"Sonserina": 2},
            "Ignora e segue seu caminho.": {},  # Sem pontos
        },
    },
    {
        "pergunta": "Você entra em uma sala com quatro objetos mágicos. Qual você escolhe?",
        "opcoes": (
            "Uma espada antiga e ornamentada",
            "Um diário com páginas em branco que responde a perguntas",
            "Um medalhão com um poder desconhecido e misterioso",
            "Um cálice de ouro que promove a amizade entre quem bebe dele",
        ),
        "pontos": {
            "Uma espada antiga e ornamentada": {"Grifinória": 2},
            "Um diário com páginas em branco que responde a perguntas": {
                "Corvinal": 2,
                "Sonserina": 1,
            },
            "Um medalhão com um poder desconhecido e misterioso": {"Sonserina": 2},
            "Um cálice de ouro que promove a amizade entre quem bebe dele": {
                "Lufa-Lufa": 2
            },
        },
    },
    {
        "pergunta": "Um trasgo montanhês invadiu Hogwarts! O que você faz?",
        "opcoes": (
            "Corro para enfrentá-lo e proteger os outros alunos",
            "Observo de longe e tento encontrar um ponto fraco ou uma armadilha inteligente",
            "Procuro um professor o mais rápido possível e alerto a todos",
            "Uso a distração para garantir minha própria segurança primeiro",
        ),
        "pontos": {
            "Corro para enfrentá-lo e proteger os outros alunos": {"Grifinória": 2},
            "Observo de longe e tento encontrar um ponto fraco ou uma armadilha inteligente": {
                "Corvinal": 2
            },
            "Procuro um professor o mais rápido possível e alerto a todos": {
                "Lufa-Lufa": 2,
                "Grifinória": 1,
            },
            "Uso a distração para garantir minha própria segurança primeiro": {
                "Sonserina": 2
            },
        },
    },
    {
        "pergunta": "Se você pudesse criar uma poção, qual seria o seu efeito?",
        "opcoes": (
            "Poção da Sorte (Felix Felicis)",
            "Poção da Cura (Wiggenweld)",
            "Poção da Verdade (Veritaserum)",
            "Poção Polissuco (para se transformar em outros)",
        ),
        "pontos": {
            "Poção da Sorte (Felix Felicis)": {"Sonserina": 2, "Grifinória": 1},
            "Poção da Cura (Wiggenweld)": {"Lufa-Lufa": 2, "Grifinória": 1},
            "Poção da Verdade (Veritaserum)": {"Corvinal": 2, "Lufa-Lufa": 1},
            "Poção Polissuco (para se transformar em outros)": {
                "Sonserina": 1,
                "Corvinal": 1,
            },
        },
    },
    {
        "pergunta": "Qual matéria em Hogwarts mais lhe interessaria?",
        "opcoes": (
            "Defesa Contra as Artes das Trevas",
            "Poções",
            "Feitiços",
            "Herbologia",
        ),
        "pontos": {
            "Defesa Contra as Artes das Trevas": {"Grifinória": 2},
            "Poções": {"Sonserina": 2, "Corvinal": 1},
            "Feitiços": {"Corvinal": 2, "Lufa-Lufa": 1},
            "Herbologia": {"Lufa-Lufa": 2},
        },
    },
    {
        "pergunta": "Você vê um aluno mais velho zombando de um aluno do primeiro ano. Qual é a sua reação?",
        "opcoes": (
            "Intervenho diretamente, mesmo que o aluno mais velho seja mais forte.",
            "Uso um feitiço inteligente ou uma distração para tirar o aluno mais novo da situação sem confronto direto.",
            "Reúno meus amigos para confrontar o agressor em grupo ou conto a um monitor.",
            "Observo para entender a dinâmica de poder antes de agir, se agir.",
        ),
        "pontos": {
            "Intervenho diretamente, mesmo que o aluno mais velho seja mais forte.": {
                "Grifinória": 2
            },
            "Uso um feitiço inteligente ou uma distração para tirar o aluno mais novo da situação sem confronto direto.": {
                "Corvinal": 2,
                "Grifinória": 1,
            },
            "Reúno meus amigos para confrontar o agressor em grupo ou conto a um monitor.": {
                "Lufa-Lufa": 2
            },
            "Observo para entender a dinâmica de poder antes de agir, se agir.": {
                "Sonserina": 2
            },
        },
    },
    {
        "pergunta": "O que você mais busca em uma amizade?",
        "opcoes": (
            "Lealdade incondicional, aconteça o que acontecer.",
            "Estímulo intelectual e debates interessantes.",
            "Conexões poderosas que podem me ajudar a alcançar meus objetivos.",
            "Aventuras emocionantes e alguém que me apoie nos desafios.",
        ),
        "pontos": {
            "Lealdade incondicional, aconteça o que acontecer.": {"Lufa-Lufa": 2},
            "Estímulo intelectual e debates interessantes.": {"Corvinal": 2},
            "Conexões poderosas que podem me ajudar a alcançar meus objetivos.": {
                "Sonserina": 2
            },
            "Aventuras emocionantes e alguém que me apoie nos desafios.": {
                "Grifinória": 2
            },
        },
    },
]
