import os
import time
import datetime

# Diretório de log
log_dir = "/caminho/para/sua/pasta/de/log"

# Data atual
data_atual = datetime.datetime.now()

# Lista os arquivos no diretório de log
arquivos = os.listdir(log_dir)

# Para cada arquivo no diretório de log
for arquivo in arquivos:
    # Caminho completo do arquivo
    arquivo_path = os.path.join(log_dir, arquivo)
    
    # Pega a data da última atualização do arquivo
    ultima_atualizacao = os.path.getmtime(arquivo_path)
    ultima_atualizacao = datetime.datetime.fromtimestamp(ultima_atualizacao)
    
    # Se a última atualização for menor que (hoje - 7 dias), deleta o arquivo
    if ultima_atualizacao < (data_atual - datetime.timedelta(days=7)):
        os.remove(arquivo_path)
        print(f"Arquivo {arquivo} deletado.")
# Removendo dados duplicados com drop_duplicates()

 df= df.drop_duplicates() 
