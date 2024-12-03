# FiapCap3Fase4
<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto
 Implementando algoritmos de Machine Learning com Scikit-learn

## 👨‍🎓 Integrantes: 
Gustavo Beu Gomes RM:560543

## 📜 Descrição 
Classificação de Grãos de Trigo com Machine Learning
Este projeto tem como objetivo automatizar a classificação de grãos de trigo em três variedades (Kama, Rosa e Canadian) com base em características físicas, utilizando técnicas de aprendizado de máquina. A iniciativa busca aumentar a eficiência e precisão do processo, especialmente para cooperativas agrícolas de pequeno porte.
Descrição
A classificação manual de grãos é um processo suscetível a erros humanos e pode ser demorado. Com o avanço do aprendizado de máquina, é possível criar modelos que realizam essa tarefa de forma automática e confiável. Este projeto utiliza o Seeds Dataset (disponível no UCI Machine Learning Repository) para construir, treinar e avaliar modelos de classificação, seguindo a metodologia CRISP-DM.
Objetivos do Projeto
Analisar e pré-processar os dados para preparar o conjunto de treinamento.
Implementar e comparar diferentes algoritmos de classificação:
K-Nearest Neighbors (KNN)
Support Vector Machine (SVM)
Random Forest
Otimizar os modelos para melhorar o desempenho.
Avaliar os resultados com métricas padronizadas e interpretar os insights.
Conjunto de Dados
O Seeds Dataset contém 210 amostras de grãos de trigo, cada uma com as seguintes características:

Área: Medida da área do grão.
Perímetro: Comprimento do contorno do grão.
Compacidade: Relacionada à forma do grão.
Comprimento do Núcleo: Comprimento do eixo principal da elipse do grão.
Largura do Núcleo: Comprimento do eixo secundário da elipse.
Coeficiente de Assimetria: Medida de assimetria do grão.
Comprimento do Sulco do Núcleo: Tamanho do sulco central do grão.
Classe: Variedade do grão (1: Kama, 2: Rosa, 3: Canadian).
Tecnologias Utilizadas
Linguagem: Python
Bibliotecas:
pandas para manipulação de dados.
matplotlib e seaborn para visualização.
scikit-learn para modelagem e avaliação.
StandardScaler para normalização.
Etapas do Projeto
Análise Exploratória e Pré-processamento:

Limpeza de dados, análise estatística e visualização.
Normalização das características para algoritmos sensíveis à escala.
Treinamento de Modelos:

Implementação de KNN, SVM e Random Forest.
Separação dos dados em conjuntos de treinamento e teste (70%/30%).
Avaliação e Comparação:

Uso de métricas como Acurácia, Precisão, Recall, F1-Score e Matriz de Confusão.
Comparação do desempenho dos algoritmos.
Otimização:

Ajuste de hiperparâmetros com GridSearch para melhorar os modelos.
Resultados e Insights
O modelo com melhor desempenho será indicado com base nas métricas.
Discussão sobre o impacto da normalização e escolha de algoritmos para aplicações reais.

## 🔧 Como executar o código
Como Executar o Projeto
Este guia explica como executar o código diretamente no seu computador, passo a passo.

1. Baixar o Arquivo do Projeto
Certifique-se de que você tem os seguintes arquivos:

O código Python consolidado (o script completo).
O arquivo do dataset seeds_dataset.txt.
Salve ambos os arquivos na mesma pasta do seu computador.

2. Instalar o Python
Verifique se o Python está instalado no seu computador:

Para Windows: Baixe em python.org e instale a versão mais recente (recomenda-se 3.8 ou superior).
Após instalar, verifique no terminal:
bash
Copiar código
python --version
3. Instalar as Bibliotecas Necessárias
Abra o terminal ou prompt de comando e instale as bibliotecas utilizadas no projeto:

bash
Copiar código
pip install pandas scikit-learn matplotlib
Essas bibliotecas são responsáveis por manipulação de dados, construção dos modelos e visualização.

4. Executar o Código
Certifique-se de que o arquivo seeds_dataset.txt está salvo na mesma pasta que o script Python.
Abra um terminal ou prompt de comando, navegue até a pasta onde está o código:
bash
Copiar código
cd caminho/da/pasta
Execute o script:
bash
Copiar código
python nome_do_arquivo.py
5. Visualizar os Resultados
O código exibirá:

Análise inicial:
Estatísticas dos dados.
Gráficos como histogramas e boxplots.
Desempenho dos Modelos:
Matrizes de confusão e relatórios de métricas (acurácia, precisão, recall e F1-score).
Comparação de Modelos:
Acurácia dos modelos KNN, SVM e Random Forest para determinar o mais eficiente.
6. Dicas Adicionais
Se quiser editar o código, use um editor de texto como VSCode, PyCharm ou até mesmo o bloco de notas.
Caso veja erros de caminho, ajuste o nome ou caminho do arquivo seeds_dataset.txt no código.

