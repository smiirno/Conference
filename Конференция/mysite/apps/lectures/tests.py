from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Lecture


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.post = Lecture.objects.create(
            audience_number=2,
            lecture_title='A good title',
            speaker_name=self.user,
            start_time=timezone.now(),
            end_time=timezone.now() + 1
        )

    def test_string_representation(self):
        lecture = Lecture(lecture_title='A sample title')
        self.assertEqual(str(lecture), lecture.lecture_title)

    def test_input(self):
        self.assertTrue(f'{self.lecture.audience_number}'.isdigit())
        self.assertTrue(f'{self.lecture.lecture_title}'.isalpha())
        self.assertTrue(f'{self.lecture.speaker_name}'.isalpha())

    def test_lecture_content(self):
        self.assertEqual(f'{self.lecture.lecture_title}', 'A good title')
        self.assertEqual(f'{self.lecture.speaker_name}', 'testuser')
        self.assertEqual(f'{self.lecture.audience_number}', '2')
