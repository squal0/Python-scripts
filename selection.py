def selection_sort(items):
    """Sorts the list of items into ascending order using the selection
    sort algorithm"""

    for step in range(len(items)):
        #Find the location of the smallest element
        #items[step:]
        location_of_smallest = step
        for location in range(step, len(items)):
            #determine the location of the smallest
            if items[location] < items[location_of_smallest]:
                location_of_smallest = location
        #Exchange items[step] with items[location_of_smallest]
        temporary_item = items[step]
        items[step] = items[location_of_smallest]
        items[location_of_smallest] = temporary_item
    return items
