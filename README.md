# 🐍 Python Fundamentals — 400-Day Solana Journey
**Days 1–30 | Phase 1**

Learning Python basics as the foundation for becoming a Solana developer.

---

## 📅 Progress

| Day | Topic | File(s) | Score | Status |
|-----|-------|---------|-------|--------|
| Day 1 | Environment Setup, Hello World & Variables | `day01_hello.py` | ✅ | Done |
| Day 2 | Variables & Data Types | `day_02_Variables_&_Data_Type.py` | 10/10 🎯 | Done |
| Day 3 | Operators, Strings & User Input | `day_03_calculator.py` `day_03_word_reverser.py` | 10/10 🎯 | Done |


---

## 📁 Files

- `day01_hello.py` — Hello World + variables + print()
- `day_02_Variables_&_Data_Type.py` — int, float, str, bool · type() · f-string alignment
- `day_03_calculator.py` — All 7 arithmetic operators + f-string column alignment
- `day_03_word_reverser.py` — String slicing `[::-1]` · `.upper()` · `len()`

---

## 💻 Day 2 Highlight — Formatted Output

```python
# my_profile
name       = "Michael Nomyongo"
age        = 25
height     = 6.9
is_student = True

# printing_type — with alignment
print(f"{'name':<12}: {name:<20} : {type(name)}")
print(f"{'age':<12}: {age:<20} : {type(age)}")
print(f"{'height':<12}: {height:<20} : {type(height)}")
print(f"{'is_student':<12}: {is_student:<20} : {type(is_student)}")
```

**Output:**
```
name        : Michael Nomyongo     : <class 'str'>
age         : 25                   : <class 'int'>
height      : 6.9                  : <class 'float'>
is_student  : True                 : <class 'bool'>
```

> 💡 Used `{value:<20}` f-string alignment — a formatting challenge conquered on Day 2!

---

## 💻 Day 3 Highlight — Calculator + Word Reverser

```python
# calculator — nested f-string alignment
num_a = float(input("Enter the first number: "))
num_b = float(input("Enter the second number: "))

print(f"\n{'Operation':<20}{'Result':<20}")
print("-" * 32)
print(f"{f'{num_a} + {num_b}':<20}{num_a + num_b}")
print(f"{f'{num_a} ** {num_b}':<20}{num_a ** num_b}")
```

```python
# word reverser — slicing trick
word = input("Enter a word: ")
reversed_word = word[::-1]   # [::-1] walks backwards through the string

print(f"Original:  {word}")
print(f"Reversed:  {reversed_word}")
print(f"Uppercase: {reversed_word.upper()}")
print(f"Length:    {len(word)} characters")
```

> 💡 Key tricks: `//` = floor division · `**` = exponentiation · `[::-1]` = string reversal

---

## 📊 Results

| Day | Assignment | Live Quiz |
|-----|-----------|-----------|
| Day 2 | 10 / 10 ✅ | 3 / 3 🏆 |
| Day 3 | 10 / 10 ✅ + Bonus ⭐ | 3 / 3 🏆 |

---

## 🔗 Part of

> [400-Day Solana Developer Journey](https://github.com/) · Michael Nomyongo  
> Python → C++ → Rust → Solana · Started March 2026

---

*Tracked & reviewed with Claude AI · Notion synced daily*
