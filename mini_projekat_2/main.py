from experiments import IrisExperiment, TimedExperiment
from metrics import AccuracyMetric, F1Metric
from observers import ConsoleObserver


def main():
    for model_name in ["linear", "tree", "knn"]:
        for metric in [AccuracyMetric(), F1Metric()]:
            print(f"\nModel: {model_name}, metrika: {type(metric).__name__}")
            experiment = IrisExperiment(model_name, metric)
            experiment.add_observer(ConsoleObserver())
            result = TimedExperiment(experiment).run()
            print(f"Rezultat: {result['score']:.4f}")
            print(f"Vrijeme: {result['time_seconds']:.6f} s")


if __name__ == "__main__":
    main()
