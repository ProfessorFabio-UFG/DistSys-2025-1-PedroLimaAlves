import zmq

from constPS import *  # Defina suas constantes como HOST e PORT

context = zmq.Context()
s = context.socket(zmq.SUB)  # Cria um socket de subscriber
p = "tcp://" + HOST + ":" + PORT  # Endereço do servidor
s.connect(p)  # Conecta-se ao servidor

# Inscreve-se para os tópicos TIME, TEMP e HUMIDITY
s.setsockopt_string(zmq.SUBSCRIBE, "TIME")      # Assina o tópico TIME
s.setsockopt_string(zmq.SUBSCRIBE, "TEMP")      # Assina o tópico TEMP
s.setsockopt_string(zmq.SUBSCRIBE, "NOME")  # Assina o tópico NOME
s.setsockopt_string(zmq.SUBSCRIBE, "MATRICULA")  # Assina o tópico MATRICULA

for i in range(5):  # Realiza 5 iterações
    msg = s.recv()  # Recebe uma mensagem
    print(bytes.decode(msg))  # Exibe a mensagem

