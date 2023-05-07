## Contagem de Hemácias
  - Projeto da disciplina de Processamento de Imagens ministrada pelo professor Leonardo
  
## Objetivo
  - A partir de técnicas de processamento de imagens aprendidas em sala, devemos detectar o número de células brancas e vermelhas em uma imagem, assim como suas posições
  
## Dados
  - A base de dados Kaggle será utilizada para o teste e validação desse projeto

## Avaliação da corretude da solução (IOU)
  - Para isso, iremos usar Intersection Over Union (Interseção sobre união)
  - Essa técnica serve para avaliar o desempenho de uma solução
  - Logo, teremos as labels das nossas células, assim como a posição de sua bounding box (retângulo limitante)
  - A corretude de uma solução será dada pelo cálculo do IOU
  - Se o IOU entre a predição da bounding box e a bounding box verdadeira for >= 0.5, então consideramos a solução como correta

## Como foi feito?

  # Preenchimento de buracos e "limpeza" dos limites dos retângulos
    - Aplicação de Fechamento seguido de Abertura da imagem, isso serve para remover pequenos buracos pretos e brancos da imagem (no caso da detecção das hemácias é muito útil, pois retira algumas das células brancas)
    - A operação de fechamento serviria para preencher os pequenos buracos da imagem
    - Enquanto a operação de abertura serviria para remover os pequenos poros que estão presentes nos limites dos objetos das imagens

  # Trabalhando no canal HSV
    - Para a detecção de células vermelhas, antes precisei fazer um tratamento da saturação do nível de azul da imagem (que é como as células brancas acabam aparecendo)
    - O mesmo precisei fazer para a detecção de células brancas, diminuindo o nível de saturação de vermelho na imagem