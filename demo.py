from package_sorter import sort

def demo():
    test_cases = [
        (50, 50, 50, 10, "Standard package"),
        (100, 100, 100, 15, "Standard package with larger volume"),
        (150, 50, 50, 10, "Bulky package (one dimension >= 150)"),
        (50, 50, 50, 20, "Heavy package (mass >= 20)"),
        (150, 50, 50, 20, "Rejected package (both bulky and heavy)"),
        (100, 100, 100, 20, "Rejected package (volume >= 1M and heavy)"),
        (149, 149, 149, 19, "Edge case - just under limits"),
        (150, 149, 149, 19, "Edge case - just over dimension limit"),
        (149, 149, 149, 20, "Edge case - just over mass limit")
    ]
    
    print("Package Sorting Demo")
    print("=" * 50)
    
    for width, height, length, mass, description in test_cases:
        result = sort(width, height, length, mass)
        volume = width * height * length
        print(f"Package: {width}x{height}x{length} cm, {mass} kg (Volume: {volume:,} cm³)")
        print(f"Description: {description}")
        print(f"Result: {result}")
        print("-" * 50)

if __name__ == "__main__":
    demo() 