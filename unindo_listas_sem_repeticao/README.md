# 🔁 Exercício 02 – Unindo Listas sem Repetição

Este exercício tem como objetivo **unir duas listas de números inteiros**, criando uma terceira lista que **não contenha elementos duplicados**.

---

## 🧠 Enunciado

Crie um programa que leia duas listas e gere uma terceira com **todos os elementos das duas**, **sem repetição de valores**.

---

## 🧩 Descrição Detalhada

O programa deve:
1. Ler valores inteiros e armazenar na **primeira lista** até que o usuário digite `0`.
2. Exibir todos os elementos digitados na primeira lista.
3. Ler valores inteiros e armazenar na **segunda lista**, também até que o usuário digite `0`.
4. Exibir os elementos da segunda lista.
5. Gerar uma **terceira lista** com os elementos das duas anteriores, **eliminando repetições**.
6. Exibir o resultado final.

---

## 🎯 Objetivos de Aprendizado

- Praticar manipulação de **listas**.  
- Trabalhar com **comparação e filtragem de elementos**.  
- Reforçar **controle de loops** e **condicionais**.  
- Entender como **evitar duplicatas** em estruturas de dados.

---

## 💻 Exemplo de Execução

Digite os valores da primeira lista (0 para sair): 3

Digite os valores da primeira lista (0 para sair): 5

Digite os valores da primeira lista (0 para sair): 7

Digite os valores da primeira lista (0 para sair): 0

Os elementos da primeira lista são:

3

5

7

Digite os valores da segunda lista (0 para sair): 5

Digite os valores da segunda lista (0 para sair): 8

Digite os valores da segunda lista (0 para sair): 0

Os elementos da segunda lista são:

5

8

A junção das duas listas (sem repetição) é [3, 5, 7, 8]

---

## 💡 Dica Extra

A forma mais simples de remover elementos duplicados é usando **conjuntos (`set`)** em Python:

```python
l3 = list(set(l + l2))
```