import random
from datetime import datetime, timedelta


class MockWhoisProvider:
    def lookup(self, value: str) -> dict:
        return {
            "registrar": "MockRegistrar",
            "created": (datetime.utcnow() - timedelta(days=1000)).isoformat(),
        }


class MockDnsProvider:
    def lookup(self, value: str) -> dict:
        return {"a": ["203.0.113.10"], "mx": ["mail.mock"]}


class MockReputationProvider:
    def lookup(self, value: str) -> dict:
        return {
            "score": random.randint(10, 95),
            "verdict": random.choice(["benign", "suspicious", "malicious"]),
        }
