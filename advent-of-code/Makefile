CXX = g++
CXXFLAGS = -std=c++23 -I./src
BUILD_DIR = build

# Pads a `0` if the provided day only has a single digit
PADDED_DAY := $(shell printf "%02d" $(DAY))
TARGET := aoc_$(YEAR)_day$(PADDED_DAY)

.PHONY: help
help:
	@echo "Advent of Code Makefile"
	@echo ""
	@echo "Usage:"
	@echo "  make run YEAR=<year> DAY=<day>  Build+run via CMake"
	@echo "  make configure                   Generate build system (CMake)"
	@echo "  make clean                       Remove build artifacts"

.PHONY: configure
configure:
	cmake -S . -B $(BUILD_DIR) -DCMAKE_EXPORT_COMPILE_COMMANDS=ON

.PHONY: run
run:
ifndef YEAR
	$(error YEAR is not set. Usage: make run YEAR=2015 DAY=01)
endif
ifndef DAY
	$(error DAY is not set. Usage: make run YEAR=2015 DAY=01)
endif
	@cmake -S . -B $(BUILD_DIR) -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
	@cmake --build $(BUILD_DIR) --target $(TARGET) --config Release
	@./$(BUILD_DIR)/$(TARGET)

.PHONY: clean
clean:
	rm -rf $(BUILD_DIR)

.PHONY: format
format:
	find src \( -name '*.cpp' -o -name '*.h' \) -exec clang-format -i {} +
	find src \( -name '*.cpp' -o -name '*.h' \) -exec clang-tidy {} -- $(CXXFLAGS) \;
