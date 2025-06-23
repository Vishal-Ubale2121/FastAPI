# Version 1.25
from fastapi import FastAPI
import re

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "status": 200,
        "message": "Server is up and running..!",
    }


@app.get("/checkEven/{number}")
def check_even(number: int):
    result = "Number is even" if number % 2 == 0 else "Number is odd"
    return {
        "status": 200,
        "response": "Ok",
        "output": result,
    }


@app.get("/checkPrime/{number}")
def check_prime(number: int):
    if number <= 1:
        return {
            "status": 200,
            "output": False,
        }
    if number == 2:
        return {
            "status": 200,
            "output": True,
        }
    if number % 2 == 0:
        return {
            "status": 200,
            "output": False,
        }

    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return {
                "status": 200,
                "output": False,
            }

    return {
        "status": 200,
        "output": True,
    }


@app.get("/checkCase/{text}")
def check_case(text: str):
    has_upper = any(char.isupper() for char in text)
    has_lower = any(char.islower() for char in text)
    return {
        "status": 200,
        "response": "Ok",
        "output": {
            "has_uppercase": has_upper,
            "has_lowercase": has_lower,
        },
    }


@app.get("/checkPalindrome/{text}")
def check_palindrome(text: str):
    cleaned = "".join(filter(lambda c: c.isalnum(), str(text))).lower()
    is_palindrome = cleaned == cleaned[::-1]
    return {
        "status": 200,
        "response": "Ok",
        "output": is_palindrome,
    }


@app.get("/factorial/{number}")
def get_factorial(number: int):
    if number < 0:
        return {
            "status": 400,
            "error": "Factorial is not defined for negative numbers",
        }
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return {"status": 200, "output": factorial}


@app.get("/fibonacci/{n}")
def get_fibonacci(n: int):
    if n <= 0:
        return {"status": 400, "error": "Please provide a positive number"}
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return {"status": 200, "output": fib[:n]}


@app.get("/reverseString/{text}")
def reverse_string(text: str):
    return {"status": 200, "output": text[::-1]}


@app.get("/charCount/{text}")
def char_count(text: str):
    count = {}
    for char in text:
        count[char] = count.get(char, 0) + 1
    return {"status": 200, "output": len(count)}


@app.get("/wordCount/{text}")
def word_count(text: str):
    words = text.split()
    return {"status": 200, "output": len(words)}


@app.get("/isNumeric/{text}")
def is_numeric(text: str):
    return {"status": 200, "output": text.isnumeric()}


@app.get("/validateEmail/{email}")
def validate_email(email: str):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    is_valid = bool(re.match(pattern, email))
    return {"status": 200, "output": is_valid}


@app.get("/findVowels/{text}")
def find_vowels(text: str):
    vowels = "aeiouAEIOU"
    found = [ch for ch in text if ch in vowels]
    count = {v: found.count(v) for v in set(found)}
    return {"status": 200, "output": {"vowels": found, "count": count}}
