# pytest_Learning
All Stuff related to Pytest Installation to Implementation

# Instructor git repo link:
https://github.com/AutomationPanda/tau-intro-to-pytest

# Setup: Install Python:
python --version

# Install Pytest:
https://docs.pytest.org/
pytest a Third party package not a part of python standard libray

# Python Packages:
This course will use a handful of third-party packages:
1. pytest
2. pytest-cov
3. pytest-html
4. pytest-xdist
5. requests
6. playwright

These packages are not part of the Python Standard Library. They must be installed separately using pip, the standard Python package installer. You can install them all before you create your test project, or you can install them as you complete each chapter in the course.
cmd: pip install pytest

# Create New Python Project
create a project directory
create a test directory and create all test file in it

# Write first Test Case
Naming conventions are important to pytest. Notice that both our test module and our test function contain the prefix 
"test_". When pytest runs, it will discover tests from its current directory down. By default, any function names with 
the prefix "test_" in any modules with the prefix "test_" will be identified and executed as test cases. 

# Run Tests using command:
1. python -m pytest
2. python -m pytest --help
3. "python -m pytest --verbose" OR "python -m pytest -v"
By Running this command pytest will print every test path along with Passed OR Failed Status
if test failed then its code will also print (print failure introspection)

4. python -m pytest --quite
This command will show only dots and F for pass and failed tests respectively. also it will
display code of failed tests (print failure introspection)

5. "python -m pytest --exitfirst" OR "python -m pytest --maxfail=1"
This command will stop executing test on first failed 

6. python -m  pytest -v .\tests\test_calculator.py 
7. python -m  pytest -v .\tests\test_math.py::test_one_plus_one
The above 6 and 7 command run the specific test case

8. python -m  pytest -v -k multi 
Run all the testcases that contains function name 'multi'

# -- pytest Marker --
in "pytest.ini" file add without quotes
"[pytest]
markers = 
    accumulator
    math"

and add decorator "@pytest.mark.math" and "@pytest.mark.accumulator" in the testcases that you want for 
math and accumulator

# How to Run Marker Testcases?
>>>>>> python -m pytest -v -m math
>>>>>> python -m pytest -v -m accumulator
Note: Use -m with marker name

10. -- plugins ---
1. pytest-html 
   > install pytest-html using command "pip install pytest-html"
   > Generate Report.html file using command "python -m pytest --html=report.html"

2. pytest.cov
   1. install pytest-html using command "pip install pytest-cov"
   2. python -m pytest --cov=stuff
   3. python -m pytest --cov=stuff --cov=tests
   4. To generate HTML Report:: "python -m pytest --cov=stuff --cov-report html"
   5. python -m pytest --cov=stuff --cov-branch
   6. python -m pytest --cov=stuff --cov-branch --cov-report html 
Note::
   By default, coverage.py will do line-by-line coverage, but it won’t cover any conditionals or branching 
   that happens in your code. So, by testing branch coverage, you’re really getting 
   the most out of your coverage report. Typically, I recommend adding branching as a default option.
   
3. pytest.sdist
   Running tests in parallel is a great way to reduce the total start-to-end execution time for test suites. 
   The pytest-xdist plugin lets you run pytest tests in parallel. 
   To install it, run the following terminal command: "pip install pytest-xdist"
   Command: python -m pytest -n 3
   Using pytest-xdist is simple. Just add the -n option with the number of threads to run. For example, -n 3 will run tests across three parallel threads.
Note: 
   Be careful when trying to run tests in parallel though. Test cases must be independent, 
   meaning they cannot share any resources or data. Otherwise, they could collide and cause each other to fail. 
   Test machines and test environments must also be powerful enough to handle multiple tests for it. 
   If you aren't careful, you may try to run more tests than your system can effectively handle. 
   pytest-xdist also lets you distribute test execution across multiple machines using SSH or sockets.

4. >>>>>> pytest.bdd
   > 
