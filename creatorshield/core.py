"""Core message shielding logic."""


def shield_message(message: str) -> str:
    """Wrap a message with a shield marker.

    Args:
        message: The message to shield.

    Returns:
        The shielded message.
    """
    cleaned = message.strip()
    if not cleaned:
        return "[shield]"
    return f"[shield] {cleaned}"
