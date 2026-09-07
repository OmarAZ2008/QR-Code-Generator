int_to_alpha: list[None | int] = [None]*256
alpha_to_int: list[None | int] = [None]*255

val = 1
for exp in range(255):
    alpha_to_int[exp] = val
    int_to_alpha[val] = exp
    val *= 2
    if val > 255:
        val = val^285

