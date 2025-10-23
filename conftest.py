import pytest
from src.nodes import Node
from src.linked_lists import LinkedList


@pytest.fixture
def get_node() -> Node:
    return Node(0)


@pytest.fixture
def get_ll() -> LinkedList:
    return LinkedList(0)


@pytest.fixture
def get_ll3() -> LinkedList:
    ll = LinkedList(0)
    ll.append(1)
    ll.append(2)
    return ll
