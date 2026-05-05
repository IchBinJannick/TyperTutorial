import typer

#CLI arguments (necessary) no default value
#CLI otpion (unnecessary) have default value
def main(name: str, lastname: str = "", formal: bool = False):
    """
    Say hi to NAME, optionally with a --lastname.
    If --formal is used, say hi very formally.
    """
    if formal:
        print(f"Greetings, {name} {lastname}")
    else:
        print(f"Hello {name} {lastname}")

if __name__ == "__main__":
    typer.run(main)