# Python Module calculate customer points on purchase

def calculate_points(total_purchases):

    if total_purchases <= 100:
        points = 10
    elif total_purchases >= 101 and total_purchases <= 500:
        points = 20
    else:
        points = 50

    return points
