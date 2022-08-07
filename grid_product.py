#!/usr/bin/env python

import sys
from argparse import ArgumentParser
from typing import List, Optional, Tuple


class GridProduct:
    INT_MIN = -sys.maxsize

    def find_greatest_product_of_contiguous_integers(
        self, grid: List[List[int]], contiguous_integers: int
    ) -> int:
        """
            Returns the greatest product of `contiguous_integers` adjacent numbers
            in the same direction.
            Simplifies finding combinations by reducing search space by considering
            combinations where the current cell is at top/left most position.
        """
        self._assert_grid_and_contiguous_integer_valid(grid, contiguous_integers)

        # All combinations can be simplified by considering to start the combination
        # only from the top/left most cell in the combination.
        # Create relative co-ordinates of cells in combination wrt the top/left most cell
        increment_different_directions = [
            (0, 1),  # right
            (1, 0),  # down
            (1, -1),  # down left
            (1, 1),  # down right
        ]

        m, n = len(grid), len(grid[0])
        max_product = GridProduct.INT_MIN
        for start_x in range(m):
            for start_y in range(n):
                # Compute all the products in various directions
                for increment_x, increment_y in increment_different_directions:
                    product = self._compute_product(
                        start_x,
                        start_y,
                        increment_x,
                        increment_y,
                        grid,
                        contiguous_integers,
                    )
                    max_product = max(max_product, product)
        # We already checked constraints earlier so this will have some legitimate value
        return max_product

    def compute_number_of_combinations(
        self, grid: List[List[int]], contiguous_integers: int
    ) -> int:
        """
            Compute total number of combintions (down, right, left, up or diagonally)
            for a given contiguous_integers
        """
        self._assert_grid_and_contiguous_integer_valid(grid, contiguous_integers)

        m, n = len(grid), len(grid[0])

        # All combinations can be simplified by considering to start the combination
        # only from the top/left most cell in the combination.
        horizontal_combinations = max(0, m * (n - contiguous_integers + 1))
        vertical_combinations = max(0, n * (m - contiguous_integers + 1))
        first_diagonal_combinations = max(
            0, (m - contiguous_integers + 1) * (n - contiguous_integers + 1)
        )
        second_diagonal_combinations = first_diagonal_combinations

        return (
            horizontal_combinations
            + vertical_combinations
            + first_diagonal_combinations
            + second_diagonal_combinations
        )

    def _is_valid(self, i: int, j: int, m: int, n: int):
        """
            Helper method to check if a cell lies inside the grid
            Returns True or False
        """
        if i < 0 or i >= m or j < 0 or j >= n:
            return False
        return True

    def _compute_product(
        self,
        start_x: int,
        start_y: int,
        increment_x: int,
        increment_y: int,
        grid: List[List[int]],
        contiguous_integers: int,
    ) -> int:
        """
            Helper method to compute the product of a combination in the grid
            Returns the maximum product from this combination starting from this cell
        """
        product = 1
        m, n = len(grid), len(grid[0])
        for i in range(contiguous_integers):
            absolute_x = start_x + i * increment_x
            absolute_y = start_y + i * increment_y
            if self._is_valid(absolute_x, absolute_y, m, n):
                product *= grid[absolute_x][absolute_y]
            else:
                return GridProduct.INT_MIN
        return product

    def _assert_grid_and_contiguous_integer_valid(
        self, grid: List[List[int]], contiguous_integers: int
    ) -> None:
        """
            Verify various constraints for the grid and contiguous integers such as:
            - Type of grid must be list
            - Grid must not be empty
            - Length of all rows must be same
            - contiguous_integers must be int, non-negative and less than #rows and #cols
            Raise appropriate exception if constraint violated
        """
        # Check grid constraints
        if type(grid) != list:
            raise TypeError(f"Invalid type of grid: {type(grid)}")
        if len(grid) == 0:
            raise ValueError(f"Empty grid {grid}")

        m, n = len(grid), len(grid[0])
        if n == 0:
            raise ValueError(f"Empty grid {grid}")

        # Check inside grid
        for row in grid:
            if len(row) != n:
                raise ValueError(f"Varying row length, {n} vs {len(row)}")

        # Check constraints of contiguous_integers
        if type(contiguous_integers) != int:
            raise TypeError(
                f"Invalid type of contiguous_integers: {type(contiguous_integers)}"
            )
        if contiguous_integers > max(m, n) or contiguous_integers <= 0:
            raise ValueError(
                f"contiguous_integers {contiguous_integers} invalid. # rows ({m}) and"
                " # columns ({n})"
            )


if __name__ == "__main__":
    parser = ArgumentParser(description="Find maximum product in a grid")
    parser.add_argument("csvpath", type=str, help="csv where grid is present")
    parser.add_argument(
        "--contiguous-integers",
        type=int,
        default=3,
        help="Number of integers to consider for product",
        required=False,
    )
    args = parser.parse_args()
    grid = []
    try:
        with open(args.csvpath, encoding="utf-8-sig") as fp:
            for line in fp:
                row = [int(number) for number in line.strip().split(",")]
                grid.append(row)
    except OSError:
        print(f"Cannot open file {args.csvpath}")
        raise
    grid_product = GridProduct()
    print(
        f"Greatest product is "
        f"{grid_product.find_greatest_product_of_contiguous_integers(grid, args.contiguous_integers)}"
    )
    print(
        f"Number of combinations is "
        f"{grid_product.compute_number_of_combinations(grid, args.contiguous_integers)}"
    )
