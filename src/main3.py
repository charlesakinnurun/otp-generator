import random
import string

otp = "".join(random.choices(string.digits,k=6))

print("Your OTP is:", otp)