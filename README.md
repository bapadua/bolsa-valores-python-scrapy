# bolsa-valores-python-scrapy
Webscraping com python 3.7 utilizando Selenium, Firefox 
buscando a cotação no site da UOL, imprimindo na tela os valores encontrados, e enviando um email, utilizando o gmail.

#Configuracoes
No arquivo main.py informe o username e password do gmail para envio do email.

#Para iniciar
python main.py emailquevaireceberoarquivo@email.com acaodesejada(ex: Petr4(Petrobrás)).

#Exemplo
python main.py seuemail@gmail.com petr4
-- aqui ele vai enviar para seu email o valor da acao da petrobrás(petr4-sa) para o email informado.
python main.py seuemail@gmail.com petr4 lame3 hapv
-- o mesmo de cima porém ele vai buscar 3 valores sendo que pode ser *infinitos* valores desde que esteja no domínio da UOL.
