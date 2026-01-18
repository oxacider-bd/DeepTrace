from rich import print

def print_section(title):
    print(f"\n[bold cyan]=== {title} ===[/bold cyan]")

def print_result(data):
    for k, v in data.items():
        print(f"[green]{k}[/green]: {v}")
