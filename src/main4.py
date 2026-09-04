import secrets
import string

otp = "".join(secrets.choices(string.digits) for _ in range(6))

print("Your Secure OTP is:", otp)