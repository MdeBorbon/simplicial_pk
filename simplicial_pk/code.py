
def intersection_poset(n, sequence):
    """
    Returns the points of intersection of the line arrangement with Grunbaum key k from its wiring diagram.
    The output is a pair of lists (double_points, multiple_points) whose elements are tuples of numbers.
    The numbers are the labels of the lines that go through the point.
    """

    # Number of lines of the arrangement
    #n = k[0]
    # wiring diagram
    #sequence = db_wd[k]

    current_order = [i for i in range(1,n+1)]
    vertex_points = []

    for crossing in sequence:
        start_pos, end_pos = crossing

        # 1. Identify which lines are involved based on current order
        # (start_pos, end_pos) refers to the lines currently in those positions.
        involved_lines = []
        for i in range(start_pos - 1, end_pos):
            involved_lines.append(current_order[i])

        # Store this point
        vertex_points.append(tuple(sorted(involved_lines)))

        # 2. Update the order (permutation) for the next step
        # The lines involved in the crossing reverse their relative order
        involved_lines_reversed = involved_lines[::-1]
        current_order[start_pos-1:end_pos] = involved_lines_reversed

    double_points = [p for p in vertex_points if len(p)==2]
    multiple_points = [p for p in vertex_points if len(p)>2]

    return double_points, multiple_points
