import click
from rich.console import Console
from rich.panel import Panel
from .agent import Agent48

console = Console()

AGENT48_ART = """
      .---.
     /     \\
    | () () |
     \\  ^  /
      |||||
      |||||
"""

@click.command()
@click.option('--model', default='granite4:3b', help='Ollama model to use')
def main(model):
    console.print(Panel(f"[bold red]{AGENT48_ART}[/bold red]\n[bold white]AGENT 48[/bold white]\n[dim]Surgical Precision Coding[/dim]", expand=False))
    console.print(f"Target Acquired: [cyan]{model}[/cyan]")
    
    agent = Agent48(model=model)
    
    while True:
        try:
            query = click.prompt("\n[bold red]MISSION[/bold red] >")
            if query.lower() in ['exit', 'quit', 'bye']:
                break
            
            console.print("\n[bold green]Response:[/bold green]")
            for chunk in agent.chat(query):
                console.print(chunk, end="")
            console.print("\n")
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {e}")

if __name__ == "__main__":
    main()
