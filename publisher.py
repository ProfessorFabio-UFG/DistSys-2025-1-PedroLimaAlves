import zmq
import time
from constPS import *  # Defina suas constantes como HOST e PORT

context = zmq.Context()
s = context.socket(zmq.PUB)  # Cria um socket de publisher
p = "tcp://" + HOST + ":" + PORT  # Defina o endereço de comunicação
s.bind(p)  # Associa o socket ao endereço

while True:
    time.sleep(5)  # Espera 5 segundos antes de enviar a próxima mensagem
    
    # Envia a hora atual
    msg_time = str.encode("TIME " + time.asctime())
    s.send(msg_time)  # Publica a hora atual
    
    # Envia a temperatura
    temp = 22.5 
    msg_temp = str.encode(f"TEMP {temp}")
    s.send(msg_temp)  # Publica a temperatura

    # Enviar o meu nome
    nome = "Pedro Henrique Lima"
    msg_nome = str.encode (f"NOME {nome}")
    s.send(msg_nome) # Publica meu nome

    # Enviar minha matrícula
    matricula = "202206799"
    msg_matricula = str.encode (f"MATRICULA {matricula}")
    s.send(msg_matricula) # Publica minha matrícula
