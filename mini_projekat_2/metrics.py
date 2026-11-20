from abc import ABC, abstractmethod

from sklearn.metrics import accuracy_score, f1_score


class MetricStrategy(ABC):
    @abstractmethod
    def calculate(self, actual, predicted):
        pass


class AccuracyMetric(MetricStrategy):
    def calculate(self, actual, predicted):
        return accuracy_score(actual, predicted)


class F1Metric(MetricStrategy):
    def calculate(self, actual, predicted):
        return f1_score(actual, predicted, average="macro", zero_division=0)
