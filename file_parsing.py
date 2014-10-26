## module with file parsing functions to extract and threat some data

sep=":"

"""
/*\ file parsing function /*\
Creates a dictionnary for first option, used for graph visualization
"""

def     extract_graph():
    data = dict()
    try:
        fileStream = open("Makefile", 'r')
        for line in fileStream:
            if is_valid_entry(line):
                line = line.replace(":", "")
                line = " ".join(line.split())
                key = get_linekey(line)
                values = get_linevalues(line)
                if len(data) == 0:
                    data[key] = values
                else:
                    set_in_graph(data, key, values)
    except IOError:
        print("there is no Makefile in current directory")
    return data

"""
/*\ file parsing function /*\
Creates 2 dictionnaries for second option, one used for command line finding and the other one for commands listing
"""

def     extract_data():
    data = dict()
    commands = dict()
    key = str()
    try:
        fileStream = open("Makefile", 'r')
        for line in fileStream:
            line = " ".join(line.split())
            if len(line) > 0 and is_valid_entry(line):
                line = line.replace(":", "")
                key = get_linekey(line)
                values = get_linevalues(line)
                if data.get(key) == None:
                    data[key] = list()
                for i, item in enumerate(values):
                    for itemkey in item.keys():
                        if data.get(itemkey) == None:
                            data[itemkey] = list()
                        data[itemkey].append(key)
            elif len(line) > 0:
                if commands.get(key) == None:
                    commands[key] = list()
                commands[key].append(line)
    except IOError:
        print("there is no Makefile in current directory")
    return (data, commands)

"""
/*\ file parsing function /*\
Checks if the line is a rule or command line
"""

def     is_valid_entry(line):
    if line.count(sep) == 1:
        return True
    return False

"""
/*\ file parsing function /*\
Used for first option dictionnary creation, fills recursively the dictionnary
"""

def     set_in_graph(data, key, values):
    for index, items in data.items():
        if items != None:
            for i, item in enumerate(items):
                for itemkey in item.keys():
                    if itemkey == key:
                        if data[index][i][itemkey] == None:
                            data[index][i][itemkey] = values
                        else:
                            data[index][i][itemkey].append(values)
                        return
                    else:
                        set_in_graph(data[index][i], key, values)

"""
/*\ file parsing function /*\
Splits the line to get dictionnary key from input file
"""

def     get_linekey(line):
    return line.split()[0]

"""
/*\ file parsing function /*\
Splits the line to get dictionnary values from input file
"""

def     get_linevalues(line):
    ret = list()
    for word in line.split()[1:]:
        ret.append({word : None})
    return ret
