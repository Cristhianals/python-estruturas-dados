# 🛒 Exercício 10 – Controle de Estoque com Dicionário

Este exercício trabalha com **dicionários** para controlar o estoque de produtos, verificar vendas e calcular o custo total.

---

## 🧠 Enunciado

Faça um programa que:

1. Solicite ao usuário o **nome do produto** e a **quantidade vendida**.  
2. Verifique se o produto existe no **dicionário de estoque**.  
3. Se existir, efetue a **baixa no estoque** e calcule o **custo da venda**.  
4. Se não existir, informe que o produto **não está em estoque**.  
5. Ao final, exiba o **total das vendas** e o **estoque atualizado**.

O dicionário de exemplo é:

```python
estoque = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijao": [100, 1.50]
}
```
Onde o primeiro valor é a quantidade em estoque e o segundo é o preço unitário.

## 🎯 Objetivos de Aprendizado

- Manipular dicionários em Python
- Validar entradas do usuário
- Atualizar valores de um dicionário
- Acumular valores para calcular totais
- Iterar sobre listas e dicionários

---

## 💻 Exemplo de Execução

Digite o produto e a quantidade.

Quando terminar de digitar todos os produtos, digite 0

Produto: tomate

Quantidade: 5

Produto: feijao

Quantidade: 10

Produto: cenoura

Quantidade: 3

Não temos cenoura em estoque.

Custo total: 23.00

Estoque atualizado:

tomate -> quantidade: 995, preço: 2.30

alface -> quantidade: 500, preço: 0.45

batata -> quantidade: 2001, preço: 1.20

feijao -> quantidade: 90, preço: 1.50
