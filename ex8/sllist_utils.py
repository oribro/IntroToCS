from sllist import List, Node


def merge_lists(first_list, second_list):
    """
    Merges two sorted (in ascending order) lists into one new sorted list in
    an ascending order. The resulting new list is created using new nodes
    (copies of the nodes of the given lists). Assumes both lists are sorted in
    ascending order. The original lists should not be modified.
    """
    # Checking for empty lists.
    if first_list.head is None and second_list.head is None:
        return []
    # Create a new head for the new list.
    initial_head = Node(None, None)
    # Pointer to the nodes of the new list.
    new_list_pointer = initial_head
    # Pointer to the nodes of the first list.
    first_list_pointer = first_list.head
    # Pointer to the nodes of the second list.
    second_list_pointer = second_list.head
    # Go over the nodes of both lists.
    while first_list_pointer is not None and \
          second_list_pointer is not None:
        # Merge the nodes of the first list into the new list.
        if first_list_pointer.get_data() <= \
           second_list_pointer.get_data():
            # Create a new node for the new list: an instance of the
            # class 'Node'. The data is a copy of first_list's node data.
            new_list_pointer.set_next(Node(first_list_pointer\
                                           .get_data(), None))
            new_list_pointer = new_list_pointer.get_next()
            first_list_pointer = first_list_pointer.get_next()
        # Merge the nodes of the second list into the new list.
        else:
            # Create a new node for the new list: an instance of the
            # class 'Node'. The data is a copy of second_list's node data.
            new_list_pointer.set_next(Node(second_list_pointer\
                                           .get_data(), None))
            new_list_pointer = new_list_pointer.get_next()
            second_list_pointer = second_list_pointer.get_next()
    # The second list is longer than the first: Merge the extra nodes
    # into the new list.
    if first_list_pointer is None:
        while second_list_pointer is not None:
            new_list_pointer.set_next(Node(second_list_pointer\
                                           .get_data(), None))
            new_list_pointer = new_list_pointer.get_next()
            second_list_pointer = second_list_pointer.get_next()
    # The first list is longer than the second: Merge the extra nodes
    # into the new list.
    elif second_list_pointer is None:
        while first_list_pointer is not None:
            new_list_pointer.set_next(Node(first_list_pointer\
                                           .get_data(), None))
            new_list_pointer = new_list_pointer.get_next()
            first_list_pointer = first_list_pointer.get_next()
    # Create a new list: an instance of the class 'List'.
    new_list = List()
    # Determine the head of the new list as the first node that was
    # created and linked to the initial head.
    new_list.head = initial_head.get_next()
    return new_list
            
    


def contains_cycle(sll):
    """
    Checks if the given list contains a cycle.
    A list contains a cycle if at some point a Node in the list points to
    a Node that already appeared in the list. Note that the cycle does not
    necessarily contain all the nodes in the list. The original list should
    not be modified.
    Returns true iff the list contains a cycle
    """
    # using "Tortoise and hare" algorithm:
    # http://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare
    if sll.head is None:
        return False
    # A "fast" pointer that advances 2 nodes each time.
    faster_pointer = sll.head
    # A "slow" pointer that advances a node each time.
    slower_pointer = sll.head
    while True:
        # The faster pointer has reached the end of the list, means
        # the list has no cycle.
        if faster_pointer is None or faster_pointer.get_next() is None:
            return False
        faster_pointer = faster_pointer.get_next().get_next()
        slower_pointer = slower_pointer.get_next()
        # The faster pointer has reached the position of the slower
        # one (the hare beat the tortoise) => the list does not end
        # and it contains a cycle.
        if faster_pointer == slower_pointer:
            return True
        


def reverse(sll):
    """
    Reverses the given list (so the head becomes the last element, and every
    element points to the element that was previously before it). Runs in O(n).
    No new object is created.
    """
    # Checking for legal list
    if sll.head is None:
        return None
    # Pointer to the node we would like to point to in order
    # to reverse the current link. Points to the first node in
    # the original list which will be the last node in the reversed one.
    previous_pointer = sll.head
    # Pointer to the node we establish the link from. The current
    # node we work with.
    current_pointer = sll.head.get_next()
    # Make the first node of the list the last one (head points to none) 
    sll.head.set_next(None)
    # Go over the nodes of the list.
    while current_pointer is not None:
        # Pointer to the next node in the list.
        next_pointer = current_pointer.get_next()
        # Link the current node to the previous node.
        current_pointer.set_next(previous_pointer)
        # Advance to the next Link in the list to be reversed.
        previous_pointer = current_pointer
        current_pointer = next_pointer
    # The head of the list is now the last node of the original list.
    sll.head = previous_pointer
            
def find_middle(sll):
    """ Given a list of nodes, this function finds the middle node
    of the list. If the list is of even length, returns the node
    in length//2. Returns the middle node of the list.
    The implementation resembles the "Tortoise and hare"
    algorithm, only that we assume the list does not contain a cycle."""

    # Checking for legal list.
    if sll.head is None:
        return False
    # A "fast" pointer that advances 2 nodes each time
    faster_pointer = sll.head
    # A "slow" pointer that advances a node each time.
    slower_pointer = sll.head
    # Go over the list of nodes.
    while faster_pointer.get_next() is not None and \
          faster_pointer.get_next().get_next() is not None:
        faster_pointer = faster_pointer.get_next().get_next()
        slower_pointer = slower_pointer.get_next()
    # By the time the fast pointer has reached the end of the list,
    # the slow one has reached the middle, that is since the ratio
    # between the pointers' advancement is 2:1.
    return slower_pointer


def is_palindrome(sll):
    """
    Checks if the given list is a palindrome. A list is a palindrome if
    for j=0...n/2 (where n is the number of elements in the list) the
    element in location j equals to the element in location n-j.
    Note that you should compare the data stored in the nodes and
    not the node objects themselves. The original list should not be modified.
    Returns true iff the list is a palindrome
    """
    # The implementation includes finding the middle of the list,
    # reversing the list of nodes starting at [middle+1],
    # Checking each parallel nodes in both list halves and finally
    # reversing the list and returning it to it's original state
    # as we were asked not to modify the original list.
    
    # Checking for legal list.
    if sll.head is None:
        return True
    # Pointer to the nodes in the left half of the list.
    left_half_pointer = sll.head
    # Pointer for keeping the original head of the list.
    list_head = left_half_pointer
    # Pointer to the middle node of the list. I use the external
    # function 'find_middle(sll)' to determine the middle node.
    # (if the list is of even length, returns the node in length//2).
    middle_pointer = find_middle(sll)
    # The head of the list is now the node in [middle+1] so that
    # we can reverse the list from that point on.
    sll.head = middle_pointer.get_next()
    # Disconnect the middle from the right half of the list.
    middle_pointer.set_next(None)
    # Reverse the right half of the list
    reverse(sll)
    # Pointer to the nodes in the right half of the list - now reversed.
    right_half_pointer = sll.head
    # Both halves are of the same length - go over them.
    while right_half_pointer is not None:
        # The data stored in the node and in its parallel are different.
        # That means: the list cannot be a palindrome by definition.
        if right_half_pointer.get_data() != \
           left_half_pointer.get_data():
            # Reverse again to return it to it's original state.
            reverse(sll)
            # Connect the middle to the right half of the list.
            middle_pointer.set_next(sll.head)
            # Determine the head of the list as the original head.
            sll.head = list_head
            return False
        right_half_pointer = right_half_pointer.get_next()
        left_half_pointer = left_half_pointer.get_next()
    # All nodes are identical to their parallels => it's a palindrome.
    # Returning the list to it's original state like we did in 'false'.
    reverse(sll)
    middle_pointer.set_next(sll.head)
    sll.head = list_head
    return True
    
    
        
    
    


def have_intersection(first_list, second_list):
    """
    Checks if the two given lists intersect.
    Two lists intersect if at some point they start to share nodes.
    Once two lists intersect they become one list from that point on and
    can no longer split apart. Assumes that both lists does not contain cycles.
    Note that two lists might intersect even if their lengths are not equal.
    No new object is created, and niether list is modified.
    Returns true iff the lists intersect.
    """
    # Checking for legal lists.
    if first_list.head is None or second_list.head is None:
        return False
    # Pointer to a node of the first list.
    pointer_one = first_list.head
    # Pointer to a node of the second list.
    pointer_two = second_list.head
    # Go over the first list.
    while pointer_one.get_next() is not None:
        pointer_one = pointer_one.get_next()
    # Go over the second list.
    while pointer_two.get_next() is not None:
        pointer_two = pointer_two.get_next()
    # The last node is common to both lists. It means that in one point,
    # The lists stopped being different and intersected.
    if pointer_one == pointer_two:
        return True
    # The last node is different in each list => they have not intersected.
    else:
        return False


def get_item(sll, k):
    """
    Returns the k'th element from of the list.
    If k > list_size returns None, if k<0 returns the k element from the end.
    """
    # Checking for legal list.
    if sll.head is None:
        return None
    # The index of the list (the current node).
    index = 0
    # Pointer to a node of the list.
    pointer = sll.head
    # Pointer to the node we seek.
    kth_element = sll.head
    # Seperating between positive and negative 'k' cases.
    if k >= 0:
        # Go over the list's nodes
        while pointer is not None:
            # The wanted element is found. Point to it for later return.
            if index == k:
                kth_element = pointer
            pointer = pointer.get_next()
            # Advance to the next element in the list.
            index += 1
        # The wanted element is not in the list.
        if k > index-1:
            return None
        return kth_element.get_data()
    
    if k < 0:
        # Count the length of the list.
        while pointer is not None:
            pointer = pointer.get_next()
            index += 1
        # Negative index means we check items from the end.
        index = index * (-1)
        # The wanted element is not in the list.
        if k < index:
            return None
        pointer = sll.head
        # Go over the list's nodes
        while pointer is not None:
            if index == k:
                kth_element = pointer
            pointer = pointer.get_next()
            index += 1
        return kth_element.get_data()
             
        
    


def slice(*args):
    """ Returns a new list after slicing the given list from start to stop
    with a step.
    Imitates the behavior of slicing regular sequences in python.
    slice(sll, [start], stop, [step]):
    With 4 arguments, behaves the same as using list[start:stop:step],
    With 3 arguments, behaves the same as using list[start:stop],
    With 2 arguments, behaves the same as using list[:stop],
    """
    return List()


def merge_sort(sll):
    """
    Sorts the given list using the merge-sort algorithm.
    Resulting list should be sorted in ascending order. Resulting list should
    contain the same node objects it did originally, and should be stable,
    i.e., nodes with equal data should be in the same order they were in in the
    original list. You may create a constant number of new to help sorting.
    """
    def recursive_merge_sort(sll):
        """ Recursive function using the algorithm we learned in class
        in order to 'divide and conquer' the list. Returns a list
        that is sorted in ascending order according to the merge-sort
        algorithm."""
        # List to help sorting the original list.
        sll_helper = List()
        # The legnth of the original list.
        sll_length = 0
        # Pointer to the nodes of the list.
        pointer = sll.head
        # Calculate the length of the list.
        while pointer is not None:
            pointer = pointer.get_next()
            sll_length += 1
        # Base condition. We stop when we divided utmost.
        if sll_length < 2:
            return (sll)
        # Using the external function to get the middle node.
        sll_middle = find_middle(sll)
        # Create a "sub-list" for the right half to ease the sorting.
        sll_helper.head = sll_middle.next
        sll_middle.next = None
        # Go over the left half of the list.
        left_half = recursive_merge_sort(sll)
        # Go over the right half of the list.
        right_half = recursive_merge_sort(sll_helper)

        # Principal similar to merge_lists: sort the half that has
        # lesser values first.
        if left_half.head.data <= right_half.head.data:
            # The half we check.
            current_half = left_half.head
            # The first node of that part of the list we sort.
            first_node = left_half.head.next
            # The second node of that part of the list we sort.
            second_node = right_half.head
            # The sorted part of the list to be returned.
            sorted_list = left_half
        else:
            current_half = right_half.head
            first_node = left_half.head
            second_node = right_half.head.next
            sorted_list = right_half
        
        while (first_node is not None) or (second_node is not None):
            # Merge the second node the we check into the list.
            if(first_node is None):
                current_half.next = second_node
                current_half  = second_node
                second_node = second_node.next
            # Merge the first node that we check into the list.
            elif(second_node is None):
                current_half.next = first_node
                current_half = first_node
                first_node = first_node.next
            # Merge and sort in ascending order.
            elif(first_node.data <= second_node.data):
                current_half.next = first_node
                current_half = first_node
                first_node = first_node.next
            elif(second_node.data < first_node.data):
                current_half.next = second_node
                current_half = second_node
                second_node = second_node.next
        return  sorted_list
    sll.head = recursive_merge_sort(sll).head
