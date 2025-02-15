def get_partitions(items, value, visited=None, partition=None, partitions=None):
    if visited is None:    
        visited = set()  # Use a set for faster lookups
        partitions = []
        partition = []
    
    if sum(partition) == value:
        partitions.append(partition.copy())
        return partitions
    
    for i in range(len(items)):
        element = items[i]
        if element not in visited:
            if sum(partition) + element <= value:
                visited.add(element)
                partition.append(element)
                
                get_partitions(items[i+1:], value, visited, partition, partitions)
                
            
                partition.pop()
                visited.remove(element)
    return partitions

items = [1,2,3,4,5]
print(get_partitions(items, 5))
