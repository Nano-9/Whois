# script criado por Nano-9                              |\
# Telegram: https://t.me/rdzin9                         |   >>> Nano-9
# Dúvidas entre em contato                              |/

import os
import sys
import urllib.request
import requests
import Baner_whois
import datetime
from bs4 import BeautifulSoup
from time import sleep

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

SESSAO_RUN = requests.Session()
DATETIMESN = datetime.datetime.now()

try:

        internet_teste = urllib.request.urlopen("https://www.google.com")

except KeyboardInterrupt:

        print("[+] Serviço cancelado pelo usuário!")
        sleep(0.5)
        sys.exit()

except:

        print("[+] Você não tem conexão com a internet!")
        sys.exit()
else:

        while True:
                Baner_whois.MudarBaner()

                try:

                        site_alvo = str(input("\033[1;36m[+] Site alvo:\033[m ")).strip().lower().replace(" ","")
                        print()
                except KeyboardInterrupt:
                        print("[!] Serviço cancelado pelo usuário!")
                        sleep(0.5)
                        sys.exit()
                except:
                        print("[!] OOOPS... Parece que ocorreu um erro :( !")
                        sys.exit()
                else:
                        if site_alvo.endswith(".br"):

                                try:
                                        print("\033[1;31m[!] Conectando ao site alvo...\033[m")
                                        start_site = SESSAO_RUN.get("https://who.is/whois/"+site_alvo.strip().lower(),headers=headers)


                                        if start_site.status_code == 200:
                                                print("\033[1;32m[✓] Conexão estabelecida!\033[m")
                                                print("\033[1;32m[*] RECEBENDO DADOS...\033[m\n")
                                                sleep(1)
                                                dados = BeautifulSoup(start_site.text,"html.parser")
                                                tag_html = dados.find("pre",attrs={"style":"border:0px;"})

                                                texto = tag_html.text
                                                if texto != None:
                                                        print("\n\n\033[1;33m################## PESQUISA CONCLUÍDA DO SITE "+"####################\033[m\n\n")

                                                        print("\033[1;31m[*] \033[1;32mSITE ALVO:\033[m {}".format(site_alvo))
                                                        print("\033[1;31m[*]\033[m \033[1;32mDATA DA PESQUISA:\033[m {}".format(DATETIMESN.strftime("%d/%m/%Y")))
                                                        print("\033[1;31m[*]\033[m \033[1;32mHORÁRIO DA PESQUISA:\033[m {}".format(DATETIMESN.strftime("%H:%M:%S")))
                                                        print("\n\n"+texto+"\n\n")

                                                else:

                                                        print("\033[1;31m[!] O site {} não pode ser encontrado!\033[m\n".format(site_alvo))
                                        else:

                                                print("\033[1;31m[!] Requisição com o site {} falhou :( !\033[m".format(site_alvo))

                                except KeyboardInterrupt:
                                        print("[!] Serviço encerrado pelo usuário!")
                                        sleep(0.5)
                                        sys.exit()
                                except:
                                        print("[!] OOOPS... Parece que ocorreu um erro :( !")
                                        sleep(0.5)
                                        sys.exit()
                                finally:
                                        pass

                        else:

                                print("[*] O site precisa ter um domínio com o final .br !")
                                sys.exit()

                break
