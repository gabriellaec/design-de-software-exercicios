Devido à pandemia do Coronavírus, a procura por pacotes de turismo caiu de forma significativa. Para estimular compras à longo prazo, uma agência de viagens resolveu fazer uma super promoção!
A empresa ranqueou os destinos por nível de procura por números de 1 a 5, sendo 1 o mais buscado e 5 o menos. Para garantir um equilíbrio nas reservas, a agência planejou dar um maior desconto para os destinos menos procurados. 
Dessa forma, inventaram um sistema em que o desconto dado é de 10% a 50%, sendo ele proporcional à posição no ranking de procura e aumentando em 10% por posição. Por exemplo, os destinos mais procurados, com classificação 1, terão apenas 10% de desconto, os de classificação 2 terão 20% e assim por diante.
Para organizar esse sistema, a empresa utilizou dicionários, como o seguinte, em que as chaves são os destinos e os valores uma lista, em que a primeira posição corresponde ao ranking e a segunda ao preço da passagem:
destinos={"Miami":[1,1000], "Ilhas Sandwich do Sul":[4,5000], "Barcelona":[2, 2000], "Antártica":[5,200], "Buenos Aires":[3,500]}
Faça uma função que recebe um dicionário como este e retorna um dicionário, em que os valores contêm o custo final dos pacotes, após o desconto, como no exemplo a seguir:
destinos_promocao={ 'Miami': 900.0,'Ilhas Sandwich do Sul': 3000.0, 'Barcelona': 1600.0, 'Antártica':100.0, 'Buenos Aires': 350.0}