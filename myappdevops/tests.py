from django.test import TestCase
from django.urls import reverse
import os


class HomePageTest(TestCase):

    def test_home_page_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_content(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertContains(response, "Welcome to my Django app")


class JenkinsLearningTest(TestCase):

    def test_conditional_fail(self):
        """
        This test will FAIL only if environment variable is set
        """
        if os.getenv("FAIL_TEST") == "1":
            self.assertEqual(1, 2)  # ❌ force fail
        else:
            self.assertEqual(1, 1)  # ✅ pass
