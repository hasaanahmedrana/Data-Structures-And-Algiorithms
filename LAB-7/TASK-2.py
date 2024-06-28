import math
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
    "Mulberry",
    "Nashi Pear",
    "Navel Orange",
    "Nectarine",
    "Ogeechee Limes",
    "Olive",
    "Oranges",
    "Oval Kumquat",
    "Papaya",
    "Paw Paw",
    "Peach",
    "Pineapple",
    "Pomegranate",
    "Prickly Pear",
    "Quararibea cordata",
    "Queen Anne Cherry",
    "Quince",
    "Rambutan",
    "Raspberries",
    "Star Fruit",
    "Strawberries",
    "Sugar Baby Watermelon",
    "Tamarind",
    "Tangerine",
    "Tart Cherries",
    "Tomato",
    "Ugni",
    "Uniq Fruit",
    "Vanilla Bean",
    "Velvet Pink Banana",
    "Voavanga",
    "Watermelon",
    "White Mulberry",
    "Wolfberry",
    "Xango Mangosteen",
    "Xigua",
    "Ximenia caffra fruit",
    "Yangmei",
    "Yellow Passion Fruit",
    "Yunnan Hackberry",
    "Zig Zag Vine fruit",
    "Zinfandel Grapes",
    "Zucchini"
]
vals = []

# def hash_function(fruit):
#     hash_val = 0
#     for i in fruit:
#         hash_val = (ord(i) +hash_val*31) % (10**9+7)
#     return hash_val

# def hash_function(fruit):
#     return (sum([ord(i) % len(fruit) for i in fruit]) + len(fruit)+(sum([ord(i) for i in fruit])))

# def hash_function(fruit):
#     return (sum([ord(i) % len(fruits) for i in fruit]) + len(fruit)* 93)


# def hash_function(fruit):
#     return sum([ord(i)%math.pi for i in fruit]) * len(fruits)
#

def hash_function(fruit):
    h = 0
    for each in fruit:
        h = ord(each) *(h*31) %(10**(9)+7)
    return h

for each in fruits:
    vals.append(hash_function(each))

print(vals)
print(max(vals))
print(len(set(vals)), len(fruits))