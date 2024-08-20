# solution.py 

def count_increases(depths: List[int]) -> int:
    current_depth = depths[0]
    increase_counter: int = 0
    for depth in depths[1:]:
        if depth > current_depth:
            increase_counter += 1
        current_depth = depth
    return increase_counter

cpdef int count_increases_cy(list depths):
    cdef int increase_counter, current_depth, depth
    current_depth = depths[0]
    increase_counter = 0
    for depth in depths[1:]:
        if depth > current_depth:
            increase_counter += 1
        current_depth = depth
    return increase_counter

cpdef int count_increases_cy_array(long[:] depths):
    cdef int increase_counter, current_depth, depth, length, i
    length = depths.shape[0]
    current_depth = depths[0]
    increase_counter = 0
    for i in range(1, length):
        if depths[i] > current_depth:
            increase_counter += 1
        current_depth = depths[i]
    return increase_counter