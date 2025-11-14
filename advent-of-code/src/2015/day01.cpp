#include <cassert>
#include <filesystem>
#include <iostream>
#include <stdexcept>

#include "utils.hpp"

int solve_p1(std::string input) {
    int floor = 0;
    for (char c : input) {
        if (c == '(') {
            ++floor;
        }
        if (c == ')') {
            --floor;
        }
    }
    return floor;
}

int solve_p2(std::string input) {
    int floor = 0;
    for (int i = 0; i < input.size(); i++) {
        if (input[i] == '(') {
            ++floor;
        }
        if (input[i] == ')') {
            --floor;
        }
        if (floor == -1) {
            return i + 1;
        }
    }
    throw std::runtime_error("No valid solution found in input (unexpected end of file).");
}

void test_p1() {
    assert(solve_p1("(())") == 0);
    assert(solve_p1("()()") == 0);
    assert(solve_p1("(((") == 3);
    assert(solve_p1("(()(()(") == 3);
    assert(solve_p1("))(((((") == 3);
    assert(solve_p1("())") == -1);
    assert(solve_p1("))(") == -1);
    assert(solve_p1(")))") == -3);
    assert(solve_p1(")())())") == -3);
}

void test_p2() {
    assert(solve_p2(")") == 1);
    assert(solve_p2("()())") == 5);
}

int main() {
    std::filesystem::path inputFile = std::filesystem::path(__FILE__).parent_path().parent_path().parent_path() / "inputs" / "2015" / "day01.txt";

    test_p1();
    test_p2();

    std::cout << "Advent of Code: 2015 Day 01\n";
    std::cout << "Part 1: " << solve_p1(read_file_to_string(inputFile)) << "\n";
    std::cout << "Part 2: " << solve_p2(read_file_to_string(inputFile)) << "\n";
    return 0;
}
