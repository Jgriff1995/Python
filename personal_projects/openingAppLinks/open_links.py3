import subprocess
import time


def open_links_from_file(file_path):
    """
    Opens all URLs listed in a text file in new tabs using Google Chrome.

    Args:
        file_path (str): The path to the text file containing the URLs.

    The text file should have one URL per line. Empty lines are ignored.
    """
    # Path to the Chrome executable (adjust for your operating system if necessary)
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

    try:
        # Read the file and extract valid links
        with open(file_path, 'r') as file:
            # Strip whitespace and filter out empty lines
            links = [link.strip() for link in file.readlines() if link.strip()]

        # Check if any valid links were found
        if not links:
            print("No valid links found in the file.")
            return

        # Open each link in a new Chrome tab
        for link in links:
            print(f"Opening: {link}")
            subprocess.Popen([chrome_path, link])
            time.sleep(0.5)  # Short delay to avoid overwhelming the system

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Prompt the user for the file path and call the function
    file_path = input("Enter the path to the text file: ")
    open_links_from_file(file_path)