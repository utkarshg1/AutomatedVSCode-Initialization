import os
import subprocess
import sys

def run_command(command):
    """Run a shell command and handle errors."""
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Error executing: {command}")
        sys.exit(1)

# Get user input
username = input("Please enter your GitHub username: ")
email = input("Please enter your GitHub email: ")
repo_url = input("Please enter GitHub repository link: ")

# Configure Git
run_command(f"git config --global user.name \"{username}\"")
run_command(f"git config --global user.email \"{email}\"")

# Clone repository
repo_name = "repository"
run_command(f"git clone {repo_url} {repo_name}")

# Copy requirements.txt if it exists
if os.path.exists("requirements.txt"):
    run_command(f"copy requirements.txt {repo_name}")  # Use `copy` for Windows

# Change to repository directory
os.chdir(repo_name)

# Create virtual environment
venv_dir = "venv"
run_command(f"python -m venv {venv_dir}")

# Activate virtual environment
if sys.platform == "win32":
    venv_activate = os.path.join(venv_dir, "Scripts", "activate.bat")
else:
    venv_activate = f"source {venv_dir}/bin/activate"

# Install dependencies
run_command(f"{venv_activate} && python -m pip install --upgrade pip")
run_command(f"{venv_activate} && pip install -r requirements.txt")

# Open VS Code
run_command("code .")
