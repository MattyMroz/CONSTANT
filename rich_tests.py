from rich.progress import track
from rich.progress import Progress, TextColumn, BarColumn, TimeRemainingColumn
import time

lista = ["a", "b", "c", "d"]

# Prosty przykład z track (najprostsze rozwiązanie)
for item in track(lista, description="Przetwarzanie..."):
    time.sleep(0.1)

# Bardziej zaawansowany przykład z własnym formatowaniem
with Progress(
    TextColumn("[bold blue]{task.description}"),
    BarColumn(complete_style="green", finished_style="grey70"),
    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    TimeRemainingColumn(),
) as progress:
    task = progress.add_task("[red]Przetwarzanie...", total=len(lista))

    for item in lista:
        time.sleep(0.1)
        progress.advance(task)