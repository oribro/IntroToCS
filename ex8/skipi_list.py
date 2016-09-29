from sllist import SkipiNode as Node


class SkipiList:

    """
    This class represents a special kind of a doubly-linked list
    called a SkipiList. A SkipiList is composed of Nodes (SkipiNode from
    sllist).cIn addition to the data, each Node has one pointer to the
    next Node in the list, and another pointer to the prev-prev Node in the
    list (hence the name "skipi"). The only data members the class contains
    are the head and the tail of the list.
    """

    def __init__(self):
        """Constructs an empty SkipiList."""
        self.head = None
        self.tail = None
            
    def add_first(self, data):
        """
        Adds an item to the beginning of a list.
        data - the item to add
        """
        # The new node to add to the start of the list.
        new_item = Node(data, self.head, None)
        # Empty list - now it has one node.
        if self.head is None:
            self.head = new_item
            self.tail = new_item
        # Use the skip_back to get to the new node. 
        elif self.head.next is not None:
            self.head.next.skip_back = new_item
        self.head = new_item
            
        

    def remove_first(self):
        """
        Removes the first Node from the list and return its data.
        Returns that data of the removed node
        """
        # Keep the node we want to remove in order to return the data.
        node_to_remove = self.head
        # Empty list.
        if self.head is None:
            return None
        # Handle special cases.
        elif self.head.next.next is None:
            self.head = self.head.next
        elif self.head.next is None:
            self.head = None
            self.tail = None
        # Remove the node and update the list.
        else:
            self.head = self.head.next
            self.head.next.skip_back = None
        return node_to_remove.data

    def add_last(self, data):
        """
        Adds an item to the end of a list.
        data - the item to add
        """
        # Pointer to the nodes of the list.
        pointer = self.head
        # Empty list - now it has one node.
        if self.head is None:
            self.head = Node(data, None)
            self.tail = self.head
        # One node - now the list has two.
        elif self.head.next is None:
            self.head.next = Node(data, None)
            self.tail = self.head.next
        # Go to the last node and add a new node there.
        else:
            while pointer.next.next is not None:
                pointer = pointer.next
            self.tail.next = Node(data, None)
            self.tail = self.tail.next
            self.tail.skip_back = pointer

            
    def remove_last(self):
        """
        Removes the last Node from the list and return its data.
        The data of the removed node
        """
        # Empty list.
        if self.tail is None:
            return None
        # Keep the data of the last node before removing it.
        last_node_data = self.tail.data
        # One node in the list - now there are none.
        if self.tail == self.head:
            self.head = None
            self.tail = None
        # Two nodes in the list - now there is one.
        elif self.head.next == self.tail:
            self.tail = self.head
            self.head.next = None
        # Remove the last node of the list for a longer list.
        else:
            self.tail = self.tail.skip_back.next
            self.tail.next.skip_back = None
            self.tail.next = None
        return last_node_data

    def remove_node(self, node):
        """
        Removes a given Node from the list, and returns its data.
        Assumes the given node is in the list. Runs in O(1).
        """
        # Keep the data of the removed node.
        removed_data = node.data
        if self.head is None:
            return None
        # Use the functions we implemented to remove the first or last
        # node of the list, in case 'node' parameter is indeed one of
        # the two.
        elif node == self.tail:
            self.remove_last()
        elif node == self.head:
            self.remove_first()
        # The wanted node is somewhere between the head and the tail.
        else:
            # Pointers that help in removing the specific node from
            # the list.
            temp_head = node.next
            temp_tail = node.next.skip_back
            temp_head.next.skip_back = temp_tail
            temp_head.skip_back = temp_tail.next.skip_back
            temp_tail.next = temp_head
            node.next = None
            node.skip_back = None    
        return removed_data

    def __getitem__(self, k):
        """
        Returns the data of the k'th item of the list.
        If k is negative return the data of k'th item from the end of the list.
        If abs(k) > length of list raise IndexError.
        """
        # The length of the list.
        list_length = 0
        # Pointer to the nodes of the list.
        pointer = self.head
        # Variable that assists in going over the nodes
        # until the k'th item has been reached.
        counter = 0

        # Calculate the length of the list.
        while pointer is not None:
            pointer = pointer.next
            list_length += 1
        pointer = self.head

        # The item is not in the list.
        if (k>0 and list_length <= k) or \
           (k<0 and list_length <= k*(-1)) :
            raise IndexError
        # The item is in the list.
        elif k > 0:
            # Get to the item.
            while counter < k:
                pointer = pointer.next
                counter += 1
        # The item is reached from the end of the list.
        elif k < 0:
            while counter < (list_length+k):
                pointer = pointer.next
                counter += 1
        return pointer.data
