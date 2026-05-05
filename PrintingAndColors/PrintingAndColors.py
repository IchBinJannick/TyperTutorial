import typer
#rich documentaitoin: https://rich.readthedocs.io/en/stable/
from rich import print #overwriting default print

data = {
    "name": "Rick",
    "age": 42,
    "items": [{"name": "Portal Gun"}, {"name": "Plumbus"}],
    "active": True,
    "affiliation": None,
}

app = typer.Typer()

@app.command()
def main():
    print("Here's some data:")
    print(data)

if __name__ == "__main__":
    app()