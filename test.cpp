#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <memory>
using namespace std;

auto generate_random_numbers(size_t count) {
    auto numbers = std::make_unique<std::vector<int>>();
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> dist(1, 100);

    for (size_t i = 0; i < count; ++i) {
        numbers->push_back(dist(gen));
    }
    return numbers;
}

int main() {
    constexpr size_t count = 10;
    auto numbers = generate_random_numbers(count);

    std::cout << "Nombres générés : ";
    for (auto num : *numbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    std::sort(numbers->begin(), numbers->end());

    std::cout << "Nombres triés : ";
    for (auto num : *numbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}