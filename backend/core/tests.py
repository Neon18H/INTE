from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Vulnerability


class AuthTests(APITestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username="tester", password="pass1234", is_staff=True)

    def test_jwt_login(self):
        response = self.client.post("/api/v1/auth/token/", {"username": "tester", "password": "pass1234"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)


class IndicatorTests(APITestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username="iocuser", password="pass1234", is_staff=True)
        token = self.client.post("/api/v1/auth/token/", {"username": "iocuser", "password": "pass1234"})
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token.data['access']}")

    def test_create_indicator(self):
        payload = {"type": "ip", "value": "8.8.8.8", "normalized": "8.8.8.8"}
        response = self.client.post("/api/v1/indicators/", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class VulnerabilityTests(APITestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username="vulnuser", password="pass1234", is_staff=True)
        token = self.client.post("/api/v1/auth/token/", {"username": "vulnuser", "password": "pass1234"})
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token.data['access']}")
        Vulnerability.objects.create(
            cve="CVE-2024-0001",
            title="Demo",
            description="Demo vuln",
            cvss=7.5,
            epss=0.2,
            kev_flag=True,
            published_date="2024-01-01",
            vendor="Vendor",
            product="Product",
            references_json=["https://example.com"],
        )

    def test_list_vulnerabilities(self):
        response = self.client.get("/api/v1/vulnerabilities/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
