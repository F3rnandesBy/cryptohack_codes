def hex_to_bytes(hex_string):
    #remove espaços em branco e caracteres especiais
    hex_string = hex_string.strip().replace(' ', '').replace('0x', '')
    
    #verifica se o comprimento é par (cada byte precisa de d2 caracteres hex)
    if len(hex_string) % 2 != 0:
        raise ValueError("String hexadecimal deve ter comprimento par")
    
    try: 
        byte_data = bytes.fromhex(hex_string)
        return byte_data
    except ValueError as e:
        raise ValueError(f"String hexadecimal inválida: {e}")
    
def result():
    #bandeira codificada em hexadecimal 
    flag = "exemple_hexadecimal"
    print("Hexadecimal original: ", flag)
    
    #convertendo para bytes
    bytes_resultado = hex_to_bytes(flag)
    print("Bytes: ", bytes_resultado)
    
    #convertendo para string para ver o conteudo
    try:
        string_resultado = bytes_resultado.decode('utf-8')
        print("String decodificada: ", string_resultado)
    except UnicodeDecodeError:
        string_resultado = bytes_resultado.decode('latin-1')
        print("String decodificada: ", string_resultado)
    return bytes_resultado 

result()
