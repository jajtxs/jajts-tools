import subprocess
import sys

dependencies = [
    "requests",
    "selenium",
    "webdriver_manager",
    "pillow",
    "pytesseract",
    "python-dotenv",
]

def install_dependencies():
    for dependency in dependencies:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", dependency])
            print(f"Successfully installed {dependency}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {dependency}: {e}")

if __name__ == "__main__":
    print("Installing required dependencies...")
    install_dependencies()
    print("All dependencies installed successfully!")
