# Projeto: Algoritmo de Karatsuba

## Descrição do Projeto
Este projeto implementa o **Algoritmo de Karatsuba**, uma técnica eficiente para multiplicação de números inteiros grandes, utilizando uma abordagem de dividir e conquistar. Em comparação com o método tradicional de multiplicação, o algoritmo de Karatsuba reduz o número de multiplicações necessárias, tornando-o mais eficiente para números com muitos dígitos.

### Lógica do Algoritmo
1. **Caso Base:**  
   Se um dos números tiver apenas um dígito (ou for menor que 10), a multiplicação é realizada diretamente.

2. **Divisão dos Números:**  
   Os números são divididos em duas partes:
   - **Parte alta:** os dígitos mais significativos.
   - **Parte baixa:** os dígitos menos significativos.
   
   Essa divisão é feita com base no tamanho (número de dígitos) máximo entre os dois números.

3. **Recursão:**  
   São realizadas três multiplicações recursivas:
   - `z0`: Multiplicação das partes baixas.
   - `z1`: Multiplicação da soma das partes altas e baixas.
   - `z2`: Multiplicação das partes altas.

4. **Combinação dos Resultados:**  
   Os resultados das três chamadas recursivas são combinados utilizando potências de 10 para realinhar os dígitos corretamente e obter o produto final.

## Como Executar o Projeto
1. **Clonar o Repositório:**
   ```bash
   git clone <URL-do-repositório>
   ```
2. **Acessar o Diretório do Projeto:**
   ```bash
   cd <nome-do-diretório>
   ```
3. **Executar o Código:**
   ```bash
   python main.py
   ```

## Relatório Técnico

## Relatório Técnico

### Análise da Complexidade Ciclomática
A complexidade ciclomática pode ser derivada através de diferentes abordagens de modelagem do fluxo de controle. A seguir, apresentamos duas abordagens que podem levar a resultados distintos:

**Abordagem 1: Diagrama Simplificado**
- **N1:** Início da função.
- **N2:** Verificação da condição `(x < 10 or y < 10)`.
- **N3:** Retorno imediato (`return x * y`) se a condição for verdadeira.
- **N4:** Execução do bloco recursivo se a condição for falsa.
- **N5:** Término da função.

Arestas:
1. N1 → N2  
2. N2 → N3 (condição verdadeira)  
3. N2 → N4 (condição falsa)  
4. N3 → N5  
5. N4 → N5  

Contando:  
- Nós (N) = 5  
- Arestas (E) = 5  
- Componentes conexos (P) = 1  

Aplicando a fórmula:
M = E - N + 2P = 5 - 5 + 2 = 2

**Abordagem 2: Considerando a Decisão com Maior Detalhamento**
Se considerarmos que a verificação da condição introduz um nó de decisão extra para separar os dois caminhos (verdadeiro e falso) de forma mais granular, a contagem pode incluir um elemento adicional. Dessa forma, a estrutura de controle pode ser interpretada de modo a resultar em:

M = E - N + 2P = 6 - 5 + 2 = 3

### Análise da Complexidade Assintótica
A complexidade temporal do algoritmo de Karatsuba é definida pela recorrência:
T(n) = 3T(n/2) + O(n)

Aplicando o Teorema Mestre, obtém-se:
- **Tempo:** O(n^(log₂3)) ≈ O(n^1.58)

Como o algoritmo é determinístico, os casos de melhor, médio e pior cenário possuem a mesma complexidade temporal.

