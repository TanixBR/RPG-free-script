import os
import sysconfig

#=- Este aquivo printa o conteudo\\
#=- contiudo nos aquivos ".txt" que contem\\
#=- o seguinte conteudo:\\
#=- nome, atributos, pontos de atributos\\
req = None

ref_arquivo = open('anao.txt','r')   
string_arquivo = ref_arquivo.read()
print(string_arquivo[:256])

ref_arquivo = open('assacino.txt','r')   
string_arquivo = ref_arquivo.read()
print(string_arquivo[:256])

ref_arquivo = open('bercerker.txt','r')   
string_arquivo = ref_arquivo.read()
print(string_arquivo[:256])

ref_arquivo = open('elfo.txt','r')   
string_arquivo = ref_arquivo.read()
print(string_arquivo[:256])

ref_arquivo = open('guardian.txt','r')   
string_arquivo = ref_arquivo.read()
print(string_arquivo[:256])

ref_arquivo = open('mago.txt','r')   
string_arquivo = ref_arquivo.read()
print(string_arquivo[:256])

ref_arquivo = open('ogro.txt','r')   
string_arquivo = ref_arquivo.read()
print(string_arquivo[:256])
try: 
    ref_arquivo
except:
    print('Erro na conexao!')
    exit()
    print(req.text)
