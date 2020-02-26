# Python webscrapper

Webscraping com python 3.7 utilizando Selenium, Firefox buscando a cotação no site da UOL, imprimindo na tela os valores encontrados, e enviando um email, utilizando o gmail.


# Configurações

No arquivo main.py informe o username e password do gmail para envio do email.

# Para rodar

python main.py emailquevaireceberoarquivo@email.com cotacao

## Exemplo 1:
python main.py seuemail@gmail.com  petr4 
-- aqui ele vai enviar para seu email o valor da acao da petrobrás(petr4-sa) para o email informado.


## Exemplo 2:
python main.py seuemail@gmail.com petr4 lame3 hapv 
-- o do exemplo 1 porém ele vai buscar 3 valores sendo que pode ser _infinitos_ valores desde que esteja no domínio da UOL.
