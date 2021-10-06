# Pytest intro session

Code Clinic session in which we wrote tests for a simple car class.

Look through the commit history to see how we actually caught some bugs in the `Car` class. I am glad it happened because it showed the power and importance of testing your code.

After the demo I added better names to the fixtures.

## Setup and run test

```
√ cars (main) $ make setup
√ cars (main) $ source venv/bin/activate
(venv) √ cars (main) $ make cov
pytest --cov=cars --cov-report term-missing
======================================================== test session starts =========================================================
platform darwin -- Python 3.7.9, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /Users/bbelderbos/Downloads/cars/cars
plugins: cov-3.0.0
collected 7 items

tests/test_cars.py .......                                                                                                     [100%]

---------- coverage: platform darwin, python 3.7.9-final-0 -----------
Name               Stmts   Miss  Cover   Missing
------------------------------------------------
cars/__init__.py       0      0   100%
cars/cars.py          22      0   100%
------------------------------------------------
TOTAL                 22      0   100%


========================================================= 7 passed in 0.06s ==========================================================
```
