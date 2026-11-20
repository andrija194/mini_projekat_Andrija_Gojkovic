from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier


class ModelFactory:
    @staticmethod
    def create(name):
        if name == "linear":
            return make_pipeline(StandardScaler(), LogisticRegression(max_iter=200))
        if name == "tree":
            return DecisionTreeClassifier(random_state=42)
        if name == "knn":
            return make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
        raise ValueError(f"Nepoznat model: {name}")
