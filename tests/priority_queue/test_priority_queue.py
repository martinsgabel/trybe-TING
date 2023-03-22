from ting_file_management.priority_queue import PriorityQueue
import pytest

mock = [
    {"qtd_linhas": 1},
    {"qtd_linhas": 7},
    {"qtd_linhas": 3},
]


def test_basic_priority_queueing():
    instance = PriorityQueue()

    for each in mock:
        instance.enqueue(each)

    assert len(instance) == len(mock)

    assert instance.search(0) == mock[0]
    assert instance.search(1) == mock[2]
    assert instance.search(2) == mock[1]
    instance.dequeue()
    assert instance.search(0) == mock[2]

    with pytest.raises(IndexError):
        instance.search(5)
