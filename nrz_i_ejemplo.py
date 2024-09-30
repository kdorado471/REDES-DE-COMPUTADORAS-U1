def nrz_i(data):
    encoded = []
    current_level = 0

    for bit in data:
        if bit == 1:
            current_level = 1 if current_level == 0 else 0
        encoded.append(current_level)
    
    return encoded


data = [1, 0, 0, 1, 1, 0, 1, 0]

nrz_i_encoded = nrz_i(data)


print(f"Datos de entrada: {data}")
print(f"Codificación NRZ-I: {nrz_i_encoded}")

