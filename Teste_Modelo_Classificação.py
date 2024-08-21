

# features (1 sim, 0 não)
# pelo longo?
# perna curta?
# late?

porco1 = [0, 1, 0]
porco2 = [0, 1, 1]
porco3 = [1, 1, 1]

cachorro1 = [0, 1, 1]
cachorro2 = [1, 0, 1]
cachorro3 = [1, 1, 1]

# 1 -> porco, 0 -> cachorro
dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
classes = [1,1,1,0,0,0]


from sklearn.svm import LinearSVC
model = LinearSVC()
model.fit(dados, classes)

animal_misterioso = [1,1,1]
model.predict([animal_misterioso])    

misterio1 = [1,1,1,]
misterio2 = [1,1,0]
misterio3 = [0,1,1]

testes = [misterio1, misterio2, misterio3]
previsoes = model.predict(testes)

teste_classe = [0, 1, 1]
