from flask import Flask, render_template, request, session
# render_template para carregar arquivos html pelo flask
# request para poder pegar os dados de formulário
# session para poder guardar valores nas variáveis de sessão do navegador da pessoa
from classes import Serie, Tema
from random import choice

app = Flask(__name__)
# chave para criptografar as variáveis de sessão
app.secret_key = "LGBSBGKYW#TBRjGJKgkejhrg"

### CRIAÇÃO DOS OBJETOS ###
# considere que todos os objetos "temas" e "series" foram criados corretamente
tema_suspense = Tema("Suspense")

serie_stranger_things = Serie("Stranger Things", "strangerthings.jpg", "Quando Will Byers desaparece misteriosamente, seus amigos iniciam uma busca pelo garoto, descobrindo experimentos secretos, forças sobrenaturais e uma garota estranha com poderes telecinéticos.", 4, "4.5 estrelas", "Millie Bobby Brown, Finn Wolfhard")
tema_suspense.adicionar_serie(serie_stranger_things)

serie_dark = Serie("Dark", "dark.jpg", "Em uma cidade pequena, desaparecimentos inexplicáveis ​​levam quatro famílias a uma busca frenética por respostas enquanto tentam desvendar um mistério que abrange três gerações.", 3, "4.8 estrelas", "Louis Hofmann, Oliver Masucci")
tema_suspense.adicionar_serie(serie_dark)

serie_narcos = Serie("Narcos", "narcos.jpg", "Baseada na história real do narcotraficante Pablo Escobar, essa série retrata a vida do poderoso chefão do tráfico e as forças policiais e políticas que tentam capturá-lo.", 5, "4.7 estrelas", "Wagner Moura, Pedro Pascal")
tema_suspense.adicionar_serie(serie_narcos)

tema_policial = Tema("Policial")

serie_lupin = Serie("Lupin", "lupin.jpg", "Em Paris, o ladrão profissional Assane Diop busca vingança pelo injusto tratamento de seu pai, e usa as habilidades de ladrão para expor os crimes da elite.", 2, "4.6 estrelas", "Omar Sy, Ludivine Sagnier")
tema_policial.adicionar_serie(serie_lupin)

serie_casa_de_papel = Serie("La Casa de Papel", "lacasadepapel.jpeg", "Oito ladrões fazem reféns e se trancam na Casa da Moeda da Espanha com o ambicioso plano de realizar o maior roubo da história.", 5, "4.9 estrelas", "Úrsula Corberó, Álvaro Morte")
tema_policial.adicionar_serie(serie_casa_de_papel)

tema_drama = Tema("Drama")

serie_breaking_bad = Serie("Breaking Bad", "breakingbad.jpg", "Um professor de química do ensino médio com câncer terminal se junta a um ex-aluno para produzir e vender metanfetamina para garantir o futuro financeiro de sua família.", 6, "4.9 estrelas", "Bryan Cranston, Aaron Paul")
tema_drama.adicionar_serie(serie_breaking_bad)

serie_ozark = Serie("Ozark", "ozark.jpg", "Um consultor financeiro se muda com sua família para as montanhas Ozark para lavar 500 milhões de dólares e acalmar um traficante de drogas.", 4, "4.7 estrelas", "Jason Bateman, Laura Linney")
tema_suspense.adicionar_serie(serie_ozark)

serie_the_witcher = Serie("The Witcher", "witcher.jpg", "Um caçador de monstros solitário luta para encontrar seu lugar em um mundo onde as pessoas frequentemente se provam mais perversas do que as bestas.", 2, "4.6 estrelas", "Henry Cavill, Anya Chalotra")
tema_suspense.adicionar_serie(serie_the_witcher)

serie_the_crown = Serie("The Crown", "thecrown.jpg", "Esta série dramática segue a vida da rainha Elizabeth II desde sua juventude até a atualidade, explorando os eventos históricos que moldaram o segundo reinado mais longo da história britânica.", 5, "4.8 estrelas", "Olivia Colman, Tobias Menzies")
tema_drama.adicionar_serie(serie_the_crown)

serie_gambito = Serie("O Gambito da Rainha", "gambito.jpg", "Em um orfanato dos anos 1950, uma jovem prodígio do xadrez luta contra o vício enquanto enfrenta os melhores jogadores do mundo.", 1, "4.5 estrelas", "Anya Taylor-Joy, Bill Camp")
tema_drama.adicionar_serie(serie_gambito)

serie_suits = Serie("Suits", "suits.jpg", "Mike Ross, um jovem inteligente que abandonou a faculdade de direito, é contratado pelo advogado mais bem-sucedido de Nova York, Harvey Specter, apesar de não ter diploma de direito.", 9, "4.7 estrelas", "Gabriel Macht, Patrick J. Adams")
tema_drama.adicionar_serie(serie_suits)

catalogo = [tema_suspense, tema_policial, tema_drama]

### FIM DA CRIAÇÃO DOS OBJETOS ###

@app.route('/')
def home():
    # SE A CHAVE "login" NÃO EXISTIR DENTRO DO DICIONÁRIO session...
    if "login" not in session:
        # cria a chave "login" na session e coloca o valor False
        session["login"] = False
    
    # seleção aleatória da série destaque
    serieDestaque = choice(choice(catalogo).series)

    # chamar a template index.html passando pra ela a série destaque e o catálogo 
    conteudo = render_template('index.html', parSerieDestaque=serieDestaque, parCatalogo=catalogo)
    return conteudo

# como essa rota pode chegar vinda de um formulário, precisamos ativar os métodos 
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    # pode chegar nessa rota vindo de um formulário ou vindo de um link.
    # quando chegar nessa rota vindo de um formulário:
    if request.method == "POST":
        # vamos pegar o que foi preenchido no formulário
        # os campos do formulário ficam armazenados no dicionário request.form
        # as chaves do dicionário são os "name" dos campos do form na template
        # os valores do dicionário são as respostas que a pessoa preencheu nos campos
        if request.form["email"] == "eu@eu.com" and request.form["senha"] == "aaa":
            # Se a pessoa acertar o login, vai alterar a session "login" para True
            # Assim saberemos em qualquer página do site se a pessoa fez login ou não
            session["login"]=True
            # depois do login, chamamos o painel de gerenciamento passando pra ele o catálogo
            conteudo = render_template("dashboard.html",parCatalogo=catalogo)
        else:
            # Se errar o login:
            mensagem = "Login inválido"
            # chamamos o template de mensagem pra mostrar uma mensagem de erro
            conteudo = render_template("mensagem.html", parMensagem=mensagem)
    
    # esse elif pertence ao primeiro IF dessa def
    # quando chegar nessa rota via GET (por um link por exemplo) 
    # mas já ter feito login:
    elif request.method == "GET" and session["login"] == True:        
        # se já fez login pode acessar o painel de gerenciamento
        conteudo = render_template("dashboard.html",parCatalogo=catalogo)
    else:
        # quando chegar nessa rota sem ter feito login:
        mensagem = "Acesso negado"
        # não pode acessar o painel, 
        # por isso chamamos a template que mostra a mensagem de erro
        conteudo = render_template("mensagem.html", parMensagem=mensagem)

    # depois dos testes de login vai retornar o conteúdo correto:
    return conteudo

@app.route("/logout")
def logout():
    # primeiro verificamos se existe algum login na session
    # caso seja o primeiro acesso ao site e a pessoa digite o endereço do logout,
    # não vai ter a chave "login" dentro da session para alterar.

    # se a chave "login" existir dentro da session...
    if "login" in session:
        # altera o valor de "login" na session e coloca o valor False
        # isso vai efetivar o logout
        session["login"] = False    

    # repete os passos de carregamento da home depois de ter feito logout 
    serieDestaque = choice(choice(catalogo).series)
    conteudo = render_template('index.html', parSerieDestaque=serieDestaque, parCatalogo=catalogo)
    return conteudo



@app.route("/adicionar_tema", methods=["GET", "POST"])
def adicionar_tema():

    nome = request.form["tema"]
    novo_tema = Tema(nome)
    catalogo.append(novo_tema)
    
    return render_template('dashboard.html', parCatalogo=catalogo)

@app.route("/modificar_tema/<nome_tema>", methods=["GET", "POST"])
def modificar_tema(nome_tema):
    
    tema = Tema(nome_tema)
    
    if request.method == "POST" and request.form.get("form_id") == "form1":
       nome = request.form["novo_nome"]
       for i in catalogo:
           if i.nome == tema.nome:
               i.nome = nome
               break
       conteudo = render_template("dashboard.html", parCatalogo=catalogo)
    
    elif request.method == "POST" and request.form.get("form_id") == "form2":
        for i in catalogo:
            if i.nome == tema.nome:
                catalogo.remove(i)
                break
        conteudo = render_template("dashboard.html", parCatalogo=catalogo)
        
    else:
        conteudo = render_template("modificar_tema.html", partema=tema)
    return conteudo
    






    



# EXECUTAR O PROGRAMA (RODAR O SITE)
if __name__ == '__main__':
    app.run(debug=True)
