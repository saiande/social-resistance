import math
import sys


def AdjacentInit(nodes, queries):
	global maxNodes 
	maxNodes = 20
	global maxQueries 
	maxQueries = 10
	global Adjacent 
	# ZERO OUT THE MAIN MATRIX
	Adjacent = [[0 for x in range(int(nodes) + int(queries))] for y in range(int(nodes) + 1)]
	# print(Adjacent)

	# SET THE LAST COEFFICIENT ROW TO ALL 1S
	for i in range(0, int(nodes)):
		Adjacent[int(nodes)][i] = 1.0
	# print(Adjacent)

	return 0
	

def scanEdgeData(nodes, edge):
	node = count = val = 0
	node = edge[0] 
	# print(node)
	count = edge[1] 
	# print(count)
	Adjacent[int(node)-1][int(node)-1] += float(count)
	# print(Adjacent)
	for i in range(2, int(count) + 2):
		val = edge[i]
		# print(val)
		Adjacent[int(node)-1][int(val)-1] = -1.0
		Adjacent[int(val)-1][int(node)-1] = -1.0
		Adjacent[int(val)-1][int(val)-1] += 1.0 

	# print(Adjacent)
	return count

def findMaxRow(nodes, queries, i):
	m = math.fabs(Adjacent[i][i])
	maxrow = i
	for j in range (int(i) + 1, int(nodes) + 1):
		tmp = math.fabs(Adjacent[j][i])
		if (tmp > m):
			m = tmp
			maxrow = j
	return maxrow

def swapRows(maxRow, i, nodes, queries):
	c = int(nodes) + int(queries)
	for j in range (0, int(c)):
		tmp = Adjacent[i][j]
		Adjacent[i][j] = Adjacent[maxRow][j]
		Adjacent[maxRow][j] = tmp

def eliminate(i, r, c):
	for j in range (0, r):
		if(j == i):
			continue
		factor = Adjacent[j][i]
		# print("factor: "+str(factor))
		for k in range (i, int(c)):
			# print("before: "+str(Adjacent[j][k]))
			Adjacent[j][k] -= factor*Adjacent[i][k]
			# print("after: "+str(Adjacent[j][k]))
		
	return 0


def solveMatrix(nodes, queries):
	c = int(nodes) + int(queries)
	r = int(nodes) + 1
	for i in range(0, int(nodes)):
		maxRow = findMaxRow(nodes, queries, i)
		if(maxRow != i):
			swapRows(maxRow, i, nodes, queries)
		# div currow by pivot
		pivot = Adjacent[i][i]
		pivot = 1.0 / pivot
		# print(Adjacent)
		for j in range (i, int(c)):
			Adjacent[i][j] *= pivot
		# now make Adjacent[i][currow] = 0 in all other rows
		# print(Adjacent)
		eliminate(i, r, c)
	

def main():
 		global query1
 		query1 = []
 		global query2
 		query2 = []
 		filename = sys.argv[-1]
 		with open(filename, 'r') as f:
 			probs = f.readline()
 			# print(probs)
 			for curProb in range (1, int(probs) + 1):
 				second = f.readline()
 				line = second.split()
 				# SETTING SECOND LINE TO RESPECTIVE VARIABLES
 				index = line[0]
 				# print("i: "+index)
 				nodes = line[1]
 				# print("n: "+nodes)
 				queries = line[2]
 				# print("q: "+queries)
 				edges = line[3]
 				# print("e: "+edges)

 				# INITIALIZING MATRIX
 				AdjacentInit(nodes, queries)

 				# READ EDGE DATA
 				edgecnt = edgelines = 0
 				while (edgecnt < int(edges)):
 					e = f.readline()
 					edge = e.split()
 					# print(edge)
 					i = scanEdgeData(nodes, edge)
 					edgelines += 1
 					edgecnt += int(i)
 				for j in range (0, int(queries)):
 					q = f.readline()
 					query = q.split()
 					# print(query)
 					for a in range(0, int(queries)):
 						query1.append(0)
 						query2.append(0)
 					queryno = query[0]
 					query1[j] = query[1]
 					query2[j] = query[2]
 					Adjacent[int(query1[j]) - 1][int(nodes) + j] = 1.0
 					Adjacent[int(query2[j]) - 1][int(nodes) + j] = -1.0

 				# print(query1)
 				# print(query2)
 				# print(Adjacent)
 				x = solveMatrix(nodes, queries)

 				print(curProb, end=" ")
 				for a in range (0, int(queries)):
 					dist = math.fabs(Adjacent[int(query1[int(a)]) - 1][int(nodes) + int(a)] - Adjacent[int(query2[int(a)]) - 1][int(nodes) + int(a)])
 					print("%.3f" % dist, end=" ")
 				print()
 				
				
 	
if __name__ == "__main__":
    main()