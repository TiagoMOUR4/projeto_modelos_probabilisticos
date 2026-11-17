# Análise da atomização e distribuição do tamanho de gotas utilizando redes bayesianas

## Sobre o projeto

O presente projeto foi desenvolvido para a disciplina de **Modelos Probabilísticos**, ministrada pelo Prof. Dr. Carlos Dias Maciel, no segundo semestre de 2026, como disciplina de Portfólio do Programa de Pós-Graduação da UNESP, em Araraquara.

O objetivo deste estudo é compreender e investigar como as diferentes características dos bicos atomizadores e as condições operacionais podem influenciar as propriedades do spray gerado, com foco na distribuição do tamanho das gotas.

Para isso, serão utilizadas ferramentas de análise estatística e modelagem probabilística em Python, com destaque para as **redes bayesianas**, visando investigar dependências entre as variáveis experimentais e identificar relações que possam contribuir para a compreensão física do processo de atomização.

## Base de dados

Os dados utilizados são provenientes do estudo experimental de Fritz e Hoffmann (2015), desenvolvido pelo *United States Department of Agriculture – Agricultural Research Service* (USDA-ARS).

Os experimentos foram realizados em túnel de vento, utilizando diferentes modelos de bicos atomizadores e variando condições como pressão de alimentação, velocidade do ar, orientação e tamanho nominal do orifício.

A distribuição do tamanho das gotas foi caracterizada por difração a laser.

A base contém:

- **2.270 registros experimentais**;
- **716 condições operacionais distintas**;
- **18 identificações de bicos atomizadores**;
- **13 variáveis**, incluindo parâmetros operacionais, características do spray e identificadores experimentais.

Os dados são experimentais, enquanto os modelos apresentados pelos autores são correlações empíricas ajustadas a partir dessas medições.

Fonte: [USDA-ARS — Fixed-Wing Spray Nozzle Models](https://catalog.data.gov/dataset/data-from-update-to-the-usda-ars-fixed-wing-spray-nozzle-models).

## Variáveis e siglas

### 1. Parâmetros operacionais

| Variável | Descrição | Unidade |
|---|---|---|
| `Nozzle` | Modelo ou família do bico atomizador utilizado no experimento. | Categórica |
| `Orifice` | Tamanho nominal do orifício do bico, conforme a designação do fabricante. | Código nominal |
| `Airspeed` | Velocidade do ar no túnel de vento. | mph |
| `Pressure` | Pressão de alimentação do líquido no bico atomizador. | psi |
| `Orientation` | Ângulo de orientação do bico em relação ao escoamento de ar. | ° |

**Observação:** os valores de `Orifice` não representam necessariamente diâmetros físicos na mesma unidade entre diferentes famílias de bicos.

### 2. Características da distribuição de gotas

| Variável | Sigla | Descrição | Unidade |
|---|---|---|---|
| `DV10` | Dv0.1 | Diâmetro abaixo do qual se encontra 10% do volume acumulado das gotas. | µm |
| `DV50` | Dv0.5 / VMD | Diâmetro mediano volumétrico, abaixo do qual se encontra 50% do volume acumulado. | µm |
| `DV90` | Dv0.9 | Diâmetro abaixo do qual se encontra 90% do volume acumulado das gotas. | µm |
| `RS` | Relative Span | Medida adimensional da largura relativa da distribuição de tamanhos. | Adimensional |
| `Less100` | — | Percentual do volume total do spray correspondente às gotas com diâmetro inferior a 100 µm. | % |
| `Less200` | — | Percentual do volume total do spray correspondente às gotas com diâmetro inferior a 200 µm. | % |

Os diâmetros DV10, DV50 e DV90 representam percentis da distribuição **volumétrica**, e não da distribuição numérica de gotas.

O *Relative Span* (RS) é calculado pela expressão:

$$
RS=\frac{DV90-DV10}{DV50}
$$

Valores menores de RS indicam uma distribuição relativamente mais estreita, enquanto valores maiores indicam maior dispersão entre os percentis volumétricos considerados.

### 3. Identificadores experimentais

| Variável | Descrição |
|---|---|
| `Run` | Identificador da execução experimental. |
| `Rep` | Identificador da repetição experimental. |

Essas variáveis serão utilizadas para organizar os registros, analisar a reprodutibilidade e evitar que medições repetidas da mesma condição sejam tratadas como condições operacionais independentes.

## Objetivos das análises

O projeto buscará investigar:

1. A influência das características dos bicos e das condições operacionais sobre a distribuição de tamanhos das gotas.
2. As relações entre os diâmetros característicos, a largura da distribuição e as frações volumétricas de gotas pequenas.
3. A existência de dependências condicionais entre variáveis operacionais e propriedades do spray utilizando redes bayesianas.
4. A capacidade de diferentes modelos estatísticos e de aprendizado de máquina representarem as observações experimentais.
5. A possibilidade de utilizar os resultados para caracterizar distribuições de tamanho de gotas em modelos computacionais de sprays.

As redes bayesianas serão utilizadas para investigar relações probabilísticas entre as variáveis, distinguindo associações estatísticas de relações causais comprovadas.

## Ferramentas

As análises serão desenvolvidas em **Python**, utilizando bibliotecas para manipulação de dados, visualização, análise estatística e modelagem probabilística.

As ferramentas e os procedimentos computacionais serão documentados conforme o desenvolvimento do projeto.

## Referências

Fritz, B. K.; Hoffmann, W. C. (2015). *Update to the USDA-ARS Fixed-Wing Spray Nozzle Models*. Transactions of the ASABE.

Dados experimentais: [USDA-ARS](https://catalog.data.gov/dataset/data-from-update-to-the-usda-ars-fixed-wing-spray-nozzle-models).
# projeto_modelos_probabilisticos
