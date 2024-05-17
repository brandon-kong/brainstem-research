def count(d):
    return sum([count(v) if isinstance(v, dict) else 1 for v in d.values()])