from blessed import Terminal

term = Terminal()

fruits = {
    "apple": term.red,
    "banana": term.yellow,
    "cherry": term.dark_red,
    "grape": term.blue,
    "mango": term.magenta,
    "orange": term.darkorange,
    "peach": term.coral
}

for fruit, color in fruits.items():
    print(color + fruit + term.normal)
