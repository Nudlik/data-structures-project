"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import pytest

from src.linked_list import LinkedList


@pytest.fixture
def test_fixture_linkedlist():
    ll = LinkedList()
    ll.insert_beginning({'id': 1})
    ll.insert_at_end({'id': 2})
    ll.insert_at_end({'id': 3})
    return ll


def test_linkedlist_representation(test_fixture_linkedlist):
    assert str(LinkedList()) == 'None'
    assert str(test_fixture_linkedlist) == "{'id': 1} -> {'id': 2} -> {'id': 3} -> None"


def test_linkedlist_inserts():
    ll = LinkedList()
    ll.insert_beginning({'id': 1})
    ll.insert_at_end({'id': 2})
    ll.insert_at_end({'id': 3})
    ll.insert_beginning({'id': 0})
    assert ll.head.data == {'id': 0}
    assert ll.head.next_node.data == {'id': 1}
    assert ll.head.next_node.next_node.data == {'id': 2}
    assert ll.head.next_node.next_node.next_node.data == {'id': 3}


def test_linkedlist_none():
    ll = LinkedList()
    ll.insert_at_end({'id': 2})
    assert ll.head.data == {'id': 2}


