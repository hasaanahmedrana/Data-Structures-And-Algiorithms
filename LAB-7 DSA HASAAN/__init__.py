def xor_of_fruits(fruits):
    xor_results = []
    for fruit in fruits:
        xor_result = 0
        for char in fruit:
            xor_result ^= ord(char)
        xor_results.append(bin(xor_result))
    return xor_results

fruits = [
    "Apples",
    "Apricots",
    "Avocados",
    "Bananas",
    "Bing Cherry",
    "Blueberries",
    "Boysenberries",
    "Cantaloupe",
    "Cherries",
    "Clementine",
    "Crab apples",
    "Cucumbers",
    "Damson plum",
    "Dates",
    "Dewberries",
    "Dinosaur Eggs",
    "Dragon Fruit",
    "Eggfruit",
    "Elderberry",
    "Entawak",
    "Evergreen Huckleberry",
    "Farkleberry",
    "Fig",
    "Finger Lime",
    "Gooseberries",
    "Grapefruit",
    "Guava",
    "Hackberry",
    "Honeycrisp Apples",
    "Imbe",
    "Indonesian Lime",
    "Jackfruit",
    "Jambolan",
    "Java Apple",
    "Kaffir Lime",
    "Kiwi",
    "Kumquat",
    "Lime (Lemon)",
    "Longan",
    "Loquat",
    "Lychee",
    "Mango",
    "Melon",
    "Mulberry"
]

print(len(set(xor_of_fruits(fruits))))

