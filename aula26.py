x = "familia"

try: # Tentativa que será True ou False
    print(x)
except: # Executa se ouver erro
    print("Erro no programa")
else:  # Executa se NÃO tiver erro
    print("Tudo certo")
finally: # Executa sempre
    print("Fim do tratamento")