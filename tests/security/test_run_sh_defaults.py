"""Static regression contract for the loopback-first launcher defaults."""

from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
RUNNER = REPOSITORY_ROOT / "run.sh"


def test_launcher_has_no_predictable_first_run_authority_values():
    source = RUNNER.read_text(encoding="utf-8")

    assert "BASIC_AUTH_PASSWORD=changeme" not in source
    assert "AUTH_ENCRYPTION_SECRET=my-test-salt" not in source
    assert "generate_local_secret()" in source
    assert "/dev/urandom" in source
    assert "umask 077" in source


def test_launcher_defaults_to_loopback_and_allows_explicit_override():
    source = RUNNER.read_text(encoding="utf-8")

    assert "HOST=${HOST:-127.0.0.1}" in source
    assert 'HOST="$2"' in source
    assert 'BASIC_AUTH_PASSWORD=${BASIC_AUTH_PASSWORD}' in source
    assert 'AUTH_ENCRYPTION_SECRET=${AUTH_ENCRYPTION_SECRET}' in source
