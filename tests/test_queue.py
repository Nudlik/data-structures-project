"""Здесь надо написать тесты с использованием unittest для модуля queue."""

from src.queue import Queue
import pytest


@pytest.fixture
def test_fixture():
    queue = Queue()
    queue.enqueue('data1')
    queue.enqueue('data2')
    queue.enqueue('data3')
    return queue


def test_queue(test_fixture):
    assert test_fixture.dequeue() == 'data1'
    assert test_fixture.dequeue() == 'data2'
    assert test_fixture.dequeue() == 'data3'
    assert test_fixture.dequeue() is None


def test_queue_str(test_fixture):
    assert str(test_fixture) == 'data1\ndata2\ndata3'


def test_queue_str_none():
    queue = Queue()
    assert str(queue) == ''


def test_queue_enqueue(test_fixture):
    assert test_fixture.head.data == 'data1'
    assert test_fixture.head.next_node.data == 'data2'
    assert test_fixture.tail.data == 'data3'
    assert test_fixture.tail.next_node is None


def test_queue_attribute_error():
    queue = Queue()
    with pytest.raises(AttributeError):
        queue.tail.next_node.data
