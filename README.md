            ﻿                                                       Dicionário de bibliotecas - Python

Python básico:
	lambda var: var**2   				 		#função lambda; funciona apenas nesse escopo
	map(função, lista)	  			     		#função map; associa uma função anterior à um objeto iterável(lista)
	filter()
	import sys
	print sys.path
	sys.path.append(' seu caminho ')       


IPython:
	
        from IPython.display import Image
	Image(url, width= , height= )

Numpy:

	np.array()
	np.arange()
	np.linspace()
	np.zeros()
	np.ones()
	np.eye()
	.size
	.shape
	.reshape()
	 

Pandas:

	pd.Series(data, index)
	pd.DataFrame(data, linhas, colunas)
	df.head()
	df.info()
	df['new'] = [dados novos]   				#insere a coluna "new" no data frame(df) com os dados novos (OBS.:colchetes referem-se a colunas)
	df.drop(coluna, axis = 1, inplace = True)  	#deleta a coluna selecionada e o parâmetro "INPLACE" substitui no dataframe original
	df.loc[]					#mostra a linha dentro de []
	df.iloc[]					#mostra a linha pelo index dentro de []
	df.set_index()
	df.reset_index(inplace = True)
	df.sort_values(ascending= True)					
	df.isnull()					#retorna um data frame de verdadeiros e falsos avaliando onde é 0
	df.pivot_table()
	pd.read_excel()
	pd.read_csv()
	df.to_excel()
	df.to_csv()
	pd.read_html()
	df.nunique()					#conta quantos nomes/valores distintos tem numa linha (axis=1) ou coluna(axis=0)
	df.value_counts()
    !!! df.apply()
	df.xs()						#análise multiindex
	Series.pct_change()				#Alteração percentual entre o elemento atual e o anterior
	df.min()
	df.max()
	df.idxmin()
	df.idxmax()					# diferente do df.max, este retorna o index onde ocorre o máximo
    !!! pd.get_dummies(coluna, drop_first = True)     !ÚTIL PARA DADOS CATEGÓRICOS(str)!# Cria um df com o mesmo index da coluna inserida, porém nesse novo df as colunas são todas as possibilidades e qd True: retorna 1, e qd False: retorna 0
    !!! pd.merge(left,right, on='coluna em comum')
    !!! df.corr()                                       #Faz todas as correlações
	df.corrwith()	
	df.rename(columns = d, inplace = False)
	
pandas-datareader:  (data,wb)
	data.DataReader(name= , data_source=, start=, end= ,**kwargs)  #leitura de dados online feita pelo pandas
	

Matplotlib:
	
	plt.plot()						#OBS: QUANDO CRIAR A FIGURA, A FUNÇÃO É PLOTADA NOS EIXOS
	plt.subplot()						#OBS: 'subplot' e 'subplots' são funções diferentes, 'subplots()' está abaixo
	figgg, axess = plt.subplots(nrows=2, ncols = 2)		#OBS: Essa função funciona melhor com 2 valores para serem retornados, figura e eixos.
		axess[0][0].plot(x,y, color = 'blue', lw = 2, ls = '-')
		axess[0][1].plot(x,z, color = 'red' , lw = 1, ls = '--')
		axess[1][0].plot(y,x, color = 'green', lw = 1, ls = '-')
		axess[1][1].plot(y,z, color = 'black', lw = 1, ls = ':')
	???plt.xlabel()
	???plt.ylabel()
	plt.title()	
	plt.figure()
	fig.add_axes([POSx , POSy ,TAMx ,TAMy ])
	axes.set_xlim(  ,  )
	axes.set_ylim(  ,  )
	axes.legend()
	axes.set_title()
	axes.set_xlabel('x')
	axes.set_ylabel('y')
	plt.hist()
	plt.scatter()
	plt.boxplot(data, vert = True, patch_artist=True)
	plt.tight_layout()
	fig.savefig('imagem.png')	

	
Seaborn:
	
	sea.distplot(dataframe['coluna'])       #Distribuição dos itens da coluna
	sea.jointplot(x, y, data)               #Distribuição com dois parâmetros
	sea.pairplot(data, hue= )		#Faz todas as distribuições possíveis do Dataframe em uma matriz
        
	Plots categóricos:   (plots para strings, ou seja, categorias que não tem valor atribuido)
		sea.barplot(x,y,data)
		sea.countplot(x, data)
		sea.boxplot(x,y, data)	
		sea.violinplot(x,y, data)
		sea.stripplot(x,y, data, jitter='True')
		sea.swarmplot(x,y, data)        #mesma coisa do stripplot, mas os dados vão sendo colocados ao lado
		sea.factorplot(x,y, data, kind=' ')
	
	Plots matriciais:
		dataFrame.corr()                      # calcula todas as correlações possíveis (interdependência entre as variáveis)
		sea.heatmap()
		sea.clustermap()

	Plots de regressão:
		sea.lmplot(x, y, data)

	PairGrid: sea.PairGrid(data)
		Cria um gráfico vazio pra cada possibilidade (plot matricial) e permite que eles sejam preenchidos através de métodos:
			
			sea.PairGrid().map(plt.scatter)    # plt.scatter foi um exemplo de função, pode ser qualquer uma
			sea.PairGrid().map_diag(plt.hist)  # aplica a função determinada na diagonal
			sea.PairGrid().map_upper(plt.scatter)	# aplica a função determina acima da diagonal
			sea.PairGrid().map_lower(sns.kdeplot)	# aplica a função determinada abaixo da diagonal
			
	FacetGrid: 
		sea.FacetGrid()		# mesma função do PairGrid, mas exige que as linhas e colunas sejam determinadas

	sea.set_style('darkgrid')       # estilo preferido :D

	
Plotly e Cufflinks:

	import plotly.plotly as py
	from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
	import cufflinks as cf
	init_notebook_mode(connected=True)   # para usar no jupyter notebook
	cf.go_offline()


Scikit-Learn:  (machine learning)

	from sklearn.model_selection import train_test_split
		train_test_split(X, Y, test_size=0.4, random_state=101)   # Faz a divisão dos dados de X e Y para teste e treino
	                                                                  #  e retorna 4 valores na forma de tupla:(X_train, X_test, Y_train, Y_test)  
									  
	Regressões:
	from sklearn.linear_model import LogisticRegression
	from sklearn.linear_model import LinearRegression
		lm = LinearRegression()		# cria instância de um modelo LinearRegression () 
		lm.fit(X_train,Y_train)		# aplica o treino à regressão
		lm.predict(X_test)		# faz as previsões de Y relacionadas aos índices de X_test
						# uma forma de analisar o erro: plt.scatter(Y_test, lm.predict(X_test))
		lm.coef_
	KNN:
	from sklearn.neighbors import KNeighborsClassifier
	    # Esse processo exige normalização do dataframe, através dos comandos das próximas linhas:
		- from sklearn.preprocessing import StandardScaler
		- scaler = StandardScaler()
		- scaler.transform()
		- criar um dataframe novo com os dados normalizados e esse será usado no aprendizado da função

		knn = KNeighborsClassifier(n_neighbors= )
	
	Árvores de Decisão e Florestas aleatórias:
	from sklearn.tree import DecisionTreeClassifier
	from sklearn.ensemble import RandomForestClassifier
	RandomForestClassifier(n_estimators = )

	SVM:
	from sklearn.svm import SVC

	K Means Clustering:
	from sklearn.cluster import KMeans
	Kmeans(n_clusters= )
	KMeans().cluster_centers_
	Kmeans.labels_                   #Esse é o resultado buscado

	PCA:  
	(obs:EXIGE NORMALIZAÇÃO COM 'StandardScaler()')
	from sklearn.decomposition import PCA
	PCA(n_components= )	
				
	análises de erro:
	from sklearn.metrics import classification_report , confusion_matrix
	from sklearn import metrics
		metrics.mean_absolute_error(Y_test,predict)
		metrics.mean_squared_error(Y_test,predict)
		np.sqrt(metrics.mean_squared_error(Y_test,predict))

Processamento de Linguagem Natural: (Complicado; Checar projeto no notebook)
	
import string
	string.punctuation
	
	modelo 'bag-of-words': 1) Contar qts vezes uma palavra ocorre na mensagem (frequencia de termo)
			       2) Pesar as contagens (tokens frequentes recebem menor peso, 'frequencia inversa do documento')
			       3) Normalizar os vetores para o comprimento da unidade, para abstrair o comp do texto original (norma L2)

	from sklearn.feature_extraction.text import CountVectorizer    

	CountVectorizer(analyzer=text_process)  # text_process é uma função exemplo pra processamento de texto.
	bow_transformer = CounVectorizer.fit(messages['message']) # exemplo de fit
	bow_transformer.transform([mensagem4])
	bow_transformer.get_feature_names()[]	
	
	from sklearn.naive_bayes import MultinomialNB
	nb = MultinomialNB()
	
	from sklearn.feature_extraction.text import  TfidfTransformer
	from sklearn.pipeline import Pipeline

	pipeline = Pipeline([
    			('bow', CountVectorizer()),  # strings to token integer counts
    			('tfidf', TfidfTransformer()),  # integer counts to weighted TF-IDF scores
    			('classifier', MultinomialNB()),  # train on TF-IDF vectors w/ Naive Bayes classifier
			    ])



Anaconda:
	
	>>$ conda create -n bloqueios python=3.7     %
	
	>>$ conda env remove -n ENV_NAME	     %*

	>>$ conda activate bloqueios		     %

	>>$ conda install pandas matplotlib	     %

	>>$ conda install -c conda-forge jupyterlab  %
	>>$ jupyter lab


	>>$ conda install netcdf4 pandas matplotlib seaborn xarray metpy  
 
	>>$ conda install pandas scikit-learn matplotlib jupyter jupyterlab sqlalchemy seaborn pip git matplotlib seaborn xarray

	>>$ jupyter lab

	>>$ conda install ipykernel
	>>$ ipython kernel install --user --name=<env name>
	>>$ jupyter kernelspec uninstall unwanted kernel
	
variaveis de ambiente do sistema


Flask:

    >>$ export FLASK_APP=nomedoprograma
    >>$ export FLASK_ENV=development
    >>$ flask run

    redirect()  # redireciona usando url_for() como arg*
    url_for("funçao_da_route", args)   # args são os arg* da função_da_route (se existirem)


Acesso Linux pelo explorer:

\\wsl$\Ubuntu-20.04\home
sudo chmod 777 file.txt