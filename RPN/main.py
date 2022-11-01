import socket

host = "ctf10k.root-me.org"
port = 8002
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

eq = s.recv(1024).decode()

print(eq)
eq = eq.replace("Can you solve this for me?", '').replace('\n', '').replace(">", '')

while True:
    nb = []
    for poss in eq.split(' '):

        if poss == '':
            pass
        elif poss in ['+', '-', 'x']:
            if poss == '+':
                nb[-2] += nb[-1]
            elif poss == '-':
                nb[-2] -= nb[-1]
            else:
                nb[-2] = nb[-2] * nb[-1]
            nb.pop()
        else:
            nb.append(int(poss))


    total = nb[0]


    print("Result :", total)

    total = str(total) + '\n'
    s.send(total.encode())

    eq = s.recv(1024).decode()
    print(eq)
    eq = eq.replace("That's correct!\nAnd this?\n", '')
    eq = eq.replace("\n> ", "").replace("\n", '')

