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


def test_linkedlist_get_by_id(test_fixture_linkedlist):
    assert test_fixture_linkedlist.get_data_by_id(1) == {'id': 1}
    assert test_fixture_linkedlist.get_data_by_id(2) == {'id': 2}
    assert test_fixture_linkedlist.get_data_by_id(3) == {'id': 3}


# def test_linkedlist_get_by_id_errors(test_fixture_linkedlist):  # как проверить то что блок try/except отработал?
#     with pytest.raises(TypeError):
#         try:
#             test_fixture_linkedlist.get_data_by_id('1')
#         except TypeError:
#             pytest.fail()


def test_linkedlist_to_list():
    ll = LinkedList()
    assert ll.to_list() == []
