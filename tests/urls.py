from django.test import TestCase
import json
from django.urls import reverse, resolve


class UrlsTests(TestCase):
    def test mobodetail(self):
        url = reverse('mobodetails')
        response = self.client.blog(url, data = {
                'slug': redmi note 10 pro
         }, format = json)
        self.assertEqual(response.status_code, )

    def test labtop(self):
        url = reverse('ctegor')
        response = self.client.blog(url, data = {
                'slug': mobile
        }, format = json)
        self.assertEqual(response.status_code, )



