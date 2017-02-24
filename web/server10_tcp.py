'''
Измените ваш echo сервер так, что бы он работать одновременно с 10 клиентами.
'''
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)

while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    if not data: conn.close()
    if data.decode('utf8').strip() == 'close': conn.close()
    conn.send(data)
    conn.close()



