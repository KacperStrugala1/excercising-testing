def get_weather(temp):
    if temp > 20:
        return "It's warm outside!"
    else:
        return "It's cold outside!"
    
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by 0")
    else:
        return a / b
    