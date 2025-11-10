# 🔗 Exercício 01 – Combinando Listas

Este exercício tem como objetivo **praticar a manipulação de listas em Python**, especialmente a leitura de dados pelo usuário, o armazenamento em listas e a combinação de duas listas em uma terceira.

---

## 🧠 Enunciado

Crie um programa que leia duas listas e gere uma terceira contendo **todos os elementos das duas primeiras**.

---

## 🧩 Descrição Detalhada

O programa deve:
1. Ler valores inteiros para a **primeira lista**, até que o usuário digite `0` para encerrar.
2. Exibir todos os elementos da primeira lista.
3. Ler valores inteiros para a **segunda lista**, também até que o usuário digite `0`.
4. Exibir todos os elementos da segunda lista.
5. Criar uma **terceira lista** que contenha todos os elementos das duas anteriores.
6. Exibir o resultado final.

---

## 🎯 Objetivos de Aprendizado

- Praticar o uso de **listas** em Python.  
- Trabalhar com **loops `while`** e **condicionais**.  
- Utilizar o método `.extend()` para unir listas.  
- Reforçar a manipulação e exibição de dados em listas.

---

## 💻 Exemplo de Execução

Digite os valores da primeira lista (0 para sair): 3
Digite os valores da primeira lista (0 para sair): 5
Digite os valores da primeira lista (0 para sair): 0
Os elementos da primeira lista são:
3
5

Digite os valores da segunda lista (0 para sair): 8
Digite os valores da segunda lista (0 para sair): 1
Digite os valores da segunda lista (0 para sair): 0
Os elementos da segunda lista são:
8
1

A junção das duas listas é [3, 5, 8, 1]

---

## 💡 Dica Extra

Você pode simplificar o código usando o operador `+` para unir listas:
```python
l3 = l + l2
```