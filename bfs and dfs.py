#dfs algo

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
visit =  set() # to store visit node
def dfs(visit,graph,node):
	if node not in visit:
		print(node)
		visit.add(node)
		for neighbour in graph[node]:
			dfs(visit,graph,neighbour)
	
print("dfs is:")
dfs(visit,graph,'5')

#bfs algo
visit =[]
queue=[]

def bfs(visit,graph,node):
	visit.append(node)
	queue.append(node)
	
	while queue:
		m=queue.pop(0)
		print(m,end=" ")
		
		for neighbour in graph[m]:
			if neighbour not in visit:
				visit.append(neighbour)
				queue.append(neighbour)
		
print("bfs is:")
bfs(visit,graph,'5')
				