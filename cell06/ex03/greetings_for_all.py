def greetings(name="noble stranger"):
    if type (name) is not str:
        print("Erro: argumemt is not a string.")
    else:
        print(f"Hello, {name}.")
greetings("Alexandra")
greetings("Wil")
greetings()
greetings(42)