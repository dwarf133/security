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
    return {
            'ai': result[len(result)-2][0],
            'xi': result[len(result)-2][1],
            'yi': result[len(result)-2][2],
            'qi': result[len(result)-2][0], 
            'data': result
            }

def mult_obr(a: int, m: int) -> int:
    tGds = gds(a, m)
    if(tGds['ai'] != 1):
        return None
    else:
        obr = tGds['yi']
        if obr < 0:
            obr  = obr + m
        return obr

def pow_by_mod(a: int, k: int, m: int) -> int:
    if k == 0:
        return 1
    binary = bin(k)
    binary = binary.removeprefix('0b')
    replaced_bin = binary.replace('1', 'sm')
    replaced_bin = replaced_bin.replace('0', 's')
    replaced_bin = replaced_bin.removeprefix('sm')
    ans = a
    for act in replaced_bin:
        if act == 's':
            ans = ((ans * ans) % m)
        if act == 'm':
            ans = ((ans * a) % m)
    return ans

def comparison(a: int, b: int, m: int) -> list:
    g = gds(a, m)
    if(b % g['ai'] != 0):
        return []
    else:
        pass

if __name__ == '__main__':
    # print(tabulate(gds(1378, 272)['data'], headers=['ai', 'xi', 'yi', 'qi'], tablefmt='pretty'))
    # k = gds(31, 11)
    # print(k['ai'], k['xi'], k['yi'], k['qi'])
    
    # print(mult_obr(13, 57))
    print(pow_by_mod(144, 183, 925))