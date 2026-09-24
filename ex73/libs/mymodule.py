from math import sqrt

def tinh_pt_bac_2(a,b,c):
    if a == 0:
    # bx+c=0
        if b == 0 and c == 0:
            return "PT vo so nghiem"
        elif b == 0 and c != 0:
            return "PT vo nghiem"
        else:
            x = -c / b
            return x
    else:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            return "PT vo nghiem"
        elif delta == 0:
            x = -b / (2 * a)
            return f"Nghiem kep x1 = x2 = {x:.2f}"
        else:
            x1 = (-b - sqrt(delta)) / (2 * a)
            x2 = (-b + sqrt(delta)) / (2 * a)
            return f"x1 = {x1:.2f}, x2 = {x2:.2f}"