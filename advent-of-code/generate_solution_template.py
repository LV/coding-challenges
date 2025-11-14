"""
Generates a C++ solution template for a given year and day
"""

from datetime import datetime
from pathlib import Path
import sys


def generate_source_file_text(year: int, day: int) -> str:
    return f"""#include <cassert>
#include <filesystem>
#include <iostream>
#include <stdexcept>

#include "utils.hpp"

int solve_p1() {{
    return 0;
}}

int solve_p2() {{
    return 0;
}}

void test_p1() {{
    assert(solve_p1() == 0);
}}

void test_p2() {{
    assert(solve_p2() == 0);
}}

int main() {{
    std::filesystem::path inputFile = std::filesystem::path(__FILE__).parent_path().parent_path().parent_path() / "inputs" / "{year}" / "day{day:02d}.txt";

    test_p1();
    test_p2();

    std::cout << "Advent of Code: {year} Day {day:02d}\\n";
    std::cout << "Part 1: " << solve_p1() << "\\n";
    std::cout << "Part 2: " << solve_p2() << "\\n";
    return 0;
}}
"""


def write_contents_to_file(year: int, day: int, contents: str) -> None:
    src_path: Path = Path("src") / str(year)
    src_path.mkdir(parents=True, exist_ok=True)

    file_path: Path = src_path / f"day{day:02d}.cpp"
    if file_path.exists():
        print(f"Error: {file_path} already exists. Not overwriting.")
        sys.exit(1)
    _ = file_path.write_text(contents)


def main() -> None:
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <YEAR> <DAY>")
        sys.exit(1)

    year: int = int(sys.argv[1])
    if year < 2015:
        print(f"Specified year {year} is before earliest AoC event (2015)")
        sys.exit(1)
    if year > datetime.now().year:
        print(f"Specified year {year} is in the future")
        sys.exit(1)

    day: int = int(sys.argv[2])
    if day < 1:
        print(f"Specified day {day} is not positive")
        sys.exit(1)
    if day > 25:
        print(f"Specified day {day} is more than the maximum AoC days (25)")
        sys.exit(1)

    contents: str = generate_source_file_text(year, day)
    write_contents_to_file(year, day, contents)
    print(f"Generated solution template: src/{year}/day{day:02d}.cpp")


if __name__ == "__main__":
    main()
