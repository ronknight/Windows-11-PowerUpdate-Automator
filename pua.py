import subprocess

# Function to run PowerShell commands
def run_powershell_command(command):
    result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Success: {result.stdout}")
    else:
        print(f"Error: {result.stderr}")

# Step 0: Set the execution policy to allow scripts
print("Setting PowerShell execution policy...")
run_powershell_command("Set-ExecutionPolicy RemoteSigned -Scope Process -Force")

# Step 1: Install the PSWindowsUpdate module
print("Installing PSWindowsUpdate module...")
run_powershell_command("Install-Module PSWindowsUpdate -Force")

# Step 2: Import the PSWindowsUpdate module
print("Importing PSWindowsUpdate module...")
run_powershell_command("Import-Module PSWindowsUpdate")

# Step 3: Check for available updates
print("Checking for available updates...")
run_powershell_command("Get-WindowsUpdate")

# Step 4: Install all available updates and automatically reboot if needed
print("Installing updates...")
run_powershell_command("Install-WindowsUpdate -AcceptAll -AutoReboot")
