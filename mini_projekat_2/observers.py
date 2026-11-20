from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass


class ConsoleObserver(Observer):
    def update(self, message):
        print(message)


class HistoryObserver(Observer):
    def __init__(self):
        self.messages = []

    def update(self, message):
        self.messages.append(message)
