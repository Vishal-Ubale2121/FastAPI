import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


@pytest.mark.parametrize(
    "number,expected", [(4, "Number is even"), (3, "Number is odd")]
)
def test_check_even(number, expected):
    response = client.get(f"/checkEven/{number}")
    assert response.status_code == 200
    assert response.json()["output"] == expected


@pytest.mark.parametrize(
    "number,expected", [(2, True), (4, False), (17, True), (1, False), (0, False)]
)
def test_check_prime(number, expected):
    response = client.get(f"/checkPrime/{number}")
    assert response.status_code == 200
    assert response.json()["output"] == expected


@pytest.mark.parametrize(
    "text,upper,lower",
    [("Hello", True, True), ("HELLO", True, False), ("hello", False, True)],
)
def test_check_case(text, upper, lower):
    response = client.get(f"/checkCase/{text}")
    data = response.json()["output"]
    assert data["has_uppercase"] == upper
    assert data["has_lowercase"] == lower


@pytest.mark.parametrize(
    "text,expected",
    [("racecar", True), ("hello", False), ("A man, a plan, a canal, Panama", True)],
)
def test_check_palindrome(text, expected):
    response = client.get(f"/checkPalindrome/{text}")
    assert response.status_code == 200
    assert response.json()["output"] == expected


@pytest.mark.parametrize("number,expected", [(5, 120), (0, 1)])
def test_get_factorial(number, expected):
    response = client.get(f"/factorial/{number}")
    assert response.status_code == 200
    assert response.json()["output"] == expected


def test_get_factorial_negative():
    response = client.get("/factorial/-1")
    assert response.status_code == 200


@pytest.mark.parametrize("n,expected", [(5, [0, 1, 1, 2, 3])])
def test_get_fibonacci(n, expected):
    response = client.get(f"/fibonacci/{n}")
    assert response.status_code == 200
    assert response.json()["output"] == expected


def test_get_fibonacci_invalid():
    response = client.get("/fibonacci/0")
    assert response.status_code == 200


def test_reverse_string():
    response = client.get("/reverseString/hello")
    assert response.status_code == 200
    assert response.json()["output"] == "olleh"


def test_char_count():
    response = client.get("/charCount/hello")
    assert response.status_code == 200
    assert response.json()["output"] == 4


def test_word_count():
    response = client.get("/wordCount/hello world test")
    assert response.status_code == 200
    assert response.json()["output"] == 3


@pytest.mark.parametrize("text,expected", [("12345", True), ("abc123", False)])
def test_is_numeric(text, expected):
    response = client.get(f"/isNumeric/{text}")
    assert response.status_code == 200
    assert response.json()["output"] == expected


@pytest.mark.parametrize(
    "email,expected", [("test@example.com", True), ("invalid_email", False)]
)
def test_validate_email(email, expected):
    response = client.get(f"/validateEmail/{email}")
    assert response.status_code == 200
    assert response.json()["output"] == expected


def test_find_vowels():
    response = client.get("/findVowels/Accenture")
    assert response.status_code == 200
    data = response.json()["output"]
    assert "A" in "".join(data["vowels"]).upper() or "E" in "".join(
        data["vowels"]
    ).upper()
