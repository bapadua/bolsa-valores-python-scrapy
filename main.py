import sys
from selenium import webdriver
#excel
from openpyxl import Workbook
#email
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


excel = Workbook()
planilha = excel.active
planilha.title = "Pesquisas"
planilha['A1'] = 'COTACAO'

args = sys.argv[2:]
email = sys.argv[1]

search_list = []
result_list = []
host = 'https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/'
postfix = '-sa'
class_ref = 'chart-info-val.ng-binding'

def separator ():
    """
    Não faz nada apenas imprime uma linha para separar
    """
    pass

    print("================================================================")

def getCotation(empresa):
    """
    Monta a url de pesquisa para o site da UOL versao (25/02/2020)
    """
    return host + empresa.lower() + postfix


def getValue(empresa = 'petr4'):
    """
    Utitliza o navegador firefox para buscar os dados pela classe css informada,
    imprimindo na tela o titulo da pagina e o valor da cotação encontrada.
    Firefox driver = geckodriver
    """
    pass
    try:
        driver = webdriver.Firefox()
        driver.get(getCotation(empresa))
        title = driver.title
        value = driver.find_element_by_class_name(class_ref).text
        driver.quit()
        result_list.append(title + ' ' + value)
        print(title)
        print(value)
    except Exception as e:
        print('ocorreu um erro: %s' % e)
    None

for param in args: 
    search_list.append(param)

separator()

for info in search_list:
    if(len(info)) < 4:
        print('Pesquisa invalida')
    else:
        getValue(info)

separator()
planilha.append(result_list)

excel.save("./cotacoes/cotacao.xlsx")

try:
    # conexão com os servidores do google
    smtp_ssl_host = 'smtp.gmail.com'
    smtp_ssl_port = 465
    
    """
    IMPORTANTE: é preciso configurar o gmail pra aceitar aplicativos não seguros
    """
    username = 'seuemail@gmail.com'
    password = 'suasenha'

    from_addr = 'seuemail@gmail.com'
    to_addrs = email
    
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addrs
    msg['Subject'] = 'Cotacao Bolsa'
    body = '\n Mensagem automatica'
    msg.attach(MIMEText(body, 'plain'))
    filename = './cotacoes/cotacao.xlsx'
    attachment = open('./cotacoes/cotacao.xlsx','rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)
    attachment.close()
    # conectaremos de forma segura usando SSL
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    # para interagir com um servidor externo precisaremos
    # fazer login nele
    server.login(username, password)
    server.sendmail(from_addr, to_addrs, msg.as_string())
    server.quit()
    print('email enviado')
except Exception as e:
    print('erro ao enviar email', e)