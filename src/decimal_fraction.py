from fractions import Fraction

# 少数を定義
decimal_number = 0.75

fraction = Fraction(decimal_number).limit_denominator()

print(f"少数: {decimal_number}")
print(f"分数: {fraction.numerator}/{fraction.denominator}")
