# -*- coding: utf-8 -*-
"""Klasa Product -- zadanie do samodzielnego wykonania."""


class Product:
    """Reprezentuje produkt w sklepie internetowym."""

    def __init__(self, name: str, price: float, quantity: int):
        # TODO: Zapisz atrybuty name, price, quantity
        # Pamietaj o walidacji: price >= 0, quantity >= 0
        if price < 0:
            raise ValueError('Cena nie może być ujemna')
        if quantity < 0:
            raise ValueError('Ilość nie może być ujemna')
        
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount: int):
        # TODO: Dodaj ilosc do magazynu. Rzuc ValueError jesli amount < 0
        if amount < 0:
            raise ValueError('ilość nie może być ujemna')
        self.quantity += amount

    def remove_stock(self, amount: int):
        # TODO: Usun ilosc z magazynu.
        # Rzuc ValueError jesli amount < 0 lub amount > quantity
        if amount < 0:
            raise ValueError('ilosc nie może być ujemna')
        if amount > self.quantity:
            raise ValueError('brak danej ilości na magazynie')
        self.quantity -= amount
        

    def is_available(self) -> bool:
        # TODO: Zwroc True jesli quantity > 0
        return self.quantity > 0

    def total_value(self) -> float:
        # TODO: Zwroc price * quantity
        return self.price * self.quantity
    
    def apply_discount(self, percent: float):
        """Obniża cenę o podany procent (0-100)."""
        if percent < 0 or percent > 100:
            raise ValueError("Procent musi być w zakresie 0-100")

        self.price -= self.price * (percent / 100)