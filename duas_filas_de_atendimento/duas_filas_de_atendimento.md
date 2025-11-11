# 🧾 Exercício 03 – Sistema de Duas Filas de Atendimento

Este exercício tem como objetivo **simular o funcionamento de duas filas de atendimento**, permitindo adicionar e atender clientes conforme comandos inseridos pelo usuário.

---

## 🧠 Enunciado

Crie um programa que trabalhe com **duas filas**.  
Para facilitar o controle, use os seguintes comandos:

| Comando | Ação |
|----------|------|
| **F** | Novo cliente chega à **fila 1** |
| **G** | Novo cliente chega à **fila 2** |
| **A** | Atende o próximo cliente da **fila 1** |
| **B** | Atende o próximo cliente da **fila 2** |
| **S** | Encerra o programa |

O programa deve mostrar o número de clientes em cada fila e permitir o processamento de várias operações em sequência.

---

## 🧩 Descrição Detalhada

O programa deve:
1. Criar duas filas iniciais (por exemplo, com 10 clientes cada).  
2. Exibir o número atual de clientes em cada fila.  
3. Solicitar ao usuário uma sequência de operações (como `FGABFS`).  
4. Processar cada operação, atualizando as filas conforme os comandos:  
   - `F` → adiciona um cliente ao final da fila 1.  
   - `G` → adiciona um cliente ao final da fila 2.  
   - `A` → atende (remove) o primeiro cliente da fila 1.  
   - `B` → atende (remove) o primeiro cliente da fila 2.  
   - `S` → encerra o programa.  
5. Informar cada operação realizada e o estado das filas após o processamento.

---

## 🎯 Objetivos de Aprendizado

- Trabalhar com **listas como estruturas de filas (FIFO)**.  
- Praticar **remoção e adição de elementos** (`pop(0)` e `append`).  
- Reforçar **uso de loops e condicionais aninhadas**.  
- Simular **operações em lote** com múltiplos comandos de entrada.  

---

## 💻 Exemplo de Execução

Existem 10 clientes na primeira fila,  
E 10 na segunda fila

Digite F para adicionar um cliente ao fim da primeira fila,  
ou G para adicionar no fim da segunda fila.  
A, para realizar o atendimento da primeira fila,  
ou B, para o atendimento da segunda fila. S para sair.  

Quais operações (F, G, A, B ou S): FAGBS

Cliente 1 da primeira fila atendido  
A operação A foi realizada  
Cliente 1 da segunda fila atendido  
A operação B foi realizada  
As operações ['F', 'A', 'G', 'B', 'S'] foram realizadas

---

## 💡 Dica Extra

Em Python, existe o módulo `collections` com a estrutura `deque`, ideal para **filas**, pois permite remoção eficiente no início da lista:

```python
from collections import deque

fila1 = deque(range(1, 11))
fila2 = deque(range(1, 11))

fila1.append(11)   # adiciona no fim
fila1.popleft()    # remove do início
```