#!/home/stasen/anaconda3/envs/atms_env/bin/python

#   N
# W   E
#   S


cells = {
    "":  " ",
    "N": "\u2579",
    "E": "\u257A",
    "S": "\u257B",
    "W": "\u2578",
    "EN": "\u2517",
    "NS": "\u2503",
    "NW": "\u251B",
    "ES": "\u250F",
    "EW": "\u2501",
    "SW": "\u2513",
    "ENS": "\u2523",
    "ENW": "\u253B",
    "NSW": "\u252B",
    "ESW": "\u2533",
    "ENSW": "\u254B"
}

def test_print_cells():
    for key, value in cells.items():
        print(key, end="")
        print_cell(key)

    print("***")
    for key, value in cells.items():
        print(key, end="")
        print_cell(key, True)

def print_cell(directions, highlight=False):
    key = "".join(sorted(directions)).upper()
    if not highlight:
        print(cells[key])
    else:
        print('\033[31m'+cells[key]+'\033[0m')

if __name__ == "__main__":
    print("""
    N
  W   E
    S
***""")
    test_print_cells()

