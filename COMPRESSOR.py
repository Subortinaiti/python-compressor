import os
import subprocess

def compress_folder(input_folder):
    # Ensure the input folder exists
    if not os.path.exists(input_folder):
        print(f"Error: The specified folder '{input_folder}' does not exist.")
        return

    # Create the output folder if it doesn't exist
    output_folder = os.path.join(os.getcwd(), "..COMPRESSED")
    os.makedirs(output_folder, exist_ok=True)

    # Get the base name of the input folder
    base_folder_name = os.path.basename(input_folder)

    # Output archive path
    output_archive = os.path.join(output_folder, f"{base_folder_name}.7z")

    # Use subprocess to call the 7-Zip command with progress updates
    cmd = ["C:\\Program Files\\7-Zip\\7z.exe", "a", "-r", output_archive, input_folder]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)

    # Print progress updates
    for line in iter(process.stdout.readline, ''):
        print(line.strip())
        if "%" in line:
            # Extract the percentage from the line
            percentage = int(line.split()[1][:-1])
            print(f"Progress: {percentage}%")

    # Wait for the process to finish
    process.wait()

    # Check if the compression was successful
    if process.returncode == 0:
        print(f"\nCompression successful. Archive saved at: {output_archive}")
        # Optionally, remove the original folder
        try:
            os.rmdir(input_folder)
            print(f"Original folder '{input_folder}' removed.")
        except OSError as e:
            print(f"Error removing original folder: {e}")
    else:
        print("\nCompression failed.")

if __name__ == "__main__":
    # Get input folder path from the user
    folder_path = input("Enter the folder PATH to compress: ").strip()

    # Call the compression function
    compress_folder(folder_path)
