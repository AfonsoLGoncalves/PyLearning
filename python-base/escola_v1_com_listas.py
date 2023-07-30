#!/usr/bin/env python3
"""Exibe relatorio de crianca por atividades

Imprimir a lista da crinças agrupadas por sala
que frequentas cada uma das atividades
"""
__version__ = "0.1.0"


# Dados
sala1 = ["Afonso", "Anthony", "Gabriel", "Carlos", "Bruno Enrique", "Pamela"]
sala2 = ["Ryan", "Bruno", "Jailson", "Kenji", "Caio", "William", "João"]

aula_ingles = ["Afonso", "Anthony", "Jailson", "Caio", "William", "Kenji"]
aula_musica = ["Afonso", "Jailson", "Kenji"]
aula_danca = ["Gabriel", "Carlos", "Bruno Enrique", "Kenji"]

atividades = [
    ("Inglês", aula_ingles),
    ("Música", aula_musica),
    ("Dança", aula_danca),
]

# Listar alunos em cada atividade por sala

for nome_da_atividade, atividade in atividades:
    
    print(f"Alunos da atividade {nome_da_atividade}")
    print("-" * 40)
    
    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in aula_ingles:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)
            
    print("Sala1 ", atividade_sala1)
    print("Sala2 ", atividade_sala2)
    print()
    print("#" * 40)
    print()