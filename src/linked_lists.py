"""
This module provides a basic implementation of a singly linked list data structure
"""

from __future__ import annotations
from typing import Any, Generator, Optional

from src.a_ds import ADS
from src.nodes import Node


class LinkedList(ADS):
    """
    A singly linked list data structure.

    Attributes:
        head (Node): The first node in the list.
        tail (Node): The last node in the list.
        length (int): The number of nodes in the list.
    """

    @property
    def get_id(self) -> str:
        """
        Returns the identifier for this data structure.

        Returns:
            str: The string "linked-list".
        """
        return "linked-list"

    def __init__(self, value: Any) -> None:
        """
        Initializes a new LinkedList with a single node containing the given value.

        Args:
            value: The value to be stored in the initial node.
        """
        new_node = Node(value)
        self.head: Optional[Node] = new_node
        self.tail: Optional[Node] = new_node
        self.length: int = 1

    def print_list(self) -> Generator[str, None, None]:
        """
        Generates a string representation of each node in the list for printing.

        Yields:
            str: String representation of each node followed by a comma.
        """
        temp = self.head
        while temp is not None:
            yield str(temp) + ","
            temp = temp.next

    def __repr__(self) -> str:
        """
        Returns a string representation of the linked list.

        Returns:
            str: A string in the format "ll:[node1, node2, ...]".
        """
        return f"ll:{list(self.print_list())}"

    def append(self, value: Any) -> bool:
        """
        Appends a new node with the given value to the end of the list.

        Args:
            value: The value to be stored in the new node.

        Returns:
            bool: Always returns True.
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            if self.tail:
                self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self) -> Optional[Node]:
        """
        Removes and returns the last node from the list.

        Returns:
            Node: The removed node, or None if the list is empty.
        """
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp and temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        if self.tail:
            self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value: Any) -> bool:
        """
        Prepends a new node with the given value to the beginning of the list.

        Args:
            value: The value to be stored in the new node.

        Returns:
            bool: Always returns True.
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def get(self, index: int) -> Optional[Node]:
        """
        Retrieves the node at the specified index.

        Args:
            index (int): The index of the node to retrieve.

        Returns:
            Node: The node at the given index, or None if the index is out of bounds.
        """
        try:
            assert 0 <= index <= self.length - 1
            tmp = self.head
            for _ in range(index):
                if tmp:
                    tmp = tmp.next
            return tmp
        except AssertionError:
            return None

    def set_value(self, index: int, value: Any) -> bool:
        """
        Sets the value of the node at the specified index.

        Args:
            index (int): The index of the node to update.
            value: The new value to set.

        Returns:
            bool: True if the value was set successfully, False if the index is invalid.
        """
        try:
            tmp = self.get(index)
            if tmp:
                tmp.value = value
                return True
        except KeyError:
            return False
        return False

    def pop_first(self) -> Optional[Node]:
        """
        Removes and returns the first node from the list.

        Returns:
            Node: The removed node, or None if the list is empty.
        """
        if self.length == 0:
            return None
        temp = self.head
        if self.head:
            self.head = self.head.next
        if temp:
            temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def remove(self, index: int) -> Optional[Node]:
        """
        Removes and returns the node at the specified index.

        Args:
            index (int): The index of the node to remove.

        Returns:
            Node: The removed node, or None if the index is invalid.
        """
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        if pre:
            temp = pre.next
            if temp:
                pre.next = temp.next
                temp.next = None
            self.length -= 1
            return temp
        return None

    def reverse(self) -> LinkedList:
        """
        Creates a new reversed copy of the linked list.

        Returns:
            LinkedList: A new LinkedList instance with the nodes in reverse order.
        """
        new_list = LinkedList(None)
        new_list.remove(0)

        current = self.head

        while current:
            new_list.prepend(current.value)
            current = current.next
        return new_list
