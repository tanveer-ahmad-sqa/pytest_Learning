# pytest_Learning
All Stuff related to Pytest Installation to Implementation

# (Instructor git repo link:)
https://github.com/AutomationPanda/tau-intro-to-pytest

# (Setup:)
Install Python:
===============
python --version

Install Pytest:
===============
https://docs.pytest.org/
pytest a Third party package not a part of python standard libray

Python Packages:
================
This course will use a handful of third-party packages:
1. pytest
2. pytest-cov
3. pytest-html
4. pytest-xdist
5. requests
6. playwright
These packages are not part of the Python Standard Library. They must be installed separately using pip, the standard Python package installer. You can install them all before you create your test project, or you can install them as you complete each chapter in the course.
cmd: pip install pytest

Create New Python Project
=========================
create a project directory
create a test directory and create all test file in it

Write first Test Case
=====================
Naming conventions are important to pytest. Notice that both our test module and our test function contain the prefix 
"test_". When pytest runs, it will discover tests from its current directory down. By default, any function names with 
the prefix "test_" in any modules with the prefix "test_" will be identified and executed as test cases. 

Run Tests using command:
=======================
python -m pytest
