# 📝 Exercício: Análise de Temperaturas em Mons, Bélgica

Este exercício tem como objetivo ensinar a manipular listas em Python para realizar operações como encontrar o maior, menor e média de um conjunto de dados numéricos. No caso, estamos lidando com as **temperaturas de Mons**, uma cidade na Bélgica.

---

## 🧠 Enunciado

Dada uma lista `T` contendo as **temperaturas diárias** em Mons, Bélgica, o objetivo é criar um programa que:

1. Imprima a **maior** e a **menor temperatura** registradas.
2. Exiba o **índice** de onde essas temperaturas ocorrem na lista.
3. Calcule e mostre a **temperatura média**.

### Exemplo de lista de temperaturas:
```python
T = [-10, -8, 0, 1, 2, 5, -2, -4]
```

---

## 🔍 Explicação do Código

1. Inicialização: Começamos com o valor da primeira temperatura como sendo a maior (maximo) e a menor (minimo), para garantir que haverá valores de comparação durante o loop.
2. Laço de Repetição: Usamos um for com enumerate() para iterar sobre a lista t, onde:
   - Se a temperatura da iteração for maior que o valor atual de maximo, ela se torna o novo  máximo e o índice da iteração é salvo na variável IM.
   - Da mesma forma, se a temperatura for menor que o valor de minimo, ela se torna o novo mínimo e o índice é salvo na variável im.
3. Cálculo da Média: A variável m acumula a soma de todas as temperaturas, e ao final, dividimos essa soma pelo número de elementos da lista para obter a média.

## 🎯 Objetivos de Aprendizado

- Manipulação de listas: Iterar sobre listas e acessar elementos com o índice.
- Encontrar valores extremos: Como identificar o maior e o menor valor em uma lista.
- Cálculo de média: Como calcular a média de uma lista de números.
- Usar o enumerate(): Para obter tanto o índice quanto o valor ao iterar sobre uma lista.

---

## 💻 Exemplo de Execução

A maior temperatura foi de 5 localizada no índice 5
A menor temperatura foi de -10 localizada no índice 0
A temperatura média é de 0.00
