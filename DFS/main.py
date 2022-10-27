import os
os.chdir("C:/Users/brewa/OneDrive/Documents/ctf/root-me-ctf-21-10-22/prog-graphs")

from graphes_avec_class import graphs

import socket

host = "ctf10k.root-me.org"
port = 8001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


while True:
    eq = s.recv(2048).decode()
    print(eq)
    eq = eq.replace("Hello there! I need some help for my homework, pleeeease.\n", '').replace("\n>", '').replace("Okay, this seems correct!\n", '')

    question = str(eq.split('\n')[:1])
    graph_data = eq.split('\n')[1:]

    myGraph = graphs()

    le_connections = []
    for node in graph_data:
        node = node.replace("Node ", '')
        if "no" in node:
            node = node.replace(" has no directed edge", '')
            myGraph.ajouterSommet(node.replace(" ", ''))
        else:
            name, connections = tuple(node.split(" has a directed edge to : "))
            myGraph.ajouterSommet(name.replace(" ", ''))
            le_connections.append((name, connections.split(", ")))


    for nom, connections in le_connections:
        for conn in connections:
            myGraph.ajouterArete(nom.replace(' ', ''), conn.replace(" ", ''))

    question = question.split("Here's my graph's adjacency list, can you tell me if I can reach node ")[1]

    question = question.replace(" please? (yes / no)\"]", '')

    target, name = question.split(" from ")


    answer = "yes" if myGraph.existeChemin(name, target) != [] else "no"

    print("[+] Sending", answer, "for", name, "->", target)
    answer = answer + '\n'
    s.send(answer.encode())








