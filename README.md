# Memory Usage Monitor and Alarm

This Python script continuously monitors system memory usage and sends alarms to a remote API if it exceeds a specified threshold.

## Prerequisites

Before running the script, make sure you have the following prerequisites installed:

- Python 3.x
- Required Python libraries (`psutil`, `requests`). You can install them using pip:


## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the Python script using the following command:



The script will start monitoring memory usage.

4. The script will continuously check memory usage, and if it exceeds the specified threshold (default: 80%), it will send an alarm to a remote API.

You can modify the `threshold` variable in the `memory_monitor.py` script to set your desired memory usage threshold.

5. To stop the script, press `Ctrl + C` in the terminal where it is running.

## Customization

You can customize the script behavior by modifying the `memory_monitor.py` file:

- Change the `threshold` value to set a different memory usage threshold.
- Modify the `url` variable in the `send_alarm` function to specify the remote API endpoint where alarms are sent.

## Example Response

When an alarm is sent, the script will print the HTTP response status code to the terminal.

## Troubleshooting

If you encounter any issues or have questions, feel free to open an issue in this repository.
