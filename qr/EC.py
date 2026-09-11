from qr.gf256 import alpha_to_int
from qr.gf256 import int_to_alpha

def multiply_polynomials(p1, p2):
    result = [0] * (len(p1) + len(p2) - 1)
    for p1_index in range(len(p1)):
        for p2_index in range(len(p2)):
            result_index = p1_index + p2_index
            if p1[p1_index] == 0 or p2[p2_index] == 0:
                result_coeff = 0
            else:
                p1_alpha = int_to_alpha[p1[p1_index]]
                p2_alpha = int_to_alpha[p2[p2_index]]
                result_alpha = (p1_alpha + p2_alpha) % 255
                result_coeff = alpha_to_int[result_alpha]
            result[result_index] ^= result_coeff
    return result

def generate_gp(num_EC): # generator polynomial
    gp = [1]
    alpha_exp = 0
    for _ in range(num_EC):
        factor = [alpha_to_int[alpha_exp], 1]
        gp = multiply_polynomials(gp, factor)
        alpha_exp += 1
    return gp

def get_EC_codewords(data, num_EC):
    gp_coeff = generate_gp(num_EC)
    reversed_data = data[::-1]

    message_polynomial = [0] * num_EC
    for coeff in reversed_data:
        message_polynomial.append(coeff)

    gp = [0] * (len(data) - 1)

    for coeff in gp_coeff:
        gp.append(coeff)

    for _ in range(len(data)):
        lead_msg_index = None
        for i in range(len(message_polynomial) - 1, -1, -1):
            if message_polynomial[i] == 0:
                continue
            lead_msg_index = i
            break
        
        lead_msg_coeff = message_polynomial[lead_msg_index]
        lead_msg_alpha = int_to_alpha[lead_msg_coeff]

        temp_gp = gp.copy()

        for gp_index in range(len(gp)):
            if temp_gp[gp_index] != 0:
                gp_alpha = int_to_alpha[temp_gp[gp_index]]
                result_alpha = (lead_msg_alpha + gp_alpha) % 255
                result_coeff = alpha_to_int[result_alpha]
                temp_gp[gp_index] = result_coeff

        for msg_index in range(len(message_polynomial)):
            message_polynomial[msg_index] = message_polynomial[msg_index] ^ temp_gp[msg_index]

        del gp[0]
        gp.append(0)


    EC_codewords = []
    for i in range(num_EC - 1, -1, -1):
        EC_codewords.append(message_polynomial[i])

    return EC_codewords

    



    

    


