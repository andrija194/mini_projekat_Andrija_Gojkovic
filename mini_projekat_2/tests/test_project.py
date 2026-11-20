from unittest.mock import patch

import pytest
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

from experiments import Experiment, IrisExperiment, TimedExperiment
from metrics import AccuracyMetric, F1Metric
from models import ModelFactory
from observers import ConsoleObserver, HistoryObserver


@pytest.mark.parametrize("name, expected", [
    ("linear", LogisticRegression),
    ("tree", DecisionTreeClassifier),
    ("knn", KNeighborsClassifier),
])
def test_factory_creates_expected_model(name, expected):
    model = ModelFactory.create(name)
    estimator = model.steps[-1][1] if hasattr(model, "steps") else model
    assert isinstance(estimator, expected)


def test_unknown_model():
    with pytest.raises(ValueError, match="Nepoznat model"):
        ModelFactory.create("unknown")


def test_accuracy():
    assert AccuracyMetric().calculate([0, 0, 1, 1], [0, 1, 1, 1]) == 0.75


def test_macro_f1():
    result = F1Metric().calculate([0, 0, 1, 1], [0, 1, 1, 1])
    assert result == pytest.approx((2 / 3 + 4 / 5) / 2)


def test_multiple_observers_receive_events():
    experiment = IrisExperiment("tree", AccuracyMetric())
    first = HistoryObserver()
    second = HistoryObserver()
    experiment.add_observer(first)
    experiment.add_observer(second)
    experiment.run()
    expected = ["Pocetak eksperimenta", "Pocetak treninga",
                "Trening zavrsen", "Eksperiment zavrsen"]
    assert first.messages == expected
    assert second.messages == expected


def test_console_observer(capsys):
    ConsoleObserver().update("Trening zavrsen")
    assert capsys.readouterr().out == "Trening zavrsen\n"


@pytest.mark.parametrize("name", ["linear", "tree", "knn"])
def test_iris_experiment(name):
    result = IrisExperiment(name, AccuracyMetric()).run()
    assert result["model"] == name
    assert 0.8 <= result["score"] <= 1


def test_strategy_can_be_replaced():
    experiment = IrisExperiment("tree", AccuracyMetric())
    experiment.metric = F1Metric()
    result = experiment.run()
    assert 0.8 <= result["score"] <= 1


def test_timing_decorator_preserves_result():
    experiment = IrisExperiment("tree", AccuracyMetric())
    original = experiment.run()
    with patch("experiments.perf_counter", side_effect=[10.0, 10.25]):
        timed = TimedExperiment(experiment).run()
    assert timed["model"] == original["model"]
    assert timed["score"] == original["score"]
    assert timed["time_seconds"] == pytest.approx(0.25)


def test_template_works_with_different_data_source():
    class SmallExperiment(Experiment):
        def load_data(self):
            x = [[i % 2, i % 2] for i in range(60)]
            y = [i % 2 for i in range(60)]
            return x, y

    result = SmallExperiment("tree", AccuracyMetric()).run()
    assert result["score"] == 1.0
