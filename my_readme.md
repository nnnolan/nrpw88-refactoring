# Please see nrpw88 Refactoring Document.pdf in my dir to see more details! 
*** 
## Build Instructions

Install: `pip install -r requirements.txt`
Run all tests from this directory using `python -m pytest -v`

***
## Test Results

Initial test after first build
```
base) nolanpestano@Nolans-MacBook-Pro-2 python % python -m pytest -v
================================== test session starts ===================================
platform darwin -- Python 3.11.5, pytest-9.1.1, pluggy-1.7.0 -- /Users/nolanpestano/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/nolanpestano/Documents/GitHub/nrpw88-refactoring/python
configfile: pytest.ini
testpaths: tests
plugins: approvaltests-0.2.4, anyio-3.5.0, dash-3.2.0, approvaltests-20.0.1
collected 2 items                                                                        

tests/test_statement.py::test_example_statement PASSED                             [ 50%]
tests/test_statement.py::test_statement_with_new_play_types PASSED                 [100%]

=================================== 2 passed in 0.03s ===================================
```

Tests after midpoint
```
base) nolanpestano@Nolans-MacBook-Pro-2 python % python -m pytest -v
================================== test session starts ===================================
platform darwin -- Python 3.11.5, pytest-9.1.1, pluggy-1.7.0 -- /Users/nolanpestano/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/nolanpestano/Documents/GitHub/nrpw88-refactoring/python
configfile: pytest.ini
testpaths: tests
plugins: approvaltests-0.2.4, anyio-3.5.0, dash-3.2.0, approvaltests-20.0.1
collected 4 items                                                                        

tests/test_characterization.py::test_tragedy_charge_and_credits_around_30_seat_threshold PASSED [ 25%]
tests/test_characterization.py::test_comedy_charge_around_20_seat_threshold PASSED [ 50%]
tests/test_statement.py::test_example_statement PASSED                             [ 75%]
tests/test_statement.py::test_statement_with_new_play_types PASSED                 [100%]
```

Tests with Historical
```
base) nolanpestano@Nolans-MacBook-Pro-2 python % python -m pytest -v
================================== test session starts ===================================
platform darwin -- Python 3.11.5, pytest-9.1.1, pluggy-1.7.0 -- /Users/nolanpestano/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/nolanpestano/Documents/GitHub/nrpw88-refactoring/python
configfile: pytest.ini
testpaths: tests
plugins: approvaltests-0.2.4, anyio-3.5.0, dash-3.2.0, approvaltests-20.0.1
collected 4 items                                                                        

tests/test_characterization.py::test_tragedy_charge_and_credits_around_30_seat_threshold PASSED [ 25%]
tests/test_characterization.py::test_comedy_charge_around_20_seat_threshold PASSED [ 50%]
tests/test_statement.py::test_example_statement PASSED                             [ 75%]
tests/test_statement.py::test_statement_with_new_play_types PASSED                 [100%]
```


My tests I wrote for the existing behavior:     
test_tragedy_charge_and_credits_around_30_seat_threshold: checks a tragedy at 30 vs 31 seats, confirming the $10 per seat surcharge and volume credits begin only above 30 seats.
test_comedy_charge_around_20_seat_threshold: checks a comedy at 20 vs 21 seats, confirming the $100 sum and $5 per extra seat begin only above 20 seats.

Both passed against the original code and still pass after refactoring.

Tests for historical 
test_spec_example_35_seats: I tested the assignment's example ($725.00, 7 credits). It also guards against accidentally adding the base over-30 credit.
test_historical_boundaries: checks 20 vs 21 seats (the $15-per-seat surcharge starts above 20) and 4 vs 5 seats (the first credit is earned at 5). This is 4 tests in one!

***
## Reflection

I had a lot of fun with this assignment! This forced me to think about some neat parts of software and real development that is out of the scope of every other class I've taken so far.

Replacing conditonal behavior with polmyorphism improved the layout the most. Before it, the rules for one play type were split across two if/elif chains, one for the amount and one for volume credits. Afterward, each play type's rules live together in one small class, and a new type means adding a class instead of editing a long function.

One thing to note, my kneejerk instinct was not to build a class hierarchy. Realistically, I would've considered anything about a class to be overkill for this scenario, and my first two refactors were just nested functions in one file. Polymorphism came from an AI, which tends to jump straight to the textbook end state, while a human tends to solve the problem at hand and add structure once it hurts. With only two play types, the if/elif chain is arguably fine. The hierarchy paid off once a third type arrived, so my takeaway is to use polymorphism when variants are likely to grow, not by default.

Refactoring differs from adding functionality because it must not change observable behavior, while a feature changes it on purpose. I wrote characterization tests against the original code first, and during each refactoring commit the only acceptable result was the same tests passing unchanged. Historical plays got new tests and their own commit, so the history shows the refactoring commits contain no behavior change.

The design made historical plays easy: one new subclass and one line in the CALCULATORS registry, with no changes to statement(), the totals, or the other types. The one catch was credits. The base class gives one credit per seat over 30, but the spec's 35-seat example expects 7 credits, not 12, so HistoricalCalculator overrides the credit rule instead of extending it.

Most of the original issues were resolved. The one function doing everything now only coordinates and formats, the play type is no longer checked in two places, the misleading "every ten" comment is fixed, and the mutable accumulators became computed totals. Magic numbers remain as literals inside each class; naming them as constants would be a next step.

***

## Generative AI Disclosure

I used Claude's assistance with this assignement. I started off by finding the isseus and the first two refatorings, but after that it was Claude's idea and assistance to write the polymorphism. I ran the tests, reviewed each commit, and I am responsible for the submitted code. 

***
[Github Link](https://github.com/nnnolan/nrpw88-refactoring.git)