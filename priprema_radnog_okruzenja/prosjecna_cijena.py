"""Jednostavan primjer obračuna prosječne cijene."""


def prosjecna_cijena(cijene: list[float]) -> float:
    """Vrati prosječnu cijenu; odbij praznu listu i neispravne cijene."""
    if not cijene:
        raise ValueError("Lista cijena ne smije biti prazna.")

    for cijena in cijene:
        if isinstance(cijena, bool) or not isinstance(cijena, (int, float)):
            raise TypeError("Sve cijene moraju biti brojevi.")
        if not 0 <= cijena < float("inf"):
            raise ValueError("Cijene moraju biti nenegativni konačni brojevi.")

    return sum(cijene) / len(cijene)


if __name__ == "__main__":
    primjer = [10.0, 20.0, 30.0]
    print(f"Prosječna cijena: {prosjecna_cijena(primjer):.2f} EUR")
