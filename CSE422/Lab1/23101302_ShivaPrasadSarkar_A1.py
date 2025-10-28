import heapq
import numpy

#task 1
def task1():

  fileinput = open("C:\\Users\\user\\Documents\\Summer 25\\Cse 422\\Lab\\Lab1\\open.txt",'r')
  row,col =  tuple(map(int,fileinput.readline().split()))
  sr,sc = tuple(map(int,fileinput.readline().split()))
  er,ec = tuple(map(int,fileinput.readline().split()))

  matrix = numpy.zeros((row,col),dtype = str)

  for i in range(row):
    b = fileinput.readline()
    for j in range(col):
      matrix[i][j] = b[j]

  def heuristic(r,c):
      global er,ec
      return abs(r-er)+abs(c-ec)

  priorityq = []

  node  =  matrix[sr][sc]
  cost_total = 0 + heuristic(sr,sc)
  parent = {str(sr)+str(sc):(str(sr)+str(sc),0)}
  heapq.heappush(priorityq,(cost_total,sr,sc,''))

  visited = []

  path =''

  while True:


    if len(priorityq)==0:
      break

    cost,r,c,d = heapq.heappop(priorityq)
    visited.append(str(r)+str(c))

    if r==er and c==ec:
      print(len(d))
      print(d)
      return


    else:
      k = str(r+1)+str(c)
      if matrix[r+1][c]!='#' and r+1<row and k not in visited:
        cost = parent[str(r)+str(c)][1]+1
        parent[str(r+1)+str(c)]=(str(r)+str(c),cost)
        cost_t = cost+heuristic(r+1,c)
        heapq.heappush(priorityq,(cost_t,r+1,c,d+"D"))

      k = str(r-1)+str(c)
      if matrix[r-1][c]!='#' and r-1>=0 and k not in visited:
        cost = parent[str(r)+str(c)][1]+1
        parent[str(r-1)+str(c)]=(str(r)+str(c),cost)
        cost_t = cost+heuristic(r-1,c)
        heapq.heappush(priorityq,(cost_t,r-1,c,d+"U"))


      k = k = str(r)+str(c+1)
      if matrix[r][c+1]!='#' and c+1<col and k not in visited:
        cost = parent[str(r)+str(c)][1]+1
        parent[str(r)+str(c+1)]=(str(r)+str(c),cost)
        cost_t = cost+heuristic(r,c+1)
        heapq.heappush(priorityq,(cost_t,r,c+1,d+"R"))

      k = str(r)+str(c-1)
      if matrix[r][c-1]!='#' and c-1>=0 and k not in visited:
        cost = parent[str(r)+str(c)][1]+1
        parent[str(r)+str(c-1)]=(str(r)+str(c),cost)
        cost_t = cost+heuristic(r,c-1)
        heapq.heappush(priorityq,(cost_t,r,c-1,d+"L"))

  print(-1)
  return




if __name__=="__main__":
  task1()

#task 2
def task2():
  fileinput = open("C:\\Users\\user\\Documents\\Summer 25\\Cse 422\\Lab\\Lab1\\open.txt",'r')
  n, m = tuple(map(int,fileinput.readline().split()))

  x = fileinput.readline()

  start,end =  tuple(map(int,fileinput.readline().split()))

  x = fileinput.readline()

  heuris = {}
  for i in range(n):
    node,h = tuple(map(int,fileinput.readline().split()))
    heuris[node]=h

  x = fileinput.readline()

  graph = {i+1:[] for i in range(n)}
  for j in range(m):
    a,b = tuple(map(int,fileinput.readline().split()))
    graph[a].append(b)
    graph[b].append(a)


  def pathscaler(graph,g):
    queue = [g]
    color = {i:0 for i in graph}
    queue.append(g)
    dis = {i:float('inf') for i in graph}
    dis[g]=0

    while queue!=[]:
      p = queue.pop(0)

      for i in graph[p]:
        if color[i]==0:
          color[i]=1
          dis[i]=dis[p]+1
          queue.append(i)

      color[p]=2

    return dis




  dis = pathscaler(graph,end)

  inadmissible = []
  for i in heuris:
    if heuris[i]>dis[i]:
      inadmissible.append(i)

  if inadmissible==[] :
    print(1)
  else :
    print(0)
    if len(inadmissible)==1:
      print(f"Here node{inadmissible[0]} is inadmissible.")
    else:
      print(f"Here nodes {', '.join(map(str,inadmissible[:len(inadmissible)-1]))} and {inadmissible[-1]} are inadmissible.")


if __name__=="__main__":
  task2()