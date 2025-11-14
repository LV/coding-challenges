CXX = g++
CXXFLAGS = -std=c++23 -I./src
BUILD_DIR = build

# Pads a `0` if the provided day only has a single digit
PADDED_DAY := $(shell printf "%02d" $(DAY))

.PHONY: help
help:
	@echo "Advent of Code Makefile"
	@echo ""
	@echo "Usage:"
	@echo "  make run YEAR=<year> DAY=<day>  Compile and run a specific day's solution"
	@echo "  make clean                      Remove all build artifacts"
	@echo ""
	@echo "Example:"
	@echo "  make run YEAR=2015 DAY=01"

run:
ifndef YEAR
	$(error YEAR is not set. Usage: make run YEAR=2015 DAY=01)
endif
ifndef DAY
	$(error DAY is not set. Usage: make run YEAR=2015 DAY=01)
endif
	@mkdir -p $(BUILD_DIR)/$(YEAR)
	@$(CXX) $(CXXFLAGS) src/$(YEAR)/day$(PADDED_DAY).cpp -o $(BUILD_DIR)/$(YEAR)/day$(PADDED_DAY)
	@./$(BUILD_DIR)/$(YEAR)/day$(PADDED_DAY)

clean:
	rm -rf $(BUILD_DIR)

.PHONY: format
format:
	find src \( -name '*.cpp' -o -name '*.h' \) -exec clang-format -i {} +
	find src \( -name '*.cpp' -o -name '*.h' \) -exec clang-tidy {} -- $(CXXFLAGS) \;
