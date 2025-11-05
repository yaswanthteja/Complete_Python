
### Frozenset

A `frozenset` in Python is an immutable version of a set. Unlike regular sets, you can't modify its elements after creation, making it useful for situations where you need a constant set of values.

```python
# Create a frozenset
frozen_set = frozenset([1, 2, 3, 4])

# Try to add an element (will raise an error)
# frozen_set.add(5)  # AttributeError: 'frozenset' object has no attribute 'add'

print(frozen_set)


```

`frozenset` ensures that your set remains unchanged throughout your program. Handy for keeping things constant and error-free!
