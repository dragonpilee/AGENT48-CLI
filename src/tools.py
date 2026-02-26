import os
import subprocess
from rich.console import Console

console = Console()

def list_dir(path: str = "/workspace"):
    """List files in a directory."""
    try:
        items = os.listdir(path)
        return "\n".join(items)
    except Exception as e:
        return f"Error: {str(e)}"

def read_file(filepath: str):
    """Read content of a file."""
    try:
        # Resolve path relative to /workspace if not absolute
        if not os.path.isabs(filepath):
            filepath = os.path.join("/workspace", filepath)
            
        with open(filepath, "r") as f:
            return f.read()
    except Exception as e:
        return f"Error: {str(e)}"

def write_file(filepath: str, content: str):
    """Write content to a file."""
    try:
        if not os.path.isabs(filepath):
            filepath = os.path.join("/workspace", filepath)
            
        # Ensure directory exists
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
            
        with open(filepath, "w") as f:
            f.write(content)
        return f"Successfully wrote to {filepath}"
    except Exception as e:
        return f"Error: {str(e)}"

import click

def execute_command(command: str):
    """Execute a shell command."""
    try:
        if not click.confirm(f"\n[bold red]PERMISSION REQUIRED[/bold red]: Execute command '[cyan]{command}[/cyan]'?", default=True):
            return "Command execution cancelled by user."
            
        result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd="/workspace")
        output = result.stdout
        if result.stderr:
            output += f"\nErrors:\n{result.stderr}"
        return output if output else "Command executed (no output)"
    except Exception as e:
        return f"Error: {str(e)}"

def search_files(pattern: str, path: str = "/workspace"):
    """Search for a pattern in files within a directory."""
    try:
        # Use grep -rn if available, otherwise fallback to python
        result = subprocess.run(['grep', '-rn', pattern, path], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
        elif result.returncode == 1:
            return "No matches found."
        else:
            return f"Error: {result.stderr}"
    except Exception as e:
        return f"Error: {str(e)}"

# Tool definitions for Ollama
TOOLS = [
    {
        'type': 'function',
        'function': {
            'name': 'list_dir',
            'description': 'List files and directories in a given path (defaults to /workspace)',
            'parameters': {
                'type': 'object',
                'properties': {
                    'path': {'type': 'string', 'description': 'The directory path to list'}
                }
            }
        }
    },
    {
        'type': 'function',
        'function': {
            'name': 'search_files',
            'description': 'Search for a pattern/string in files (like grep)',
            'parameters': {
                'type': 'object',
                'properties': {
                    'pattern': {'type': 'string', 'description': 'The text or regex pattern to search for'},
                    'path': {'type': 'string', 'description': 'The directory to search in'}
                },
                'required': ['pattern']
            }
        }
    },
    {
        'type': 'function',
        'function': {
            'name': 'read_file',
            'description': 'Read the contents of a file',
            'parameters': {
                'type': 'object',
                'properties': {
                    'filepath': {'type': 'string', 'description': 'Path to the file to read'}
                },
                'required': ['filepath']
            }
        }
    },
    {
        'type': 'function',
        'function': {
            'name': 'write_file',
            'description': 'Write or update a file with specific content',
            'parameters': {
                'type': 'object',
                'properties': {
                    'filepath': {'type': 'string', 'description': 'Path to the file to write'},
                    'content': {'type': 'string', 'description': 'Content to write to the file'}
                },
                'required': ['filepath', 'content']
            }
        }
    },
    {
        'type': 'function',
        'function': {
            'name': 'execute_command',
            'description': 'Execute a shell command in the /workspace directory',
            'parameters': {
                'type': 'object',
                'properties': {
                    'command': {'type': 'string', 'description': 'Terminal command to run'}
                },
                'required': ['command']
            }
        }
    }
]

# Map tool names to Python functions
TOOL_MAP = {
    'list_dir': list_dir,
    'search_files': search_files,
    'read_file': read_file,
    'write_file': write_file,
    'execute_command': execute_command,
}
