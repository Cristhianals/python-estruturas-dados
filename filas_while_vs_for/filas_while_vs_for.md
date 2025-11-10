# 🏛️ Exercício 08 – Por que nem todo while pode virar for?

Este exercício tem como objetivo **entender as limitações de transformar loops `while` em loops `for`**. 

O programa simula **duas filas de clientes**, permitindo:

- Adicionar clientes no final da fila (`F` e `G`).
- Atender clientes da fila (`A` e `B`).
- Sair do programa (`S`).

O usuário digita operações e o programa realiza cada ação, mostrando o estado atual das filas.

---

## 🧠 Enunciado

1. Analise o programa de atendimento a filas abaixo.  
2. Explique **por que nem todo `while` pode ser transformado em `for`** nesse caso.  
3. Observe que a quantidade de operações e o tamanho das filas **mudam dinamicamente** durante a execução, tornando difícil a substituição direta do `while True` por um `for`.

---

## 🎯 Objetivos de Aprendizado

- Entender **loops infinitos (`while True`)** e suas utilidades.  
- Observar que **loops `for` percorrem elementos de uma sequência fixa**, enquanto o `while` permite **condições dinâmicas de parada**.  
- Trabalhar com **listas como filas (FIFO)** e operações de inserção/remoção.  
- Praticar **interação com o usuário** dentro de loops.

---

## 💻 Exemplo de Execução

Existem 10 clientes na primeira fila,
E 10 na segunda fila
Digite F para adicionar cliente na primeira fila,
ou G para a segunda fila
A para atender primeira fila, B para segunda fila, S para sair
Operações: FGA

cliente 11 adicionado na primeira fila
cliente 11 adicionado na segunda fila
cliente 1 atendido na primeira fila


---

## 💡 Explicação

- O `while True` **permite que o loop continue indefinidamente até que o usuário decida sair (`S`)**.  
- Um `for` tradicional precisaria de uma sequência finita (`range` ou lista) para iterar, **o que não se aplica quando a quantidade de operações não é conhecida antecipadamente**.  
- Além disso, o **tamanho das filas muda a cada iteração**, algo que não é simples de controlar com `for`.  

