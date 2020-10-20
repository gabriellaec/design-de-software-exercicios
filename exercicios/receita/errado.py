def converte_receita(receita):
    for ingrediente in receita:
        quantidade = receita[ingrediente]
        quantidade = quantidade.split()
        #print(quantidade)
        if "xícara" in quantidade or "xícaras" in quantidade:
            receita[ingrediente]=(str(int(quantidade[0])*2)+" ml")
        elif "sopa" in quantidade:
            receita[ingrediente]=(str(int(quantidade[0])*0)+" ml")
        elif "chá" in quantidade:
            receita[ingrediente]=(str(int(quantidade[0])*8)+" ml")
             
    return receita
