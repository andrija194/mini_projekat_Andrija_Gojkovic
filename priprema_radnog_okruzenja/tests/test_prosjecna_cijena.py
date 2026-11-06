"""Testovi funkcije prosjecna_cijena."""

import pytest

from prosjecna_cijena import prosjecna_cijena


def test_prosjecna_cijena_vise_vrijednosti():
    assert prosjecna_cijena([10, 20, 30]) == pytest.approx(20.0)


def test_prosjecna_cijena_jedna_vrijednost():
    assert prosjecna_cijena([15.5]) == pytest.approx(15.5)


def test_prazna_lista():
    with pytest.raises(ValueError, match="prazna"):
        prosjecna_cijena([])


def test_negativna_cijena():
    with pytest.raises(ValueError, match="nenegativni"):
        prosjecna_cijena([10, -5])


def test_nekonacna_cijena():
    with pytest.raises(ValueError):
        prosjecna_cijena([5, float("nan")])
