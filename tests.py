import pytest

from grid_product import GridProduct


@pytest.fixture
def grid_product():
    return GridProduct()


class TestBasic:
    def test_minimal(self, grid_product):
        # Test minimal grid and contiguous integer
        assert grid_product.find_greatest_product_of_contiguous_integers([[1]], 1) == 1

    def test_horizonal(self, grid_product):
        # Ensure maximum product horizontally is picked up
        assert (
            grid_product.find_greatest_product_of_contiguous_integers(
                [[1, 2, 3], [7, 8, 9], [4, 5, 6]], 3
            )
            == 504
        )
        assert (
            grid_product.find_greatest_product_of_contiguous_integers(
                [[1, 2, 3], [9, 8, 7], [4, 5, 6]], 3
            )
            == 504
        )

    def test_vertical(self, grid_product):
        # Ensure maximum product vertically is picked up
        assert (
            grid_product.find_greatest_product_of_contiguous_integers(
                [[1, 7, 4], [2, 8, 5], [3, 9, 6]], 3
            )
            == 504
        )
        assert (
            grid_product.find_greatest_product_of_contiguous_integers(
                [[1, 9, 4], [2, 8, 5], [3, 7, 6]], 3
            )
            == 504
        )

    def test_diagonal(self, grid_product):
        # Ensure maximum product at diagonal is picked up
        assert (
            grid_product.find_greatest_product_of_contiguous_integers(
                [[7, 2, 1], [4, 8, 3], [6, 5, 9]], 3
            )
            == 504
        )
        assert (
            grid_product.find_greatest_product_of_contiguous_integers(
                [[1, 2, 9], [3, 8, 5], [7, 4, 6]], 3
            )
            == 504
        )


class TestRobustness:
    def test_incorrect_type(self, grid_product):
        # Incorrect type of grid or contiguous_integers
        with pytest.raises(TypeError):
            grid_product.find_greatest_product_of_contiguous_integers(set(), 5)
        with pytest.raises(TypeError):
            grid_product.find_greatest_product_of_contiguous_integers([[1]], "1")

    def test_different_row_lengths(self, grid_product):
        # Lengths of row is different in grid
        with pytest.raises(ValueError):
            grid_product.find_greatest_product_of_contiguous_integers([[1, 2], [1]], 1)

    def test_empty(self, grid_product):
        # No numbers present in grid
        with pytest.raises(ValueError):
            grid_product.find_greatest_product_of_contiguous_integers([], 1)
        with pytest.raises(ValueError):
            grid_product.find_greatest_product_of_contiguous_integers([[]], 1)

    def test_non_positive_contiguous_integer(self, grid_product):
        # Test contiguous_integer being zero and below
        with pytest.raises(ValueError):
            grid_product.find_greatest_product_of_contiguous_integers([[2]], 0)
        with pytest.raises(ValueError):
            grid_product.find_greatest_product_of_contiguous_integers([[2]], -1)

    def test_contiguous_integer_bigger_than_row_and_column(self, grid_product):
        # Test exception raised if contiguous_integer is more than bounds of rows and cols
        with pytest.raises(ValueError):
            grid_product.find_greatest_product_of_contiguous_integers([[1]], 20)


class TestLarge:
    def test_sample(self, grid_product):
        grid = [
            [8, 2, 22, 97, 38, 15, 0, 40, 0, 75],
            [49, 49, 99, 40, 17, 81, 18, 57, 60, 87],
            [81, 49, 31, 73, 55, 79, 14, 29, 93, 71],
            [52, 70, 95, 23, 4, 60, 11, 42, 69, 24],
            [22, 31, 16, 71, 51, 67, 63, 89, 41, 92],
            [24, 47, 32, 60, 99, 3, 45, 2, 44, 75],
            [32, 98, 81, 28, 64, 23, 67, 10, 26, 38],
            [67, 26, 20, 68, 2, 62, 12, 20, 95, 63],
            [24, 55, 58, 5, 66, 73, 99, 26, 97, 17],
            [21, 36, 23, 9, 75, 0, 76, 44, 20, 45],
        ]
        assert (
            grid_product.find_greatest_product_of_contiguous_integers(grid, 3) == 667755
        )

    def test_large(self, grid_product):
        m = 100
        n = 1000
        grid = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                grid[i][j] = i + j
        assert 1445551740720 == grid_product.find_greatest_product_of_contiguous_integers(
            grid, 4
        )


class TestComputeNumberOfCombinations:
    def test_basic(self, grid_product):
        assert (
            grid_product.compute_number_of_combinations([[1, 2, 3], [4, 5, 6]], 2) == 11
        )

    def test_invalid_contiguous_integers(self, grid_product):
        with pytest.raises(TypeError):
            grid_product.find_greatest_product_of_contiguous_integers([[1]], "1")
        with pytest.raises(ValueError):
            grid_product.find_greatest_product_of_contiguous_integers([[2]], 0)
        with pytest.raises(ValueError):
            grid_product.find_greatest_product_of_contiguous_integers([[2]], -1)
        with pytest.raises(ValueError):
            grid_product.find_greatest_product_of_contiguous_integers([[1]], 20)

    def test_sample(self, grid_product):
        grid = [
            [8, 2, 22, 97, 38, 15, 0, 40, 0, 75],
            [49, 49, 99, 40, 17, 81, 18, 57, 60, 87],
            [81, 49, 31, 73, 55, 79, 14, 29, 93, 71],
            [52, 70, 95, 23, 4, 60, 11, 42, 69, 24],
            [22, 31, 16, 71, 51, 67, 63, 89, 41, 92],
            [24, 47, 32, 60, 99, 3, 45, 2, 44, 75],
            [32, 98, 81, 28, 64, 23, 67, 10, 26, 38],
            [67, 26, 20, 68, 2, 62, 12, 20, 95, 63],
            [24, 55, 58, 5, 66, 73, 99, 26, 97, 17],
            [21, 36, 23, 9, 75, 0, 76, 44, 20, 45],
        ]
        assert grid_product.compute_number_of_combinations(grid, 3) == 288
