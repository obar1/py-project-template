"""
This module provides a basic implementation of Nodes
"""

from __future__ import annotations
from typing import Any, Optional


class Node:
    """Node with next, ll"""

    def __init__(self, value: Any) -> None:
        self.value = value
        self.next: Optional[Node] = None

    def __str__(self) -> str:
        return f"node:{self.value}"


class NodeP:
    """Node with next and prev, dll"""

    def __init__(self, value: Any) -> None:
        self.value = value
        self.next: Optional[NodeP] = None
        self.prev: Optional[NodeP] = None

    def __str__(self) -> str:
        return f"node:{self.value}"


class NodeLR:
    """Node with left and right, graph"""

    def __init__(self, value: Any) -> None:
        self.value = value
        self.left: Optional[NodeLR] = None
        self.right: Optional[NodeLR] = None

    def __str__(self) -> str:
        return f"node:{self.value}"
