# 📝 Exercício 12 – Comparando Listas com Conjuntos

Este exercício ensina como **comparar listas usando conjuntos (sets)** e extrair informações como elementos comuns, únicos e não repetidos.

---

## 🧠 Enunciado

Faça um programa que:

1. Leia **duas listas** do usuário.  
2. Imprima:
   - Os valores **comuns** nas duas listas.  
   - Os valores que **só existem na primeira lista**.  
   - Os valores que **só existem na segunda lista**.  
   - Uma lista com os elementos **não repetidos** das duas listas.  
   - A primeira lista **sem os elementos que se repetem na segunda**.

### Dica

- Utilize operadores de **conjuntos**:  
  - `&` → interseção (valores comuns)  
  - `|` → união  
  - `-` → diferença  
  - `^` → elementos exclusivos de cada conjunto  

---

## 🎯 Objetivos de Aprendizado

- Manipular **listas e conjuntos** em Python  
- Compreender **operações de conjuntos** (`&`, `|`, `-`, `^`)  
- Identificar **elementos comuns e únicos**  
- Transformar **listas em conjuntos** para simplificar comparações  

---


# Conversão para conjuntos
c1 = set(l1)
c2 = set(l2)

# Valores comuns
comuns = c1 & c2
# Valores exclusivos
so_l1 = c1 - c2
so_l2 = c2 - c1
# Valores não repetidos
nao_repetidos = c1 ^ c2
# Primeira lista sem elementos repetidos da segunda
l1_sem_repetidos = so_l1

# Impressão dos resultados
print(f"Valores comuns: {comuns}")
print(f"Só na primeira lista: {so_l1}")
print(f"Só na segunda lista: {so_l2}")
print(f"Valores não repetidos: {nao_repetidos}")
print(f"Primeira lista sem elementos repetidos da segunda: {l1_sem_repetidos}")
