x = ""

try: # Tentativa que será True ou False
    print(x)
except: # Executa se ouver erro
    print("Erro no programa")
else:  # Executa se NÃO tiver erro
    print("Tudo certo")
finally: # Executa sempre
    print("Fim do tratamento")

if not x:
    raise Exception("Variável x sem valor atribuido.") # Dispara um erro