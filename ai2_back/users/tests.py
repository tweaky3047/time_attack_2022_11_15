from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
# Create your tests here.

class UserRegistrationAPIViewTestCase(APITestCase):
    def test_registration(self):
        url = reverse("user_view")
        user_data = {
            "username": "testuser",
            "fullname": "테스터",
            "email": "test@testuser.com",
            "password":"password",
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.data, {"message": "가입 완료!!"})
