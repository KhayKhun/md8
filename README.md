floating-point precision error

Solutions
1. use abs
2. use decimal library in python
3. use math.isclose() or `diff < 1e-10`, `print(math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-9))`
4. 