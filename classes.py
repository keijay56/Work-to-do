class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return f"'{self.title}' by {self.author}"


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32


class Timer:
    def __init__(self, start=0):
        self.time = start

    def tick(self):
        self.time += 1

    def reset(self):
        self.time = 0

    def current_time(self):
        return self.time
