from abc import ABC, abstractmethod
from time import perf_counter

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from models import ModelFactory


class ExperimentRunner(ABC):
    @abstractmethod
    def run(self):
        pass


class Experiment(ExperimentRunner):
    def __init__(self, model_name, metric):
        self.model_name = model_name
        self.metric = metric
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

    @abstractmethod
    def load_data(self):
        pass

    def run(self):
        self.notify("Pocetak eksperimenta")
        x, y = self.load_data()
        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.3, random_state=42, stratify=y
        )
        model = ModelFactory.create(self.model_name)
        self.notify("Pocetak treninga")
        model.fit(x_train, y_train)
        self.notify("Trening zavrsen")
        predicted = model.predict(x_test)
        score = self.metric.calculate(y_test, predicted)
        self.notify("Eksperiment zavrsen")
        return {"model": self.model_name, "score": float(score)}


class IrisExperiment(Experiment):
    def load_data(self):
        return load_iris(return_X_y=True)


class ExperimentDecorator(ExperimentRunner):
    def __init__(self, experiment):
        self.experiment = experiment

    def run(self):
        return self.experiment.run()


class TimedExperiment(ExperimentDecorator):
    def run(self):
        start = perf_counter()
        result = super().run()
        result["time_seconds"] = perf_counter() - start
        return result
