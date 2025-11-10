# 🧮 Exercício 04 – Validação de Parênteses com Pilhas

Este exercício tem como objetivo **verificar se os parênteses em uma expressão estão balanceados**, ou seja, se foram **abertos e fechados corretamente** usando o conceito de **pilhas (LIFO)**.

---

## 🧠 Enunciado

Crie um programa que leia uma **expressão contendo parênteses** e verifique se ela está correta.  
Os parênteses devem ser **abertos e fechados na ordem certa**.

**Exemplos:**

(()) → OK
()()(()()) → OK
()) → Erro


A cada parêntese aberto `'('`, o programa deve **empilhar** o símbolo.  
A cada parêntese fechado `')'`, o programa deve **desempilhar**.  
Se em algum momento tentar desempilhar sem ter nada na pilha, há **erro**.  
Se, ao final, a pilha não estiver vazia, há **parênteses abertos sem fechamento**.

---

## 🧩 Descrição Detalhada

O programa deve:
1. Pedir ao usuário para digitar uma expressão.  
2. Percorrer a expressão caractere por caractere.  
3. Cada vez que encontrar `'('`, adicioná-lo à **pilha**.  
4. Cada vez que encontrar `')'`, remover o último `'('` da pilha.  
5. Se tentar remover de uma pilha vazia, exibir erro de fechamento incorreto.  
6. Se, ao final, a pilha ainda tiver elementos, exibir erro de parênteses não fechados.  
7. Caso contrário, exibir que a expressão está correta.

---

## 🎯 Objetivos de Aprendizado

- Entender o funcionamento de **pilhas (LIFO)**.  
- Praticar o uso de **listas como estrutura de pilha** em Python.  
- Trabalhar com **loops e condicionais** em validação lógica.  
- Aprender a identificar **erros de balanceamento de símbolos**.

---

## 💻 Exemplo de Execução

Digite S para adicionar uma expressão
ou N para parar
O que deseja fazer? S ou N: S
Digite a expressão: (())
OK, a expressão está correta

Digite S para adicionar uma expressão
ou N para parar
O que deseja fazer? S ou N: S
Digite a expressão: ())
Erro
Você fechou um parêntese sem abrir um antes,
no 3° elemento da expressão ['(', ')', ')']

