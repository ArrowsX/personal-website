## Introdução à Programação Prática usando Python



### Um pouco sobre mim
- Engenharia de Minas (3⁰ano) <!-- .element: class="fragment" data-fragment-index="1" -->
- Fez MAC2166 <!-- .element: class="fragment" data-fragment-index="2" -->
- Já copiou EP e fechou com 6,4 de média <!-- .element: class="fragment" data-fragment-index="3" -->
- Nunca programou antes da faculdade <!-- .element: class="fragment" data-fragment-index="4" -->



#### E agora...
## Faço milagres com python <!-- .element: class="fragment" -->



### O que não esperar do workshop <!-- .element: class="fragment" data-fragment-index="1" -->
- Aprender sobre algoritmos <!-- .element: class="fragment" data-fragment-index="2" -->
- Se tornar um expert em Python <!-- .element: class="fragment" data-fragment-index="3" -->
- Revisão para rec de numérico <!-- .element: class="fragment" data-fragment-index="4" -->
- Deixar a mãe impressionada <!-- .element: class="fragment" data-fragment-index="5" -->
### O que esperar do workshop <!-- .element: class="fragment" data-fragment-index="6" -->  
- Ter um gostinho do Python na vida real <!-- .element: class="fragment" data-fragment-index="7" -->
- Familiarização com as principais ferramentas utilizadas <!-- .element: class="fragment" data-fragment-index="8" -->



### Objetivos
- Enviar um e-mail com Python <!-- .element: class="fragment" data-fragment-index="1" -->
- Familiarização com cmd/Powershell <!-- .element: class="fragment" data-fragment-index="2" -->
- Baixar um vídeo do Youtube <!-- .element: class="fragment" data-fragment-index="3" -->
- Construir um chatbot no Telegram <!-- .element: class="fragment" data-fragment-index="4" -->



### Ferramentas
- Python 3.4+
- pip (gerenciador de pacotes)
- IDLE ou qualquer outro editor de texto
- Prompt de comando (cmd) ou Powershell
Note:
Tentem digitar python ou pip no cmd/powershell, se não der certo vão ter que reinstalar



## Enviando e-mails Usando Python


### Modulo SMTP
SMTP (Simple Mail Transfer Protocol) é o protocolo padrão para envio de e-mails através da Internet.


### Vamos trabalhar agora
```python
import smtplib

# Cria uma conexão SMTP em smtp.gmail.com na porta 587
server = smtp.SMTP('smtp.gmail.com', 587)
# Validação do Gmail no server SMTP
server.ehlo()
# Coloca o email no modo de segurança
server.starttls()

server.login('seu-usuario', 'sua-senha')
server.sendmail('email-origem', 'email-destino', 'Hello World')
server.quit()
```


### Aprimorando o Código
```python
import smtplib

# Credenciais
username = 'seu-usuario'
password = 'sua-senha'
recipient = 'email-destino'

server = smtp.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()

server.login(username, password)
server.sendmail(username, recipient, content)

server.quit()
```


### Aprimorando o Código
```python
username = 'seu-usuario'
password = 'sua-senha'
recipient = 'email-destino'

subject = "Aula Python"
message = "Hello World"

headers = "\r\n".join([
    "from: " + username,
    "subject: " + subject,
    "to: " + recipient,
    "mime-version: 1.0",
    "content-type: text/html"])

content = headers + "\r\n\r\n" + message
```
Note:
MIME (Multipurpose Internet Mail Extensions) é uma norma da internet para o formato
das mensagens de correio eletrônico.



## Familiarização com interpretadores de linha de comando


### Cmd / Powershell / Terminal
Programas de computador responsáveis por tomar ações baseadas nas
sequências de comandos textuais inseridas


### Dir / ls
```powershell
C:\Users\Python Rules> dir
 O volume na unidade C é OS
 O Número de Série do Volume é F32D-A48F

 Pasta de C:\Users\Python Rules

 03/12/2008 04:00   <DIR>         .
 03/12/2008 04:10   <DIR>         .
 03/12/2008 00:09   <DIR>         Desktop
 03/12/2008 00:54   <DIR>         Documents
 03/12/2008 01:48   <DIR>         Downloads
 03/12/2008 00:09   <DIR>         Downloads
 03/12/2008 03:29   <DIR>         Music
 03/12/2008 02:04   <DIR>         Pictures
 03/12/2008 00:32   <DIR>         Videos
```


### Cd
```powershell
C:\Users\Python Rules> cd Desktop

C:\Users\Python Rules\Desktop> cd ..

C:\Users\Python Rules>
```


### Mkdir
```powershell
> mkdir Desktop\workspace
```


### Copy / cp
```powershell
> copy Desktop\teste.txt .
```


### Del / rm
```powershell
> del Desktop\teste.txt
```


### Move / rm
```powershell
> move teste.txt Desktop
```


### Instalando novas bibliotecas
```powershell
> pip install modulo-ou-biblioteca
```


## E o mais importante...


### exit
```powershell
> exit
```



## Baixando vídeos com Python


### Bibliotecas necessárias
```powershell
> pip install beautifulsoup4
> pip install youtube-dl
```


### Exemplo BeautifulSoup4
```python
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/results?search_query=find+you'
content = urlopen(url).read() # Lê o url como uma string
soup = BeautifulSoup(content, 'html.parser') # Lê em HTML
print(soup.prettify()) # Deixa bonito para ver
```
Note:
Se quiserem ver o nível de feiura, podem dar print nas variáveis
content e soup


## Usando youtube-dl
```python
import youtbe_dl

ydl_opts = {} # Opções customizadas
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=IOpXKKfuYZo'])
```


## Juntar e aprimorar
```python
from urllib.request import urlopen
import youtube_dl
from bs4 import BeautifulSoup

query = 'find you'
query = '+'.join(query.lower().split())
url = 'https://www.youtube.com/results?search_query=' + query
content = urlopen(url).read()
soup = BeautifulSoup(content, 'html.parser')
tag = soup.find('a', {'rel': 'spf-prefetch'}) # Acha tags
video_url = 'https://www.youtube.com' + tag.get('href')

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
```
Note:
Alguém sabe explicar o que a segunda linha do código faz?



## Chatbots no Telegram


### Chatbots no Telegram
Chatbots são simplesmente contas do Telegram operadas por um software - não humano


### Chatbots no Telegram
Eles podem pesquisar, transmitir, relembrar, conectar, integrar com outros serviços, ou até passar comandos para a IoT (Internet of Things)
Note:
IoT para quem não sabe é tipo uma network que conecta os aparelhos do dia-a-dia (as coisas) à internet.


#### Resumindo... <!-- .elements class="fragment" data-fragment-index="1" -->
## Ele abre portas para a imaginação <!-- .elements class="fragment" data-fragment-index="2" -->


### Telegram Bot API
```powershell
> pip install python-telegram-bot
```


### Recebendo TOKEN
- Adicione no Telegram @BotFather <!-- .element class="fragment" data-fragment-index="1" -->
- Inicie uma conversa e digite /newbot <!-- .element class="fragment" data-fragment-index="2" -->
- Siga as instruções seguintes <!-- .element class="fragment" data-fragment-index="3" -->
- Copia o TOKEN <!-- .element class="fragment" data-fragment-index="4" -->
Note:
TOKEN é uma chave única de acesso para autenticação individual


### Baby steps
```python
from telegram.ext import Updater

updater = Updater('TOKEN')
dispatcher = updater.dispatcher
```
Note:
dispatcher é a ferramenta que liga o seu TOKEN com os comandos


### Biblioteca anti-merda
```python
import logging

logging.basicConfig(
   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
   level=logging.INFO)
```
Note:
logging é a ferramenta que te informa se houve algum erro no programa


### Primeiro comando
```python
from telegram.ext import CommandHandler

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="Oi, você acabou de criar um bot foda!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
```


### Iniciando o bot
```python
# Inicia o bot
updater.start_polling()

# Finaliza o bot ao apertar Ctrl+C
updater.idle()
```


### Mais customização
```python
from telegram.ext import MessageHandler, Filters

def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text=update.message.text)

echo_handler = MessageHandler([Filters.text], echo)
dispatcher.add_handler(echo_handler)
```


### Muita informação?
## Vamos organizar o código <!-- .element: class="fragment" -->
Note:
Abre o IDLE e começa a organizar o código



#### Projeto Final:
## Juntar a porra toda <!-- .element: class="fragment" -->
Note:
Ou seja, vamos fazer um bot que baixa vídeo do youtube e depois manda um email para mim com o nome do título do vídeo



# Perguntas?
