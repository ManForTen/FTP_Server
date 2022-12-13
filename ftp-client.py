import socket


def cts(filename: str) -> None:  # Отправление файла на сервер
    with open(filename, 'rb') as f:
        a = f.read()
    sock.send(a)

def ctc() -> None:  # Принятие файла с сервера"
    filename = sock.recv(1024).decode()
    print(filename)
    a = b''
    while True:
        data = sock.recv(1024)
        a += data
        if not data:
            break
    with open(filename, 'wb') as f:
        f.write(a)

HOST = 'localhost'
PORT = 9020

print('''
    Доступные команды:
    pwd - Показывает название рабочей директории
    ls - Показывает содержимое текущей директории
    cat <Название файла> - Отправляет содержимое файла
    mkdir <Название директории> - Создает директорию
    rmdir <Название директории> - Удаляет директорию
    remove <Название файла> - Отправляет содержимое файла
    rename <Название файла> <Новое название файла> - Переименовывает файл
    rm <Название файла> - Удаляет файл
    cts <Название файла> - Копирование файла на сервер
    ctc <Название файла> - Копирование файла на клиент
    exit - Отключение клиента
    ''')

while True:
    request = input('Введите действие:')

    sock = socket.socket()
    sock.connect((HOST, PORT))
    sock.send(request.encode())
    if request[:4] == 'cts ':
        cts(request[4:])

    response = sock.recv(1024).decode()
    if response == 'file':
        ctc()
    print(response)
    sock.close()
    if response == 'exit':
        print("Отключение от сервера.")
        break