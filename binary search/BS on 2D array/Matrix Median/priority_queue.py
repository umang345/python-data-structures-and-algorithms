import heapq

class PQEntity:
    def __init__(self, num, rowIndex, colIndex):
        self.num = num 
        self.rowIndex = rowIndex
        self.colIndex = colIndex

def priority_func(entity):
    return (entity.num, entity.rowIndex, entity.colIndex)

def getMedian(matrix):
    rows, cols = len(matrix), len(matrix[0])

    pq=[]
    for row in range(rows):
        entity = PQEntity(matrix[row][0], row, 0)
        heapq.heappush(pq, (priority_func(entity), entity))

    medianIndex = ((rows*cols)//2)
    if (rows*cols %2 == 0):
        medianIndex-=1

    while medianIndex>0:
        entity = heapq.heappop(pq)
        num = entity[1].num 
        rowIndex = entity[1].rowIndex
        colIndex = entity[1].colIndex

        if colIndex+1<cols:
            colIndex+=1
            newEntity = PQEntity(matrix[rowIndex][colIndex], rowIndex, colIndex)
            heapq.heappush(pq,(priority_func(newEntity), newEntity))
        
        medianIndex-=1
    
    resultEntity = heapq.heappop(pq)
    return resultEntity[1].num

    
