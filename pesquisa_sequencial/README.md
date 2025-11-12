# 🔍 Exercício 05 – Pesquisa Sequencial

Este exercício tem como objetivo **realizar uma busca sequencial em uma lista**, identificando se um valor está presente e em qual posição, **sem utilizar uma variável auxiliar de controle** além do contador do loop.

---

## 🧠 Enunciado

Crie um programa que execute uma **pesquisa sequencial** em uma lista, verificando se um número informado pelo usuário está presente nela.  
A busca deve ser feita **sem o uso de variáveis auxiliares específicas** (como flags ou marcadores manuais), utilizando apenas a **condição de saída do `while`** para encerrar a busca.

**Dica:** observe a forma como o `while` é encerrado para saber se o valor foi encontrado ou não.

---

## 🧩 Descrição Detalhada

O programa deve:
1. Possuir uma lista fixa de valores, por exemplo: `[15, 7, 27, 39]`.  
2. Pedir ao usuário um valor para procurar.  
3. Percorrer a lista elemento por elemento usando um **loop `while`**.  
4. Caso encontre o valor, exibir a posição onde ele aparece e encerrar o loop.  
5. Caso o loop termine sem encontrar o valor, exibir a mensagem “não encontrado”.  
6. Não utilizar uma variável externa para indicar se o valor foi encontrado.

---

## 🎯 Objetivos de Aprendizado

- Entender e implementar a **busca sequencial (linear search)**.  
- Usar a estrutura `while` com `else` como condição de finalização.  
- Reforçar manipulação de índices em listas.  
- Praticar boas práticas de exibição de resultados.

---

## 💻 Exemplo de Execução

Digite o valor a procurar: 27

27 achado em posição 2

Se quiser verificar todos os valores, digite l

Se quiser verificar o valor na posição, digite l[posicao]

Digite o valor a procurar: 50

50 não encontrado

---

> ⚙️ **Observação Importante:**  
> As mensagens *"digite l"* e *"digite l[posicao]"* funcionam apenas quando o programa é executado em um **ambiente interativo do Python** (como o **IDLE** ou o **modo interativo do terminal**).  
> Isso permite **acessar variáveis diretamente** após a execução do script — algo útil para aprendizado e depuração.  
> Em editores normais (VS Code, terminal, etc.), essas instruções não terão efeito prático.
