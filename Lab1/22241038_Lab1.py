import heapq

file1 = open("F://Summer 23/CSE422/Labs/Lab1/Input file.txt", mode='r')
lines = file1.readlines()

heuristics = {}
graph = {}

city = {'Arad': 'A', 'Neamt' :'F', 'Bucharest': 'Z', 'Oradea' :'B', 'Craiova' : 'S', 'Pitesti' :'P', 'Eforie': 'T', 'RimnicuVilcea': 'R', 'Fagaras': 'O', 'Timisoara': 'C', 'Dobreta': 'V', 'Urziceni': 'D', 'Hirsova' : 'N','Vaslui' : 'H', 'lasi': 'Q', 'Zerind' : 'E', 'Lugoj': 'G', 'Mehadia': 'L', 'Giurgiu': 'X', 'Sibiu': 'Y'}

start = input('Source: ').strip().capitalize()
dest = input('Destination: ').strip().capitalize()
source = city[start]
dest = city[dest]


for i in lines:
    x = i.strip()
    list1 = x.split()
    head = list1[0] 
    hval = int(list1[1])
    nodeSymbol = city[head]
    heuristics[nodeSymbol] = hval 
    list1.pop(0)
    list1.pop(0)

    loop = len(list1) // 2
    for j in range(loop):
        c1 = []
        cost = int(list1[1])
        vertex = list1[0]
        vertexSymbol = city[vertex]
        c1 += [cost, vertexSymbol]  
        if nodeSymbol in graph.keys(): 
            graph[nodeSymbol].append(c1)
        else:
            graph[nodeSymbol] = [c1]
        list1.pop(0)
        list1.pop(0)   

queue = []
goal = {} 
allBranches = {} 

def search(G, src):
    queue = [[0, src]]
    while queue:
        m = heapq.heappop(queue)
        branch = m[1] 
        branching = ''     
        for cost, neighbour in graph.get(branch[-1]):      
            if neighbour not in branch:   
                branching = branch
                branching += neighbour
                if branch in allBranches.keys():
                    allBranches[branching] = allBranches[branch] + cost   
                else:
                    allBranches[branching] = cost
                pathcost = allBranches[branching]
                Heuristic = heuristics[neighbour]
                total = pathcost + Heuristic
                if neighbour == dest:
                    goal[branching] = total
                else:
                    heapq.heappush(queue, [total, branching])
                    heapq.heapify(queue) 

search(graph, source)

path = []
if bool(goal) == True:
    result = min(goal.values()) 
    goalPath = []
    for k, v in goal.items():
        if v == result:
            goalPath.append(k)  

    notations1 = {}
    for k,v in city.items():
        notations1[v] = k

    for i in goalPath:
        string = ''
        for j in i:
            if j in notations1.keys():
                string += notations1[j]
                string += '->'
        string = string[:-2] + '\n'
        string += f'Optimum distance: {result} km\n'
        path.append(string)
else:
    p1 = f'NO PATH FOUND'
    path.append(p1)

for i in path:
    print(i)