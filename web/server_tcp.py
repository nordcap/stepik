'''Разработать простейший TCP echo сервер.

Требования

Запускается на IP адресе 0.0.0.0 и TCP порту 2222
Получает сообщения длинной не более 1024 байт и отправляет обратно клиенту
Закрывает соединение при получении сообщения с текстом close﻿
'''
import socket


# правильное чтение из сокета
def myreceive(sock, msglen):
    msg = ''  # сообщение
    while len(msg) < msglen:
        chunk = sock.recv(msglen - len(msg))
        if chunk == '':
            raise RuntimeError("broken")
        msg = msg + chunk
    return msg


# правильная запись в сокет
def mysend(sock, msg):
    totalsent = 0
    while totalsent < len(msg):
        sent = sock.send(msg[totalsent:])
        if sent == 0:
            raise RuntimeError("broken")
        totalsent = totalsent + sent


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(1)

conn, addr = s.accept()
while True:
    data = conn.recv(1024)
    # data = myreceive(conn, 1024)
    if not data: break
    # mysend(conn, data)
    if data.decode('utf8').strip() == 'close': conn.close()
    conn.send(data)


