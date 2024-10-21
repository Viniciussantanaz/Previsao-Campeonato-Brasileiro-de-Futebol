from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://onefootball.com/pt-br/competicao/brasileirao-betano-16/resultados') #Acessando o site
time.sleep(5) # tempo de 5seg para página carregar

botao = driver.find_element(By.ID, 'onetrust-accept-btn-handler') #Botão cookies que esta bloqueando a pagina

botao.click() #Clicando no botão 
time.sleep(3)

botao2 = driver.find_element(By.CLASS_NAME, 'Button_ghost__3pIFo') #Botão para acessar todos os jogos do campeonato

botao2.click() #Cliacando no botão
time.sleep(3)

div = driver.find_element(By.CLASS_NAME, 'MatchCardsListsAppender_container__y5ame') # Div que obtem o link de todos os jogos
links = div.find_elements(By.TAG_NAME,'a') #Pegando os links dos jogos

urls = [link.get_attribute('href') for link in links] # Add os links em uma lista

driver.quit()
df = {'time_casa':[], # df de stats vazia
      'time_fora':[], 
      'chutes_casa':[], 
      'chutes_gol_casa':[], 
      'chutes_fora':[],
      'chutes_gol_fora':[]}
i = 0
while i < len(urls): # Laço para acessar todos os jogos atraves do link
    try: #Tratamento para reniciar o driver caso falhe
        driver.get(urls[i])
        time.sleep(5)        
    
        try: #Tratamento de erro para os jogos qua não tem estátiscas.
            stats = driver.find_element(By.CLASS_NAME, 'MatchStats_list__29Ej7')
            stats = stats.text.split('\n')
            df['chutes_casa'].append(stats[3])
            df['chutes_gol_casa'].append(stats[6])
            df['chutes_fora'].append(stats[5])
            df['chutes_gol_fora'].append(stats[8])
            df['time_casa'].append(driver.find_element(By.CLASS_NAME, 'MatchScoreTeam_home__9Ehdk').text)
            df['time_fora'].append(driver.find_element(By.CLASS_NAME, 'MatchScoreTeam_away__O_HfB').text)
        except: 
            continue
        finally: 
            driver.quit()
            i+= 1
    except:
        driver.quit()
        # Reiniciar o Driver caso dê erro de rede.
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        time.sleep(5)

df = pd.DataFrame(df) # Transformando o Df em uma tabela.

df.to_excel('stats.xlsx',index=False, sheet_name='stats') #Exportando para excel.
