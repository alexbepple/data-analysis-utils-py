
def get_x_y(x, y, data):
    if data is not None:
        return data[x], data[y]
    else:
        return x, y
