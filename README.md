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
  # Segmentação das imagens (HSV - Matiz, Saturação e Valor)
    - Matiz: é a representação pura da cor
    - Saturação: é o grau de intensidade da cor
    - Valor: é o nível de brilho e sombra da cor
    - A detecção de células brancas e vermelhas foram feitas separadamente
    - Para a remoção das células que não estavam sendo procuradas foi feito o seguinte:
    - Uma máscara contendo o range da cor procurada é estabelecido, e uma operação de bitwise (and &) é feita para remoção de artefatos que não sejam daquela cor

  # Preenchimento de buracos e "limpeza" nos limites dos retângulos
    - Aplicação de Fechamento seguido de Abertura da imagem, isso serve para remover pequenos buracos pretos e brancos da imagem (no caso da detecção das hemácias é muito útil, pois retira algumas das células brancas)
    - Aplicação de erosão para preenchimento de pequenos buracos nos círculos
  

## Algoritmos utilizados
  - Clahe (Aumento do contraste da imagem, isso faz com que os círculos fiquem em evidência) É uma adaptação da equalização histogrâmica
  - Filtro Gaussiano (É um filtro para remoção de ruído em imagens, produz um efeito de borramento)
  - Fechamento (Remoção de pequenos objetos - serve como um removedor de ruídos)
  - Abertura (Remoção de objetos da parte da frente da imagem e os posicionando na parte de trás)
  - Binarização da imagem (Treshold adaptativo)
  - Erosão (Preenchimento de pequenos buracos na imagem, isso faz com que eles não sejam detectados como uma célula)
  - Inverso da imagem (mapeamento das intensidades dos pixels para seu oposto, 255 - intensidade do pixel)