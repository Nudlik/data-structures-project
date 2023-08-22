"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import pytest

from src.stack import Stack


@pytest.fixture()
def test_stack():
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')
    return stack


def test_stack_push(test_stack):
    assert test_stack.top.data == 'data3'
    assert test_stack.top.next_node.data == 'data2'
    assert test_stack.top.next_node.next_node.data == 'data1'
    assert test_stack.top.next_node.next_node.next_node is None
    with pytest.raises(AttributeError):
        test_stack.top.next_node.next_node.next_node.data


def test_stack_pop(test_stack):
    assert test_stack.pop() == 'data3'
    assert test_stack.pop() == 'data2'
    assert test_stack.pop() == 'data1'
    assert test_stack.pop() is None
