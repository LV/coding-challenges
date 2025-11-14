CXX = g++
CXXFLAGS = -std=c++23 -I./src
BUILD_DIR = build

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
	@$(CXX) $(CXXFLAGS) src/$(YEAR)/day$(DAY).cpp -o $(BUILD_DIR)/$(YEAR)/day$(DAY)
	@./$(BUILD_DIR)/$(YEAR)/day$(DAY)

clean:
	rm -rf $(BUILD_DIR)

.PHONY: format
format:
	find src \( -name '*.cpp' -o -name '*.h' \) -exec clang-format -i {} +
	find src \( -name '*.cpp' -o -name '*.h' \) -exec clang-tidy {} -- $(CXXFLAGS) \;
