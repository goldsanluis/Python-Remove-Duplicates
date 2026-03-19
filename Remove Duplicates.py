def remove_duplicates(items):
    """Remove duplicates from a list while maintaining original order."""
    if not isinstance(items, list):
        raise TypeError("Input must be a list")

    seen = []
    result = []

    for item in items:
        if item not in seen:
            seen.append(item)
            result.append(item)

    return result


print(remove_duplicates([1, 2, 2, 3, 3, 3, 4]))   # [1, 2, 3, 4]
print(remove_duplicates(['a', 'b', 'a', 'c']))     # ['a', 'b', 'c']
print(remove_duplicates([1, 1, 1]))                # [1]
print(remove_duplicates(['Gold']))                     # ['Gold']
print(remove_duplicates([2, 2, 5, 21, 2005]))                           # []