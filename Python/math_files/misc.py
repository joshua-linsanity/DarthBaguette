
# Given float x, # sig figs sf, and units, prints x in engineering notation
def engr(x: int, sf: int, units: str):
    n = 0
    while x >= 10:
        x /= 10
        n += 1

    x = round(x, sf - 1)
    rem = n % 3
    n -= rem

    prefix = {-12: "p", -9: "n", -6: "u", -3: "m", 3: "k", 6: "M", 9: "G", 12: "T", 15: "P", 18: "E"}

    if n in prefix:
        return f"{x} {prefix[n]}{units}"
    else:
        return f"{x}E{n + rem} {units}"
