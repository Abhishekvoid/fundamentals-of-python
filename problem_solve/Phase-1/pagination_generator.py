"""
Pagination Generator
Problem:
    - Given a list and page size
    - Yield pages one at a time

Hint: generator + slicing
"""

def pagination(items, page_size):

    for i in range(0, len(items), page_size):
        yield items[i:i + page_size]
    



pagining = pagination([1,2,3,4,5,6], 2)
print(next(pagining))
print(next(pagining))
print(next(pagining))

