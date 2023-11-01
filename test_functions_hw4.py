
import unittest
import sys
from pandas.testing import assert_series_equal
import pandas as pd
import numpy as np
from hw4 import *

# TEST CLASS PATIENT

class TestPatient(unittest.TestCase):
    
    def setUp(self):
        self.patient_with_covid = Patient('John Doe', ['fever', 'cough'])
        self.patient_without_covid = Patient('Jane Doe', ['headache', 'sore_throat'])
    
    def test_patient_creation(self):
        self.assertEqual(self.patient_with_covid.name, 'John Doe')
        self.assertEqual(self.patient_with_covid.symptoms, ['fever', 'cough'])
        self.assertEqual(self.patient_with_covid.tests, {})
    
    def test_add_test(self):
        self.patient_with_covid.add_test('covid', True)
        self.assertEqual(self.patient_with_covid.tests, {'covid': True})
    
    def test_has_covid_positive(self):
        self.patient_with_covid.add_test('covid', True)
        probability = self.patient_with_covid.has_covid()
        self.assertEqual(probability, 0.99)
    
    def test_has_covid_negative(self):
        probability = self.patient_without_covid.has_covid()
        self.assertEqual(probability, 0.05)
    
    def test_has_covid_with_symptoms(self):
        self.patient_without_covid.symptoms.append('fever')
        probability = self.patient_without_covid.has_covid()
        self.assertEqual(probability, 0.15)
    
    def test_has_covid_negative_test(self):
        self.patient_without_covid.add_test('covid', False)
        prob = self.patient_without_covid.has_covid()
        self.assertEqual(prob, 0.01)

# TEST CLASSES CARD AND DECK

class TestCardDeck(unittest.TestCase):
    
    def test_card_creation(self):
        card = Card('Hearts', 'A')
        self.assertEqual(card.suit, 'Hearts')
        self.assertEqual(card.value, 'A')
    
    def test_deck_creation(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)
    
    def test_deck_shuffle(self):
        deck = Deck()
        original_order = deck.cards.copy()
        deck.shuffle()
        self.assertNotEqual(original_order, deck.cards)
    
    
    def test_deck_draw(self):
        deck = Deck()
        drawn_card = deck.draw()
        self.assertIsNotNone(drawn_card)
    
    def test_dech_draw2(self):
        deck2 = Deck()
        self.assertIsNotNone(deck2.draw())
    
    def test_deck_empty_draw(self):
        deck = Deck()
        while deck.cards:
            deck.draw()
        
        drawn_card = deck.draw()
        self.assertEqual(drawn_card, "No more cards to draw.")

# TEST CLASS SHAPE

class TestShape(unittest.TestCase):
    
    def test_triangle(self):
        shape = Triangle(base = 3, c1 = 4, c2 = 5, h = 4)
        self.assertEqual(shape.compute_surface(), 6)
        self.assertEqual(shape.compute_perimeter(), 12)
    
    def test_triangle_null(self):
        self.assertRaises(ValueError, Triangle, base = 0, c1 = 0, c2 = 0, h = 0)
        #    shape = Triangle(base = 0, c1 = 0, c2 = 0, h = 0)
    
    def test_triangle_not_valid(self):
        self.assertRaises(ValueError, Triangle, base = 3, c1 = 4, c2 = 5, h = 10)
    
    def test_triangle_not_valid2(self):
        self.assertRaises(ValueError, Triangle, base = 7, c1 = 4, c2 = 2, h = 1)
    
    def test_rectangle(self):
        shape = Rectangle(4, 5)
        self.assertEqual(shape.compute_surface(), 20)
        self.assertEqual(shape.compute_perimeter(), 18)
    
    def test_rectangle_null(self):
        #shape = Rectangle(0, 0)
        self.assertRaises(ValueError, Rectangle, 0, 0)
    
    def test_circle_null(self):
        #shape = Circle(0)
        self.assertRaises(ValueError, Circle, 0)
    
    def test_circle(self):
        shape = Circle(7)
        self.assertEqual(shape.compute_surface(), pi*49)
        self.assertEqual(shape.compute_perimeter(), 14*pi)