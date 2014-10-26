## mobule for data processing to treat data

"""
/*\ data process function /*\
Creates graph for dot with nodes and edges
"""

def     prepare_graph(dot, data, prev):
    print(data)
    for i, index in enumerate(data.keys()):
        dot.node(index, index)
        if (prev != None):
            dot.edge(index, prev, constraint='true')
    for index, items in data.items():
        if (items != None):
            for j, item in enumerate(items):
                for itemkey in item.keys():
                    prepare_graph(dot, data[index][j], index)

"""
/*\ data process function /*\
Creates adjacent matrix through the dictionary created from the input file
"""

def     do_adja_matrix(data):
    guys = sorted(data.keys())
    matrix = []
    index = 0
    while index < len(guys):
        i = 0
        matrix.append([])
        while i < len(guys):
            j = 0
            nb = 0
            while j < len(data[guys[index]]):
                if data[guys[index]][j] == guys[i]:
                    nb = 1
                j += 1
            matrix[index].append(nb)
            i += 1
        index += 1
    return matrix

"""
/*\ data process function /*\
Finds the way through adjacente matrix for compilation commands
"""

def     finder(data, commands, matrix, index):
    for i, node in enumerate(matrix[index]):
        if node == 1:
            for command in commands[sorted(data.keys())[i]]:
                print(command)
            finder(data, commands, matrix, i)
