# String Methods & Syntax

## Lower Method

**Syntax:**

```python
s.lower()
```

**Description:**

* Returns the string `s` as a lowercase string.
* Accepts **no parameters**.
* Returns a **lowercase version** of the string.

**Example Usage:**

```python
# Example 1: Mixed case
s = 'Hello World!'
lowered = s.lower()
print(lowered)  # Prints 'hello world!'

# Example 2: All uppercase
s = 'HELLO WORLD'
lowered = s.lower()
print(lowered)  # Prints 'hello world'
```

---

## Split Method

**Syntax:**

```python
s.split(separator)
```

**Description:**

* Splits the string into a list along whitespace or a specified separator.
* `separator` is optional. If omitted, the string is split along any whitespace.
* Returns a **list of substrings**.

**Example Usage:**

```python
# Example 1: Split along whitespace
s = 'Never gonna give you up'
split = s.split()
print(split)  # Prints ['Never', 'gonna', 'give', 'you', 'up']

# Example 2: Split along specified separator
s = 'Never-gonna-let-you-down'
split = s.split("-")
print(split)  # Prints ['Never', 'gonna', 'let', 'you', 'down']
```

---

## Join Method

**Syntax:**

```python
s.join(x)
```

**Description:**

* `s` is the **separator** placed between elements in the iterable `x`.
* Accepts one **required parameter** `x`: an iterable (like a list).
* Returns a **single string** where the elements of `x` are joined by `s`.

**Example Usage:**

```python
# Example 1: Join items in a list separated by space
lst = ['Never', 'gonna', 'run', 'around', 'and', 'desert', 'you']
joined = ' '.join(lst)
print(joined)  # Prints 'Never gonna run around and desert you'

# Example 2: Join items in a list separated by dash
lst = ['Never', 'gonna', 'make', 'you', 'cry']
joined = '-'.join(lst)
print(joined)  # Prints 'Never-gonna-make-you-cry'
```

---

## Strip Method

**Syntax:**

```python
s.strip(characters)
```

**Description:**

* Removes **whitespace** or specified **characters** from both ends of the string `s`.
* `characters` is an **optional parameter**. If omitted, whitespace is removed.
* Returns the **trimmed version** of `s`.

**Example Usage:**

```python
# Example 1: Strip whitespace
s = '       Never gonna say goodbye       '
stripped = s.strip()
print(stripped)  # Prints 'Never gonna say goodbye'

# Example 2: Strip question marks
s = '????Never gonna tell a lie and hurt you?????'
stripped = s.strip('?')
print(stripped)  # Prints 'Never gonna tell a lie and hurt you'
```
