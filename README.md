# Trabalho 2 de IA

## Como executar o código
  Abrir o terminal e ir até a pasta onde está o código.
  Depois, é só executar com:

  ```sh
    python3 main.py
  ```

  Os resultados finais estarão nos arquivos ```results/10geracoes.txt``` e ```results/20geracoes.txt```, contendo uma tabela com os resultado de cada geração para cada teste, bem como a média e qual se saiu melhor.


## Sobre o Algoritmo Genético
  O Algoritmo Genético (AG) é um método de otimização inspirado na pŕopria biologia, onde os seres sofrem mutações e os mais aptos sobrevivem.

  Ele é implementado como uma simulação de computador, geralmente se iniciando a partir de um conjunto de população criada aleatoriamente, e seguindo através de gerações. A cada geração, a adaptação de cada indivíduo na população é avaliada, alguns indivíduos são selecionados para a próxima geração, e recombinados ou mutados para formar uma nova população. A nova população então é utilizada como entrada para a próxima iteração do algoritmo.


## Resumo do algoritmo desenvolvido
  - Cada arquivo é uma classe que representa uma parte do algoritmo;

  - O ```chromosome.py``` representa as possíveis soluções, e conta com os atributos de resultado em bits, resultado em decimal e aptidão, além de funções para trazer e encontrar esses valores a serem utilizados pelas outras classes;

  - O ```crossover.py``` é uma classe para realizar o crossover entre dois cromossomos, em que o método principal ```execute``` chama a função de crossover ```crossover_chromosomes``` se a taxa de crossover for <= 60%;

  - O ```mutation.py``` tem a estrutura semelhante ao crossover, com um método ```execute``` que fará a mutação caso a taxa de mutação for <= 1%;

  - O ```population.py``` gera a população inicial para o algoritmo genético, retornando a lista de população;

  - O ```genetic_algorithm.py``` é o arquivo que contém a classe que realmente executa o algoritmo genético. Seu método principal é o ```execute```, que irá iniciar uma população, procurar os melhores candidatos entre elas com o método ```get_best_from_population```, e criar uma nova geração com ```get_new_population```. Ele fará isso para uma determinada quantidade de ```gerações```, que é passada como parâmetro na criação da classe;

  - O ```main.py``` gerencia para que o algoritmo genético ocorra para 10 e 20 gerações, e chama o auxiliar ```test2txt``` para salvar os resultados nos arquivos ```.txt``` para relatório.