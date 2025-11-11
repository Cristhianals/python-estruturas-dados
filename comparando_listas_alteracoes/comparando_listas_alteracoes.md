# 📝 Exercício 13 – Comparando Versões de Listas com Conjuntos

Este exercício demonstra como utilizar **conjuntos (sets)** para comparar duas versões de uma lista, identificando **o que mudou, o que foi adicionado e o que foi removido**.

---

## 🧠 Enunciado

Escreva um programa que compare duas listas:

- A **primeira** lista representa a **versão inicial**.  
- A **segunda** lista representa a **versão após alterações**.  

Utilizando **operações com conjuntos**, o programa deve listar:

1. Os elementos que **não mudaram**.  
2. Os **novos elementos** adicionados.  
3. Os **elementos removidos** na nova versão.

---

## 🎯 Objetivos de Aprendizado

- Trabalhar com **conjuntos** para comparar coleções de dados  
- Utilizar operações como **interseção**, **diferença** e **união**  
- Compreender como identificar mudanças entre versões de listas  
- Manipular entrada de dados de forma dinâmica  

---

# Conversão para conjuntos

c1 = set(l1)

c2 = set(l2)

# Comparação entre as versões

mantidos = c1 & c2        # Elementos que não mudaram

novos = c2 - c1           # Novos elementos

removidos = c1 - c2       # Elementos removidos

