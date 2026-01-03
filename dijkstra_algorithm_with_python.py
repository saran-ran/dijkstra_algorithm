def dijkstra_explain(L, prev, W, Q, start, terminal):
    minimun_temp_dist = sorted(L, key=L.get)[len(L)-len(Q)]
    print(f"     choose u={minimun_temp_dist} with minimum temp. dist. L(V)\n\
as the current node\n\
Then update temp. dist. L(V) for all node V in Q\n\
which are adjacent to current node, {minimun_temp_dist};")
    weight_to_update = []
    adjacent_vertex = []
    for q in Q:
        try :
            weight_to_update.append(W[minimun_temp_dist, q])
            adjacent_vertex.append(q)
        except Exception as e:
            continue
    print()
    for i in range(len(adjacent_vertex)):
        print(f"     L[{adjacent_vertex[i]}] = min(L[{adjacent_vertex[i]}], L[{minimun_temp_dist}]+W[{minimun_temp_dist},{adjacent_vertex[i]}])")
        print(f"     {L[adjacent_vertex[i]]} = min({L[adjacent_vertex[i]]}, {L[minimun_temp_dist]}+{weight_to_update[i]}]", end = '')
        if L[minimun_temp_dist]+weight_to_update[i]<L[adjacent_vertex[i]]:
            prev[adjacent_vertex[i]]=minimun_temp_dist
        L[adjacent_vertex[i]] = min(L[adjacent_vertex[i]], L[minimun_temp_dist]+weight_to_update[i])
        print(f" = {L[adjacent_vertex[i]]}; prev({adjacent_vertex[i]}) = {prev[adjacent_vertex[i]]}")
    
    print()
    print(f"     Consider node {minimun_temp_dist} as the discovered node\n\
and delete {minimun_temp_dist} out from set Q.\n\
Label L({minimun_temp_dist})={L[minimun_temp_dist]} as the permanent dist. of {minimun_temp_dist}")
    minimun_temp_dist = str(minimun_temp_dist)
    Q.remove(minimun_temp_dist)
    print(f"Q = {Q}")
    print()

    display_list = [['V'], 
                    ['L(V)'], 
                    ['prev(V)']]
    for vertex in sorted(L, key=L.get):
        display_list[0].append(vertex)
        display_list[1].append(L[vertex])
        display_list[2].append(prev[vertex])
    for row in display_list:
        fmt = "|{:<7}| |" + " |".join(["{:<5}|" for _ in row[1:]])
        print(fmt.format(*row))        
    
    if not Q:
        print(f"Stop when {terminal} is discovered")
        print(f"Length of the shortest path from {start} to {terminal} is {L[terminal]}")
        path = []
        temp_terminal = terminal
        while temp_terminal != start:
            path.append(prev[temp_terminal])
            temp_terminal = prev[temp_terminal]
        print(f"Where the path is ", end='')
        path.reverse()
        for node in path:
            print(f"{node}", end='-')
        print(f"{terminal}")

    elif minimun_temp_dist==terminal:
        Q.clear()
        print(f"Stop when {terminal} is discovered")
        print(f"Length of the shortest path from {start} to {terminal} is {L[terminal]}")
        path = []
        temp_terminal = terminal
        while temp_terminal != start:
            path.append(prev[temp_terminal])
            temp_terminal = prev[temp_terminal]
        print(f"Where the path is ", end='')
        path.reverse()
        for node in path:
            print(f"{node}", end='-')
        print(f"{terminal}")

def dijkstra_no_explain(L, prev, W, Q, start, terminal):
    minimun_temp_dist = sorted(L, key=L.get)[len(L)-len(Q)]
    weight_to_update = []
    adjacent_vertex = []
    for q in Q:
        try :
            weight_to_update.append(W[minimun_temp_dist, q])
            adjacent_vertex.append(q)
        except Exception as e:
            continue
    for i in range(len(adjacent_vertex)):
        if L[minimun_temp_dist]+weight_to_update[i]<L[adjacent_vertex[i]]:
            prev[adjacent_vertex[i]]=minimun_temp_dist
        L[adjacent_vertex[i]] = min(L[adjacent_vertex[i]], L[minimun_temp_dist]+weight_to_update[i])

    minimun_temp_dist = str(minimun_temp_dist)
    Q.remove(minimun_temp_dist)
      
    if not Q:
        display_list = [['V'], 
                    ['L(V)'], 
                    ['prev(V)']]
        for vertex in sorted(L, key=L.get):
            display_list[0].append(vertex)
            display_list[1].append(L[vertex])
            display_list[2].append(prev[vertex])
        for row in display_list:
            fmt = "|{:<7}| |" + " |".join(["{:<5}|" for _ in row[1:]])
            print(fmt.format(*row))  
        print(f"Stop when {terminal} is discovered")
        print(f"Length of the shortest path from {start} to {terminal} is {L[terminal]}")
        path = []
        temp_terminal = terminal
        while temp_terminal != start:
            path.append(prev[temp_terminal])
            temp_terminal = prev[temp_terminal]
        print(f"Where the path is ", end='')
        path.reverse()
        for node in path:
            print(f"{node}", end='-')
        print(f"{terminal}")

    elif minimun_temp_dist==terminal:
        display_list = [['V'], 
                    ['L(V)'], 
                    ['prev(V)']]
        for vertex in sorted(L, key=L.get):
            display_list[0].append(vertex)
            display_list[1].append(L[vertex])
            display_list[2].append(prev[vertex])
        for row in display_list:
            fmt = "|{:<7}| |" + " |".join(["{:<5}|" for _ in row[1:]])
            print(fmt.format(*row))  
        Q.clear()
        print(f"Stop when {terminal} is discovered")
        print(f"Length of the shortest path from {start} to {terminal} is {L[terminal]}")
        path = []
        temp_terminal = terminal
        while temp_terminal != start:
            path.append(prev[temp_terminal])
            temp_terminal = prev[temp_terminal]
        print(f"Where the path is ", end='')
        path.reverse()
        for node in path:
            print(f"{node}", end='-')
        print(f"{terminal}")
    
if __name__=="__main__":
    running = True
    while running:
        L = {}
        prev = {}
        W = {}
        Q = []
        i = 0
        print("--Welcome to Dijsktra's Algorithm Program--")
        vertex_name = input(f"Enter the vertex {i+1} name: ")
        prev[vertex_name] = '-'
        Q.append(vertex_name)
        L[vertex_name] = 1000
        while True:
            i+=1
            vertex_name = input(f"Enter the vertex {i+1} name (DONE=stop_input_vertex): ")
            if vertex_name.lower()=="done":
                break
            prev[vertex_name] = '-'
            Q.append(vertex_name)
            L[vertex_name] = 1000
        print(f"Q = {Q}")
        weight_check = []
        for start in Q:
            for terminal in Q:
                if start!=terminal and [terminal, start] not in weight_check:
                    weight = int(input(f"Enter the [{start}, {terminal}] weight: "))
                    weight_check.append([start, terminal])
                    if weight!=0:
                        W[start,terminal] = weight
                        W[terminal,start] = weight
        running_local = True
        Q2 = list(Q)
        running_option = True
        while running_local:
            while running_option:
                print("(1) Dijkstra's Algorithm with explain\n\
(2) Dijkstra's Algorithm with no explain")
                choice = int(input("Enter your chioce: "))
                start, terminal = input("Enter the shortest path from _ to _ | type x,x |: ").split(',')
                L[start] = 0
                match choice:
                    case 1:
                        while Q:
                            dijkstra_explain(L, prev, W, Q, start, terminal)
                        running_option = False
    
                    case 2:
                        while Q:
                            dijkstra_no_explain(L, prev, W, Q, start, terminal)
                        running_option = False
                        continue
                    case other:
                        print("Invalid Input!!")
                        continue
                    
            is_again = input("Do you wanna use again?: (Yes/No): ")
            if is_again.lower()=="yes":
                repeat_data = input("Do you want to use this data again (Yes/No): ")
                if repeat_data.lower()=="yes":
                    Q = Q2
                    running_option = True
                elif repeat_data.lower()=="no":
                    running_local = False
                else :
                    continue
            elif is_again.lower()=="no":
                running_local = False
                running = False
            else :
                continue
    print('--Bye Bye--')            