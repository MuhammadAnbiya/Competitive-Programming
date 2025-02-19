def get_zat(pairs):
    return list(map(lambda x: (min(x), max(x)), pairs))

pairs = [(-54, -40), (-50, -42), (36, 77), (49, 100)]
min_zat = get_zat(pairs)[0][1]
print(min_zat) 