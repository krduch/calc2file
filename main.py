from calcFunc import dodawanie, odejmowanie, mnozenie, dzielenie

num1 = float(input("wprowadz pierwszą liczbę: "))
num2 = float(input("wprowadz drugą liczbę: "))
dzial = str(input("wprowadz działanie które chcesz wykonać (+ , - , *, / ): "))


if dzial == "+":
    dodawanie()

elif dzial == "-":
    odejmowanie()

elif dzial == "*":
    mnozenie()

elif dzial == "/":
    dzielenie()