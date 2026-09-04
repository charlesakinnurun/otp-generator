# 🔐 OTP Generator in Python

A simple Python project that demonstrates how to generate **One-Time Passwords (OTPs)** using progressively stronger approaches, from basic random number generation to the cryptographically stronger `secrets` module.

## 📌 Project Overview

This project explores four different ways to generate OTPs in Python:

1. **4-digit OTP** using `random.randint()`
2. **6-digit numeric OTP** using `random.randint()`
3. **6-digit OTP** using `random.choices()` and `string.digits`
4. **Secure 6-digit OTP** using Python's `secrets` module

The project demonstrates how OTP generation can evolve from a basic programming exercise into a more security-conscious implementation.

---

## 🧩 Version 1 — 4-Digit OTP

```python
import random

otp = random.randint(1000, 9999)

print("Your OTP is:", otp)
```

### Example Output

```text
Your OTP is: 4827
```

This generates a random **4-digit number** between `1000` and `9999`.

---

## 🔢 Version 2 — 6-Digit OTP

```python
import random

otp = random.randint(100000, 999999)

print("Your OTP is:", otp)
```

### Example Output

```text
Your OTP is: 735921
```

This increases the OTP length to **6 digits**, providing more possible combinations.

---

## 🔤 Version 3 — Using `string.digits`

```python
import random
import string

otp = "".join(random.choices(string.digits, k=6))

print("Your OTP is:", otp)
```

### Example Output

```text
Your OTP is: 194638
```

### How It Works

* `string.digits` provides the characters `0123456789`.
* `random.choices()` selects 6 digits.
* `"".join()` combines the selected digits into one string.

Using strings also means the OTP can naturally preserve leading zeros.

For example:

```text
042817
```

---

## 🛡️ Version 4 — Secure OTP Generation

```python
import secrets
import string

otp = "".join(secrets.choice(string.digits) for _ in range(6))

print("Your Secure OTP is:", otp)
```

### Example Output

```text
Your Secure OTP is: 583204
```

This version uses Python's **`secrets` module**, which is designed for generating values that need to be unpredictable and suitable for security-sensitive applications.

> **Note:** `random` is excellent for learning and general-purpose randomness, but it should not be relied upon for security-sensitive OTP generation. For real authentication systems, use a cryptographically secure generator such as `secrets`.

---

## 📊 Comparison

| Version | Method             |   Length | Security    |
| ------- | ------------------ | -------: | ----------- |
| 1       | `random.randint()` | 4 digits | Basic       |
| 2       | `random.randint()` | 6 digits | Basic       |
| 3       | `random.choices()` | 6 digits | Basic       |
| 4       | `secrets.choice()` | 6 digits | 🔐 Stronger |

---

## 🧠 Concepts Demonstrated

* Python modules
* Random number generation
* String manipulation
* `string.digits`
* `random.randint()`
* `random.choices()`
* `secrets.choice()`
* Generator expressions
* `join()`
* Basic security concepts

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/otp-generator.git
```

### 2. Navigate into the project

```bash
cd otp-generator
```

### 3. Run the Python file

```bash
python otp_generator.py
```

No external packages are required.

---

## 🔮 Possible Improvements

This project could be extended by adding:

* OTP expiration timers
* OTP verification
* Maximum verification attempts
* User input
* SMS/email delivery
* Configurable OTP length
* OTP regeneration
* Hashing OTPs before storage
* Rate limiting

---

## 🎯 Learning Goal

The goal of this project is to demonstrate the progression from **basic random OTP generation** to a more appropriate **secure OTP generation approach** using Python's built-in `secrets` module.

## 📄 License

This project is open-source and available for educational purposes.
