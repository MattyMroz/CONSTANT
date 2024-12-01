from alive_progress import alive_bar
import time

# Podstawowy przykład z dostępnymi opcjami
with alive_bar(
    total=100,
) as bar:
    for i in range(100):
        bar.text = f'Przetwarzam element {i}'  # Dynamiczny tekst
        time.sleep(0.1)
        bar()