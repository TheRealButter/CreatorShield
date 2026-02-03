import subprocess
import sys


def test_cli_shields_message():
    result = subprocess.run(
        [sys.executable, "-m", "creatorshield", "--message", "Hello"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert result.stdout.strip() == "[shield] Hello"
