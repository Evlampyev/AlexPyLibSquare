class NumberValidator:
    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, float | int) and value <= 0:
            raise ValueError(f"Значение '{value}' не является целым положительным числом")
        self.value = value
