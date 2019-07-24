import os
import sysconfig

#=- Este aquivo printa o conteudo\\
#=- contiudo nos aquivos ".txt" que contem\\
#=- o seguinte conteudo:\\
#=- nome, atributos, pontos de atributos\\
req = None

ref_arquivo = open('c:\\Users\\zambe\\Desktop\\trabalhosizaias\\rpg_free\\anao.txt','r')   
string_arquivo = ref_arquivo.read()
print(string_arquivo[:256])

ref_arquivo = open('c:\\Users\\zambe\\Desktop\\trabalhosizaias\\rpg_free\\assacino.txt','r')   
string_arquivo = ref_arquivo.read()
print(string_arquivo[:256])

ref_arquivo = open('c:\\Users\\zambe\\Desktop\\trabalhosizaias\\rpg_free\\bercerker.txt','r')   
string_arquivo = ref_arquivo.read()
print(string_arquivo[:256])

ref_arquivo = open('c:\\Users\\zambe\\Desktop\\trabalhosizaias\\rpg_free\\elfo.txt','r')   
string_arquivo = ref_arquivo.read()
print(string_arquivo[:256])

ref_arquivo = open('c:\\Users\\zambe\\Desktop\\trabalhosizaias\\rpg_free\\guardian.txt','r')   
string_arquivo = ref_arquivo.read()
print(string_arquivo[:256])

ref_arquivo = open('c:\\Users\\zambe\\Desktop\\trabalhosizaias\\rpg_free\\mago.txt','r')   
string_arquivo = ref_arquivo.read()
print(string_arquivo[:256])

ref_arquivo = open('c:\\Users\\zambe\\Desktop\\trabalhosizaias\\rpg_free\\ogro.txt','r')   
string_arquivo = ref_arquivo.read()
print(string_arquivo[:256])
try: 
    ref_arquivo
except:
    print('Erro na conexao!')
    exit()
    print(req.text)
