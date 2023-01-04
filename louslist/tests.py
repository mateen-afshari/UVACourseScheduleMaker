import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from django.test import Client

class departmentTests(TestCase):
    def test_edhs(self):
        url = '/EDHS'
        response = self.client.get(url)
        self.assertContains(response, "EDHS")
    def test_edis(self):
        url = '/EDIS'
        response = self.client.get(url)
        self.assertContains(response, "EDIS")
    def test_edlf(self):
        url = '/EDLF'
        response = self.client.get(url)
        self.assertContains(response, "EDLF")
    def test_kine(self):
        url = '/KINE'
        response = self.client.get(url)
        self.assertContains(response, "KINE")
    def test_klpa(self):
        url = '/KLPA'
        response = self.client.get(url)
        self.assertContains(response, "KLPA")
    