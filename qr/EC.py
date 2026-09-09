from qr.gf256 import alpha_to_int
from qr.gf256 import int_to_alpha

def multiply_polynomials(p1, p2):
    result = [0] * (len(p1) + len(p2) - 1)
    for p1_index in range(len(p1)):
        for p2_index in range(len(p2)):
            result_index = p1_index + p2_index
            if p1[p1_index] == 0 or p2[p2_index] == 0:
                coeff = 0
            else:
                coeff = (int_to_alpha[p1[p1_index]] + int_to_alpha[p2[p2_index]]) % 255
                coeff = alpha_to_int[coeff]
            result[result_index] ^= coeff
    return result

def generate_gp(num_EC):
    gp = [1]
    alpha_exp = 0
    for _ in range(num_EC):
        factor = [alpha_to_int[alpha_exp], 1]
        gp = multiply_polynomials(gp, factor)
        alpha_exp += 1
    return gp
