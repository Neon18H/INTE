import threading
from datetime import datetime, timedelta
from .models import Indicator, IndicatorObservation
from .providers import MockDnsProvider, MockReputationProvider, MockWhoisProvider


def _run(indicator_id: int) -> None:
    indicator = Indicator.objects.get(pk=indicator_id)
    whois = MockWhoisProvider().lookup(indicator.value)
    dns = MockDnsProvider().lookup(indicator.value)
    reputation = MockReputationProvider().lookup(indicator.value)

    IndicatorObservation.objects.create(
        indicator=indicator,
        source="mock-enrichment",
        first_seen=datetime.utcnow() - timedelta(days=30),
        last_seen=datetime.utcnow(),
        confidence=70,
        severity=4,
        tags=["mock", reputation["verdict"], "dns"],
        note=f"WHOIS: {whois} | DNS: {dns} | Reputation: {reputation}",
    )


def trigger_enrichment(indicator_id: int) -> None:
    thread = threading.Thread(target=_run, args=(indicator_id,), daemon=True)
    thread.start()
