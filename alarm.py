import time

import psutil
import requests

threshold = 80


def send_alarm() -> None:
    """
        Send an alarm to a remote API if memory usage exceeds the threshold.

        This function sends a POST request to a remote API with memory usage information.

        Parameters:
        None

        Returns:
        None
        """

    url = "https://api.example.com/alarm"
    params = {
        "memory_usage": psutil.virtual_memory().percent
    }
    response = requests.post(url, json=params)
    print(response.status_code)


def main() -> None:
    """
      Continuously monitor memory usage and send alarms if it exceeds the threshold.

      This function runs in an infinite loop, checking the system's memory usage. If the memory
      usage exceeds the specified threshold, it calls the send_alarm function and then waits
      for 1 second before checking again.

      Parameters:
      None

      Returns:
      None
      """
    while True:
        memory_usage = psutil.virtual_memory().percent
        if memory_usage > threshold:
            send_alarm()
        time.sleep(1)


if __name__ == '__main__':
    main()
