import random

"""
Return a random Treblle endpoint
@returns { string }
"""


def treblle_base_url() -> str:
    base_url = [
        "https://rocknrolla.treblle.com",
        "https://punisher.treblle.com",
        "https://sicario.treblle.com",
    ]

    randomIndex: int = random.randint(0, len(base_url) - 1)

    return base_url[randomIndex]


if __name__ == "__main__":
    treblle_base_url()
