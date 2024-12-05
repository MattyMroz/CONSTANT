import requests
from rich.progress import Progress


def download_file(url: str, filename: str) -> None:
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kilobyte

    with Progress() as progress:
        task = progress.add_task("Downloading...", total=total_size)

        with open(filename, 'wb') as file:
            for data in response.iter_content(block_size):
                file.write(data)
                progress.update(task, advance=len(data))
                downloaded = progress.tasks[task].completed
                remaining = total_size - downloaded
                progress.console.print(
                    f"Downloaded: {downloaded} bytes, Remaining: {remaining} bytes", end='\r')


# Example usage
download_file('https://example.com/largefile.zip', 'largefile.zip')
