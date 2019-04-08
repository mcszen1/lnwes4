# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 14:03:34 2019

@author: Reborn
"""

import newspaper
from newspaper import news_pool
from newspaper import Article
print()
print('LNEWS - Ferramenta de extração de conteúdo')
print('Desenvolvida por MCS - LABCOM/DCS/UFMA')
print()
w=0
while w==0:
    print ('ETAPA 1 - SELEÇÃO DA FONTE DE MÍDIA')
    print()
    print ("Vamos escolher o site do veículo de onde quer os dados")
    print()
    print ('Digite 1 para Uol')
    print ('Digite 2 para Estadao')
    print ('Digite 3 para Globo.com')
    print ('Digite 4 para entrar com o endereço de outro veículo')
    veiculo=input("Escolha o veículo para extração: ")
    print('Conectando ao site. Aguarde...')
    try:  
        if str(veiculo)=='1':
            escolha="https://www.folha.uol.com.br/"
            break
        elif str(veiculo)=='2':
            escolha="https://www.estadao.com.br/"
            break
        elif str(veiculo)=='3':
            escolha="https://www.globo.com/"
            break
        elif str(veiculo)=='4': 
            escolha=input('Digite o endereço (URL) do veículo que deseja: ')
            break
        else:
            print ('Você não digitou um valor da lista. Digite apenas um número entre 1 e 4')
            print()
            continue
    except ValueError:
        print()
                  
meio=newspaper.build(escolha, language='pt', memoize_articles=False)
fast=[meio]
news_pool.set(fast,threads_per_source=2)
print()
print ('Total de registros coletados: ' + str(meio.size()))
listaurl=[]
urlfinal=[]
for article in meio.articles:
    listaurl.append(article.url)
for url in listaurl:
    if veiculo=="1":
           if "#comments" and "especial" not in url: 
               urlfinal.append(url)
    elif veiculo=="2":
           if "galerias" and "?" not in url:
               urlfinal.append(url)
    elif veiculo=="3":
           if "globoplay" not in url:
               urlfinal.append(url)
    else:
               urlfinal.append(url)
print ("Quantidade de matérias coletadas: " + str(len(urlfinal)))
print ("Lista de URLs das matérias coletadas :")
for link in urlfinal:
    print (str(urlfinal.index(link)+1)+ " - "+link)
print()

z=0
while z==0: #  article.download()
  #  article.parse()
    print()
    print ('ETAPA 2 - EXPLORE AS MATÉRIAS')
    numero=input("Escolha um número entre 1 e "+str(len(urlfinal))+ ": ")    
    article=Article(urlfinal[int(numero)-1],language='pt')
    article.download()
    article.parse()
    print("URL escolhida:")
    print (str(urlfinal[int(numero)-1]))
    print()
    print ('Texto da matéria escolhida:')
    print (article.text)
#    article.nlp()
#    print()
#    print ("Palavras chave do artigo:")
#    print (article.keywords)
#    print()
#    print ("Autores identificados no artigo (se constar a informação) :")
#    print (article.authors)
#    print()
#    print ("Resumo do artigo (função ainda pouco operacional para a lingua portuguesa) : ")
#    print()
#    print (article.summary)
#    print()
    choice=input('QUER VER OUTRA MATÉRIA ? DIGITE 1 PARA SIM E 2 PARA NÃO : ')
    try:    
        if str(choice)=="1":
            continue
        elif str(choice)=="2":
            break
        else:
            print('Você não fez uma escolha válida, para sair tem que digitar 2')
            continue
    except ValueError:
        print ()
print()
print ('ETAPA 3 - SALVANDO MATÉRIAS EM ARQUIVOS DE TEXTO')
print()
nomearquivo=input('Escolha um nome para o seu arquivo: ')
f=open(nomearquivo,'w')
u=open('lista'+str(nomearquivo),'w')
linktextos=[]
rotulo=input("Defina um filtro (editoria ou temática de interesse) : ")
qlink=0
for link in urlfinal:
     if rotulo in link:
        linktextos.append(link)
        print (str(linktextos.index(link)+1)+ " - "+link)
        qlink +=1
print()
print ('Coleta com filtro gerou '+ str(qlink)+ "  matérias.")        
print('Aguarde , estou salvando a lista de links das matérias ....') 
for indice in linktextos:
    u.write(str(linktextos.index(indice)+1)+ " - "+str(indice)+"\r\n")
print('Aguarde , estou salvando os textos das matérias ....')  
for filtro in linktextos:
    try:
        article=Article(filtro, language='pt')
        article.download()
        article.parse()
        article.nlp
        txt=article.text
        f.write(str(txt.encode('utf-8').decode('utf-8'))+'\r\n')
    except Exception:
        print ('Link com problema - Extração incompleta')
   
f.close()
u.close()

print ('Arquivos com a lista e os textos salvos.')
