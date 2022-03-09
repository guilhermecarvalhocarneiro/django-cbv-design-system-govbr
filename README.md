# Projeto Django CBV Design System gov.br

O objetivo deste projeto é desenvolver um projeto django que implemente o padrão visual do design system fornecido pelo governo federal, os templates desenvolvidos serão externos ao admin possibilitando assim uma maior customização das funcionalidades.  

## Versões
-------------
O projeto será desenvolvido utilizando as versões abaixo descritas:

Python 3.8.2

Django 3.2 (LTS)

## Estrutura do projeto
-------------------
Na diretório core temos além dos arquivos padrões dos projetos Django um subdiretório **templates/core** que contêm os arquivos html bases:

1. Cabeçalho da Página -> head.html
1. Menu -> menu.html
1. Rodapé -> footer.html
1. Base -> base.html (Arquivo que agrupa os arquivos anteriores e que será extendido pelos templates das Apps do projeto)  

Já no diretório **modelo/templates/modelo** temos os arquivo que serão utilizados para criar os templates da app.  
1. index.html  
1. listview.html  
1. createview.html
1. updateview.html  
1. detailview.html
1. deleteview.html 
  
## Design System **gov.br**
----------
[Design System gov.br](http://dsgov.estaleiro.serpro.gov.br/introducao/como-comecar)