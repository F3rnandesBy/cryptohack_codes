import base64

# Decodificar o hexadecimal em bytes, ou seja, criar uma função hex_base64
def hex_to_bytes(flag_hexadecimal):
    # Remover espaços e caracteres especiais
    flag_hexadecimal = flag_hexadecimal.strip().replace(' ', '').replace('0x', '')
    
    # Verifica se o hexadecimal é par
    if len(flag_hexadecimal) % 2 != 0:
        raise ValueError("String hexadecimal deve ter comprimento par!")
    try:
        bytes_data = bytes.fromhex(flag_hexadecimal)
        return bytes_data
    except ValueError as e:
        raise ValueError(f"String decimal inválida: {e}") 


def bytes_encode_base64():
    flag = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
    print("Flag hexadecimal: ", flag)

    bytes_result = hex_to_bytes(flag)
    print("Resultado em bytes: ", bytes_result)
    
    string_resultado = base64.b64encode(bytes_result)
    print("Resultado Final: ", string_resultado.decode())

bytes_encode_base64()
