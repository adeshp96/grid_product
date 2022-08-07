# Grid Product

* Grid Product is a Python library that computes the maximum product for a contiguous sequence of numbers from a grid
* `GridProduct` Python class provides the interface.
* `requirements.txt` provided for quick and easy setup of environment
* Type hints are added to all methods. Code has been processed through code formatter (`black`), `isort` and type checked using `mypy`.
## How to run?
Please ensure Python >= 3.7 is installed

```bash
$ ./grid_product.py TechConsultingTestGrid.csv --contiguous-integers 3
Greatest product is 667755
Number of combinations is 288
```
## Interface
```python
from grid_product import GridProduct
grid_product = GridProduct()
# Output: 72
print(grid_product.find_greatest_product_of_contiguous_integers([[1, 2, 3], [7, 8, 9]], 2))
 # Output: 11
print(grid_product.compute_number_of_combinations([[1, 2, 3], [7, 8, 9]], 2))
```
* `GridProduct::find_greatest_product_of_contiguous_integers(grid, contiguous_integers)` returns the greatest product of `contiguous_integers` adjacent numbers in the same direction.
* `GridProduct::compute_number_of_combinations(grid, contiguous_integers)` returns the number of different combinations possible of `contiguous_integers` adjacent numbers in the same direction.
## Tests
```bash
$ pip install -r requirements.txt
$ pytest -v tests.py
tests.py::TestBasic::test_minimal PASSED
tests.py::TestBasic::test_horizonal PASSED
tests.py::TestBasic::test_vertical PASSED
tests.py::TestBasic::test_diagonal PASSED
tests.py::TestRobustness::test_incorrect_type PASSED
tests.py::TestRobustness::test_different_row_lengths PASSED
tests.py::TestRobustness::test_empty PASSED
tests.py::TestRobustness::test_non_positive_contiguous_integer PASSED
tests.py::TestRobustness::test_contiguous_integer_bigger_than_row_and_column PASSED
tests.py::TestLarge::test_sample PASSED
tests.py::TestLarge::test_large PASSED
tests.py::TestComputeNumberOfCombinations::test_basic PASSED
tests.py::TestComputeNumberOfCombinations::test_invalid_contiguous_integers PASSED
tests.py::TestComputeNumberOfCombinations::test_sample PASSED
```