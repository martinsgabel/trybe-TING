from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.__data = []

    def __len__(self):
        return len(self.__data)

    def __contains__(self, value):
        if value in self.__data:
            return True
        return False

    def enqueue(self, value):
        self.__data.append(value)

    def dequeue(self):
        return self.__data.pop(0)

    def search(self, index):
        try:
            if index < 0 or index > len(self.__data):
                raise IndexError
            return self.__data[index]
        except IndexError:
            raise IndexError
