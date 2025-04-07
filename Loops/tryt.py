
try:
    result = 7 + 8 == 11
    # Si no lo es, se lanza una excepción AssertionError con un mensaje personalizado
    assert result == 11, "El resultado no es 11"
    
except AssertionError as error:
    print(f"Error: {error}")
