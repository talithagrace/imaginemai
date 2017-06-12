import os
import unittest
from os.path import abspath
from django.test import TestCase
from django.db import connection
from django.core import signals
from django.core.handlers.wsgi import WSGIHandler
from django.conf import settings
from django.core.files.base import ContentFile
from PIL import Image

class PhotoTests(unittest.TestCase):
    def test_jpg(self):
        image_path = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(image_path, "testdata", "test.jpg")
        trial_image = Image.open(image_path)
        try:
            trial_image.load()
        except:
            print ("!!!NO JPEG SUPPORT!!!")
            print ("To fix this:")
            print ("sudo aptitude install libjpeg libjpeg-dev")
            print ("sudo aptitude install libfreetype6 libfreetype6-dev")
            print ("in your virtual env: pip install http://effbot.org/media/downloads/Imaging-1.1.6.tar.gz")
            self.assertTrue(False)
