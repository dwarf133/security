from tabulate import tabulate

def gds(a: int, b: int) -> list:
    if b > a:
        a, b = b, a 
    result = [[a, 1, 0, '-'], [b, 0, 1, a//b]]
    i = 2
    while True:
        if result[i-2][0]-result[i-1][0]*result[i-1][3] == 0:
            result.append([0, '-', '-', '-'])
            break
        else:
            ai = result[i-2][0]-result[i-1][0]*result[i-1][3]
            xi = result[i-2][1]-result[i-1][1]*result[i-1][3]
            yi = result[i-2][2]-result[i-1][2]*result[i-1][3]
            qi = result[i-1][0] // ai
            result.append([ai, xi, yi, qi])
            i += 1
    return result

if __name__ == '__main__':
    print(tabulate(gds(1378, 272), headers=['ai', 'xi', 'yi', 'qi'], tablefmt='pretty'))