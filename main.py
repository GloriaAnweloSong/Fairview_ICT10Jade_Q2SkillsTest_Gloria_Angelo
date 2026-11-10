from pyscript import document, display

def show_symbol(e):
    document.getElementById("output").innerHTML = ""
    symbol = {
        "H": "Hydrogen",
        "He": "Helium",
        "C": "Carbon",
        "N": "Nitrogen",
        "O": "Oxygen",
        "F": "Fluorine",
        "Ne": "Neon",
        "P": "Phosphorus",
        "S": "Sulfer",
        "Cl": "Chlorine",
        "Ar": "Argon",
        "Se": "Selenium",
        "Br": "Bromine",
        "Kr": "Krypton",
        "I": "Iodine",
        "Xe": "Xenon",
        "At": "Astatine",
        "Rn": "Radon",
        "Ts": "Tennessine",
        "Og": "Oganesson"

    }

    symbol_code = document.getElementById("symbols").value

    show_symbol = symbol_code in symbol
    list_symbol = list(symbol.values())

    display("Is your Element Symbol a Nonmetal? - ", show_symbol, target="output")
    display("Num. of Nonmetals - ", len(symbol), target="output")
    display("What are the Nonmetals? ", list_symbol, target="output")

