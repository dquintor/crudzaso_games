
'''Banco de preguntas. 
Las preguntas estan alojadas en diccionarios, cada diccionario tiene tres claves: 
1. texto: el valor corresponde a la pregunta que estamos haciendo 
2. opciones: es una lista con las opciones de respuesta que se le proporcionan al usuario
3. correcta : el valor corresponde al indice de la respuesta correcta en la lista "opciones" 

Los diccionarios de cada pregunta estan alojados en tres listas: 
1. preguntas_faciles: preguntas de menor dificultad
2. preguntas_intermedias: preguntas de dificultad media
3. preguntas_dificiles: preguntas de mayor dificultad '''

#PREGUNTAS DE INGLES 

preguntas_faciles_ingles = [
    {
        "texto": "Which one is correct?",
        "opciones": ["I am agree", "I agree", "I'm agree", "I am in agree"],
        "correcta": 1
    },
    {
        "texto": "Choose the correct translation: 'Tengo 20 años'",
        "opciones": ["I have 20 years", "I am 20 years", "I am 20", "I have 20"],
        "correcta": 2
    },
    {
        "texto": "Which sentence is correct?",
        "opciones": ["She don't like coffee", "She doesn't like coffee", "She doesn't likes coffee", "She not like coffee"],
        "correcta": 1
    },
    {
        "texto": "Pick the natural one:",
        "opciones": ["Can you help me?", "You can help me?", "You can help me no?", "You help me?"],
        "correcta": 0
    },
    {
        "texto": "What’s the plural of 'child'?",
        "opciones": ["childs", "childes", "children", "childrens"],
        "correcta": 2
    },
    {
        "texto": "Choose the correct option:",
        "opciones": ["I didn’t went", "I didn’t go", "I don’t went", "I no went"],
        "correcta": 1
    },
    {
        "texto": "Which one is correct?",
        "opciones": ["There is two people", "There are two people", "There are two persons", "There is two persons"],
        "correcta": 1
    },
    {
        "texto": "Pick the correct translation for 'botón' (ropa):",
        "opciones": ["bottom", "botton", "button", "buttom"],
        "correcta": 2
    }
]


preguntas_intermedias_ingles = [
    {
        "texto": "Which sentence is correct?",
        "opciones": [
            "He said me that he was tired.",
            "He told me that he was tired.",
            "He said to me that he was tired.",
            "He told that he was tired."
        ],
        "correcta": 1
    },
    {
        "texto": "Choose the natural sentence:",
        "opciones": [
            "I'm thinking to buy a car.",
            "I'm thinking about buying a car.",
            "I think to buy a car.",
            "I'm thinking in buying a car."
        ],
        "correcta": 1
    },
    {
        "texto": "Pick the correct option:",
        "opciones": [
            "I didn’t knew that.",
            "I didn’t know that.",
            "I don’t knew that.",
            "I not knew that."
        ],
        "correcta": 1
    },
    {
        "texto": "Which sounds more natural?",
        "opciones": [
            "It makes me feel good.",
            "It makes me to feel good.",
            "It makes me feeling good.",
            "It makes me feel well."
        ],
        "correcta": 0
    },
    {
        "texto": "Select the correct sentence:",
        "opciones": [
            "I'm interested on learning more.",
            "I'm interested to learn more.",
            "I'm interested in learning more.",
            "I'm interesting in learn more."
        ],
        "correcta": 2
    },
    {
        "texto": "Choose the correct option:",
        "opciones": [
            "He works hardly every day.",
            "He hardly works every day.",
            "He works hard every day.",
            "He hard works every day."
        ],
        "correcta": 2
    },
    {
        "texto": "Which is correct?",
        "opciones": [
            "We didn’t have to do it.",
            "We mustn’t do it yesterday.",
            "We hadn’t to do it.",
            "We haven’t to do it yesterday."
        ],
        "correcta": 0
    },
    {
        "texto": "Pick the correct sentence:",
        "opciones": [
            "I have the same age as her.",
            "I am the same age with her.",
            "I am the same age as she is.",
            "I have the same age like her."
        ],
        "correcta": 2
    },
    {
        "texto": "Choose the natural one:",
        "opciones": [
            "Let me know if you need something.",
            "Let me know if you will need something.",
            "Let me know if you needed something.",
            "Let me know if you need anything."
        ],
        "correcta": 3
    },
    {
        "texto": "Which sentence is correct?",
        "opciones": [
            "By the time I arrived, she already left.",
            "By the time I arrived, she had already left.",
            "By the time I have arrived, she already left.",
            "By the time I arrive, she had already left."
        ],
        "correcta": 1
    }
]


preguntas_dificiles_ingles = [
    {
        "texto": "Which sentence sounds the most natural?",
        "opciones": [
            "If I would know, I would tell you.",
            "If I knew, I would tell you.",
            "If I know, I will tell you.",
            "If I would knew, I told you."
        ],
        "correcta": 1
    },
    {
        "texto": "Choose the correct sentence:",
        "opciones": [
            "Neither of them are coming.",
            "Neither of them is coming.",
            "Neither they are coming.",
            "Neither they is coming."
        ],
        "correcta": 1
    },
    {
        "texto": "Pick the correct one:",
        "opciones": [
            "I look forward to see you.",
            "I look forward to seeing you.",
            "I'm looking forward to see you.",
            "I am looking forward you."
        ],
        "correcta": 1
    },
    {
        "texto": "Which option is grammatically correct?",
        "opciones": [
            "I have lived here since three years.",
            "I live here since three years.",
            "I have been living here for three years.",
            "I am living here since three years."
        ],
        "correcta": 2
    },
    {
        "texto": "Which one is correct?",
        "opciones": [
            "It depends of the situation.",
            "It depends on the situation.",
            "It depends from the situation.",
            "It depends in the situation."
        ],
        "correcta": 1
    },
    {
        "texto": "Choose the natural sentence:",
        "opciones": [
            "I'm used to wake up early.",
            "I used to waking up early.",
            "I'm used to waking up early.",
            "I’m use to wake up early."
        ],
        "correcta": 2
    },
    {
        "texto": "Pick the most natural option:",
        "opciones": [
            "Let's discuss about it.",
            "Let's discuss it.",
            "Let's discuss about this topic.",
            "Let's talk it."
        ],
        "correcta": 1
    },
    {
        "texto": "Which is correct?",
        "opciones": [
            "He suggested me to try it.",
            "He suggested to me to try it.",
            "He suggested that I try it.",
            "He suggested that I to try it."
        ],
        "correcta": 2
    }
]



#PREGUNTAS DE CULTURA E HISTORIA 
preguntas_faciles_cultura = [
    {
        "texto": "¿En qué año llegó Cristóbal Colón a América?",
        "opciones": ["1492", "1500", "1482", "1510"],
        "correcta": 0
    },
    {
        "texto": "¿Cuál es la capital de Francia?",
        "opciones": ["Londres", "Berlín", "París", "Madrid"],
        "correcta": 2
    },
    {
        "texto": "¿Quién escribió 'Don Quijote de la Mancha'?",
        "opciones": ["Lope de Vega", "Miguel de Cervantes", "García Lorca", "Calderón de la Barca"],
        "correcta": 1
    },
    {
        "texto": "¿En qué continente está Egipto?",
        "opciones": ["Asia", "Europa", "África", "América"],
        "correcta": 2
    },
    {
        "texto": "¿Cuántos continentes hay en el mundo?",
        "opciones": ["5", "6", "7", "8"],
        "correcta": 2
    }
]

preguntas_intermedias_cultura = [
    {
        "texto": "¿Quién pintó 'La última cena'?",
        "opciones": ["Miguel Ángel", "Leonardo da Vinci", "Rafael", "Donatello"],
        "correcta": 1
    },
    {
        "texto": "¿En qué año comenzó la Segunda Guerra Mundial?",
        "opciones": ["1939", "1941", "1914", "1945"],
        "correcta": 0
    },
    {
        "texto": "¿Qué civilización construyó Machu Picchu?",
        "opciones": ["Aztecas", "Mayas", "Incas", "Olmecas"],
        "correcta": 2
    },
    {
        "texto": "¿Quién fue el primer presidente de Estados Unidos?",
        "opciones": ["Thomas Jefferson", "George Washington", "Abraham Lincoln", "Benjamin Franklin"],
        "correcta": 1
    },
    {
        "texto": "¿En qué país se encuentra la Torre de Pisa?",
        "opciones": ["Francia", "España", "Italia", "Grecia"],
        "correcta": 2
    }
]


preguntas_dificiles_cultura = [
    {
        "texto": "¿En qué año cayó el Imperio Romano de Occidente?",
        "opciones": ["476 d.C.", "410 d.C.", "395 d.C.", "500 d.C."],
        "correcta": 0
    },
    {
        "texto": "¿Quién escribió 'Cien años de soledad'?",
        "opciones": ["Mario Vargas Llosa", "Gabriel García Márquez", "Pablo Neruda", "Julio Cortázar"],
        "correcta": 1
    },
    {
        "texto": "¿En qué batalla fue derrotado definitivamente Napoleón Bonaparte?",
        "opciones": ["Austerlitz", "Leipzig", "Waterloo", "Jena"],
        "correcta": 2
    },
    {
        "texto": "¿Qué filósofo griego fue maestro de Platón?",
        "opciones": ["Aristóteles", "Sócrates", "Pitágoras", "Heráclito"],
        "correcta": 1
    },
    {
        "texto": "¿En qué año se firmó la Declaración de Independencia de Estados Unidos?",
        "opciones": ["1776", "1789", "1783", "1765"],
        "correcta": 0
    }
]



temas = {
    "Cultura": [
        ("Fácil", preguntas_faciles_cultura),
        ("Intermedio", preguntas_intermedias_cultura),
        ("Difícil", preguntas_dificiles_cultura),
    ],
    "Ingles": [
        ("Easy", preguntas_faciles_ingles),
        ("Intermediate", preguntas_intermedias_ingles),
        ("Hard", preguntas_dificiles_ingles),
    ],
}