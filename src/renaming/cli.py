import typer
from .renamer import rename

app = typer.Typer()
app.command()(rename)

if __name__ == "__main__":
    app()