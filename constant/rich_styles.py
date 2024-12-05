"""
    This script defines various paths to files and folders that are used in the project.
    It also includes definitions of styles for the rich library, which is used for printing colored text in the console.

    * Example usage:
        from constants import console

    Variables:
        - console: Instance of the Console class from the rich library, defined with various styles.
"""

from typing import Optional, Callable, Any, Dict, Tuple
from rich.progress import Progress, ProgressColumn, BarColumn, TextColumn
from rich.text import Text
from rich.progress import ProgressColumn
import time
from rich.progress import Progress, TextColumn, BarColumn, TaskProgressColumn, TimeRemainingColumn, TimeElapsedColumn
from rich.table import Table
from rich.console import Console
from rich.theme import Theme

# Rich print styles
console: Console = Console(theme=Theme({
    "purple": "purple",
    "purple_bold": "purple bold",
    "purple_italic": "purple italic",
    "pink": "pale_violet_red1",
    "pink_bold": "pale_violet_red1 bold",
    "pink_italic": "pale_violet_red1 italic",
    "red": "bright_red",
    "red_bold": "bright_red bold",
    "red_italic": "bright_red italic",
    "brown": "rgb(180,82,45)",
    "brown_bold": "rgb(180,82,45) bold",
    "brown_italic": "rgb(180,82,45) italic",
    "orange": "rgb(255,135,70)",
    "orange_bold": "rgb(255,135,70) bold",
    "orange_italic": "rgb(255,135,70) italic",
    "yellow": "bright_yellow",
    "yellow_bold": "bright_yellow bold",
    "yellow_italic": "bright_yellow italic",
    "green": "green",
    "green_bold": "green bold",
    "green_italic": "green italic",
    "blue": "dodger_blue2",
    "blue_bold": "dodger_blue2 bold",
    "blue_italic": "dodger_blue2 italic",
    "white": "white",
    "white_bold": "white bold",
    "white_italic": "white italic",
    "normal": "default",
    "normal_bold": "bold",
    "normal_italic": "italic",
    "black": "rgb(0,0,0) on white",
    "black_bold": "rgb(0,0,0) on white bold",
    "black_italic": "rgb(0,0,0) on white italic",
    "gray": "rgb(58,58,58)",
    "gray_bold": "rgb(58,58,58) bold",
    "gray_italic": "rgb(58,58,58) italic",
    "repr.number": "bright_red bold",
    "warning": "rgb(224,34,103)",
    "warning_bold": "rgb(224,34,103) bold",
    "warning_italic": "rgb(224,34,103) italic"
}))


# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="purple")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="purple_bold")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="purple_italic")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="pink")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="pink_bold")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="pink_italic")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="red")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="red_bold")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="red_italic")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="brown")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="brown_bold")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="brown_italic")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="orange")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="orange_bold")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="orange_italic")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="yellow")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="yellow_bold")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="yellow_italic")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="green")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="green_bold")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="green_italic")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="blue")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="blue_bold")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="blue_italic")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="white")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="white_bold")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="white_italic")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="normal")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="normal_bold")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="normal_italic")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="black")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="black_bold")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="black_italic")
# console.print("╚═══ Multimedia Magic – Audio Visual Heaven ═══╝", style="repr.number")
# input()


# table = Table(title="Available Styles")
# table.add_column("Color", justify="center")
# table.add_column("Normal", justify="center")
# table.add_column("Bold", justify="center")
# table.add_column("Italic", justify="center")

# table.add_row(
#     "Purple",
#     "[purple]purple[/purple]",
#     "[purple_bold]purple_bold[/purple_bold]",
#     "[purple_italic]purple_italic[/purple_italic]"
# )
# table.add_row(
#     "Pink",
#     "[pink]pink[/pink]",
#     "[pink_bold]pink_bold[/pink_bold]",
#     "[pink_italic]pink_italic[/pink_italic]"
# )
# table.add_row(
#     "Red",
#     "[red]red[/red]",
#     "[red_bold]red_bold[/red_bold]",
#     "[red_italic]red_italic[/red_italic]"
# )
# table.add_row(
#     "Brown",
#     "[brown]brown[/brown]",
#     "[brown_bold]brown_bold[/brown_bold]",
#     "[brown_italic]brown_italic[/brown_italic]"
# )
# table.add_row(
#     "Orange",
#     "[orange]orange[/orange]",
#     "[orange_bold]orange_bold[/orange_bold]",
#     "[orange_italic]orange_italic[/orange_italic]"
# )
# table.add_row(
#     "Yellow",
#     "[yellow]yellow[/yellow]",
#     "[yellow_bold]yellow_bold[/yellow_bold]",
#     "[yellow_italic]yellow_italic[/yellow_italic]"
# )
# table.add_row(
#     "Green",
#     "[green]green[/green]",
#     "[green_bold]green_bold[/green_bold]",
#     "[green_italic]green_italic[/green_italic]"
# )
# table.add_row(
#     "Blue",
#     "[blue]blue[/blue]",
#     "[blue_bold]blue_bold[/blue_bold]",
#     "[blue_italic]blue_italic[/blue_italic]"
# )
# table.add_row(
#     "White",
#     "[white]white[/white]",
#     "[white_bold]white_bold[/white_bold]",
#     "[white_italic]white_italic[/white_italic]"
# )
# table.add_row(
#     "Normal",
#     "[normal]normal[/normal]",
#     "[normal_bold]normal_bold[/normal_bold]",
#     "[normal_italic]normal_italic[/normal_italic]"
# )
# table.add_row(
#     "Black",
#     "[black]black[/black]",
#     "[black_bold]black_bold[/black_bold]",
#     "[black_italic]black_italic[/black_italic]"
# )
# table.add_row(
#     "Gray",
#     "[gray]gray[/gray]",
#     "[gray_bold]gray_bold[/gray_bold]",
#     "[gray_italic]gray_italic[/gray_italic]"
# )

# console.print(table)


# class ColoredProgressColumn(ProgressColumn):
#     def __init__(self, style_name):
#         self.style_name = style_name
#         super().__init__()

#     def render(self, task) -> Text:
#         percentage = int(task.percentage)
#         return Text(f"{percentage:>3d}%", style=self.style_name)


# class ColoredTimeColumn(ProgressColumn):
#     def __init__(self, style_name):
#         self.style_name = style_name
#         super().__init__()

#     def render(self, task) -> Text:
#         elapsed = task.elapsed
#         if elapsed is None:
#             return Text("00:00:00.000", style=self.style_name)

#         hours = int(elapsed // 3600)
#         minutes = int((elapsed % 3600) // 60)
#         seconds = int(elapsed % 60)
#         milliseconds = int((elapsed % 1) * 1000)

#         return Text(f"| {hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}", style=self.style_name)


# class ColoredRemainingColumn(ProgressColumn):
#     def __init__(self, style_name):
#         self.style_name = style_name
#         super().__init__()

#     def render(self, task) -> Text:
#         remaining = task.time_remaining
#         if remaining is None:
#             return Text("00:00:00", style=self.style_name)

#         hours = int(remaining // 3600)
#         minutes = int((remaining % 3600) // 60)
#         seconds = int(remaining % 60)

#         return Text(f"| {hours:02d}:{minutes:02d}:{seconds:02d}", style=self.style_name)


# def color_progress():
#     current_style = "red_bold"
#     progress_column = ColoredProgressColumn(current_style)
#     time_column = ColoredTimeColumn(current_style)
#     remaining_column = ColoredRemainingColumn(current_style)

#     progress = Progress(
#         TextColumn("[progress.description]{task.description}"),
#         BarColumn(
#             bar_width=40,
#             complete_style=current_style,
#             finished_style="green_bold"  # LAST COLOR
#         ),
#         progress_column,
#         remaining_column,
#         time_column,
#         console=console,
#         expand=False
#     )

#     with progress:
#         task = progress.add_task("[red_bold]Processing...", total=100)

#         colors = {
#             25: ("red_bold", "red_bold"),
#             50: ("orange_bold", "orange_bold"),
#             75: ("yellow_bold", "yellow_bold"),
#             100: ("green_bold", "green_bold")
#         }

#         for i in range(100):
#             for threshold, (text_color, bar_color) in colors.items():
#                 if i <= threshold:
#                     progress.columns[1].complete_style = bar_color
#                     progress_column.style_name = bar_color
#                     time_column.style_name = bar_color
#                     remaining_column.style_name = bar_color
#                     progress.update(task,
#                                     advance=1,
#                                     description=f"[{text_color}]Processing...")
#                     break
#             time.sleep(0.05)


# color_progress()


# Progress Bar Styles
class ProgressBar:
    @staticmethod
    def bubble(width: int, progress: float, color: str, empty_color: str = "gray_bold") -> str:
        filled: int = int(width * progress)
        empty: int = width - filled
        return f"[{color}]{'●' * filled}[/{color}][{empty_color}]{'○' * empty}[/{empty_color}]"

    @staticmethod
    def blocks(width: int, progress: float, color: str, empty_color: str = "gray_bold") -> str:
        filled: int = int(width * progress)
        empty: int = width - filled
        return f"[{color}]{'█' * (filled-1)}{'▌' if filled > 0 else ''}[/{color}][{empty_color}]{'░' * empty}[/{empty_color}]"

    @staticmethod
    def arrows(width: int, progress: float, color: str, empty_color: str = "gray_bold") -> str:
        filled: int = int(width * progress)
        empty: int = width - filled
        return f"[{color}]{'﷼' * filled}[/{color}][{empty_color}]{'﷼' * empty}[/{empty_color}]"

    @staticmethod
    def custom(width: int, progress: float, color: str, empty_color: str, filled_char: str, empty_char: str) -> str:
        filled: int = int(width * progress)
        empty: int = width - filled
        return f"[{color}]{filled_char * filled}[/{color}][{empty_color}]{empty_char * empty}[/{empty_color}]"


# Progress Column Components
class ColoredProgressColumn(ProgressColumn):
    def __init__(self, style_name: str) -> None:
        self.style_name: str = style_name
        super().__init__()

    def render(self, task) -> Text:
        if task.total is None:
            return Text("---%", style=self.style_name)
        percentage: int = min(100, int(task.percentage))
        return Text(f"{percentage:>3d}%", style=self.style_name)


class ColoredTimeColumn(ProgressColumn):
    def __init__(self, style_name: str) -> None:
        self.style_name: str = style_name
        super().__init__()

    def render(self, task) -> Text:
        elapsed: float = task.elapsed
        if elapsed is None:
            return Text("00:00:00.000", style=self.style_name)
        hours: int = int(elapsed // 3600)
        minutes: int = int((elapsed % 3600) // 60)
        seconds: int = int(elapsed % 60)
        milliseconds: int = int((elapsed % 1) * 1000)
        return Text(f"| {hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}", style=self.style_name)


class ColoredRemainingColumn(ProgressColumn):
    def __init__(self, style_name: str) -> None:
        self.style_name: str = style_name
        super().__init__()

    def render(self, task) -> Text:
        if task.total is None:
            return Text("| --:--:--", style=self.style_name)
        remaining: float = task.time_remaining
        if remaining is None:
            return Text("| 00:00:00", style=self.style_name)
        hours: int = int(remaining // 3600)
        minutes: int = int((remaining % 3600) // 60)
        seconds: int = int(remaining % 60)
        return Text(f"| {hours:02d}:{minutes:02d}:{seconds:02d}", style=self.style_name)


# Main Progress Bar Manager
class ProgressBarManager:
    def __init__(self,
                 description: str = "Processing...",
                 colors: dict = None,
                 total: int = None,
                 bar: str = "rich",
                 custom_chars: tuple = None,
                 unknown_style: str = "warning_bold") -> None:

        self.total: int = total
        self._init_colors(colors, total, unknown_style)
        self._init_bar_style(total, bar, custom_chars)
        self._init_display_settings(description)
        self._init_columns()
        self._init_progress_bar()

    def _init_colors(self, colors: dict, total: int, unknown_style: str) -> None:
        self.colors: dict = colors or {
            25: ("red_bold", "red_bold"),
            50: ("orange_bold", "orange_bold"),
            75: ("yellow_bold", "yellow_bold"),
            100: ("green_bold", "green_bold")
        }
        first_color: str = list(self.colors.values())[0][0]
        self.current_style: str = first_color if total is not None else unknown_style
        self.last_successful_progress: int = 0

    def _init_bar_style(self, total: int, bar: str, custom_chars: tuple) -> None:
        self.bar_style: str = "rich" if total is None else bar
        self.custom_chars: tuple = custom_chars
        self.progress_bars: dict = {
            "rich": None,
            "bubble": ProgressBar.bubble,
            "blocks": ProgressBar.blocks,
            "arrows": ProgressBar.arrows,
            "custom": ProgressBar.custom if custom_chars else None
        }

    def _init_display_settings(self, description: str) -> None:
        self.description: str = description
        console_width: int = console.width
        desc_length: int = len(description) + 2
        progress_info_width: int = 30

        available_width: int = console_width - desc_length - progress_info_width

        if available_width < 3 and len(description) > 20:
            self.description = description[:17] + "..."
            desc_length = 20 + 2
            available_width = console_width - desc_length - progress_info_width

        self.bar_width: int = max(3, min(40, available_width))

    def _init_columns(self) -> None:
        self.progress_column = ColoredProgressColumn(self.current_style)
        self.time_column = ColoredTimeColumn(self.current_style)
        self.remaining_column = ColoredRemainingColumn(self.current_style)

    def _init_progress_bar(self) -> None:
        last_color: str = list(self.colors.values(
        ))[-1][1] if self.total is not None else self.current_style

        if self.bar_style == "rich":
            self._init_rich_progress_bar(last_color)
        else:
            self._init_custom_progress_bar()

    def _init_rich_progress_bar(self, last_color: str) -> None:
        self.progress: Progress = Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(
                bar_width=self.bar_width,
                complete_style=self.current_style,
                finished_style=last_color,
                pulse_style=self.current_style if self.total is None else "warning_bold"
            ),
            self.progress_column,
            self.remaining_column,
            self.time_column,
            console=console,
            expand=False
        )

    def _init_custom_progress_bar(self) -> None:
        self.progress: Progress = Progress(
            TextColumn("[progress.description]{task.description}"),
            TextColumn(
                "{task.fields[custom_bar]}",
                justify="left"
            ),
            self.progress_column,
            self.remaining_column,
            self.time_column,
            console=console,
            expand=False
        )

    def __enter__(self) -> 'ProgressBarManager':
        self.progress.start()
        self._init_task()
        return self

    def _init_task(self) -> None:
        if self.bar_style != "rich":
            self._init_custom_task()
        else:
            self.task: int = self.progress.add_task(
                f"[{self.current_style}]{self.description}",
                total=self.total
            )

    def _init_custom_task(self) -> None:
        if self.bar_style == "custom" and self.custom_chars:
            initial_bar: str = self.progress_bars[self.bar_style](
                self.bar_width, 0, self.current_style, "gray_bold",
                self.custom_chars[0], self.custom_chars[1]
            )
        else:
            initial_bar: str = self.progress_bars[self.bar_style](
                self.bar_width, 0, self.current_style
            )
        self.task: int = self.progress.add_task(
            f"[{self.current_style}]{self.description}",
            total=self.total,
            custom_bar=initial_bar
        )

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type is not None:
            self.update_style(self.last_successful_progress)
        elif self.total:
            self.update_style(self.total)
        self.progress.stop()

    def update_style(self, current: int) -> None:
        try:
            if not self.total:
                return

            percentage: int = min(100, int((current / self.total) * 100))
            progress: float = current / self.total if self.total else 0

            self._update_progress_bar(current, percentage, progress)
            self.last_successful_progress = current

        except Exception:
            self.progress.update(
                self.task,
                completed=self.last_successful_progress
            )

    def _update_progress_bar(self, current: int, percentage: int, progress: float) -> None:
        if self.bar_style != "rich":
            self._update_custom_bar(progress)

        self._update_colors(current, percentage)

    def _update_custom_bar(self, progress: float) -> None:
        if self.bar_style == "custom" and self.custom_chars:
            custom_bar: str = self.progress_bars[self.bar_style](
                self.bar_width, progress, self.current_style, "gray_bold",
                self.custom_chars[0], self.custom_chars[1]
            )
        else:
            custom_bar: str = self.progress_bars[self.bar_style](
                self.bar_width, progress, self.current_style
            )
        self.progress.update(self.task, custom_bar=custom_bar)

    def _update_colors(self, current: int, percentage: int) -> None:
        last_color: tuple = None
        for threshold, (text_color, bar_color) in sorted(self.colors.items()):
            if percentage <= threshold:
                self._apply_color_update(current, text_color, bar_color)
                break
            last_color = (text_color, bar_color)
        else:
            if last_color:
                text_color, bar_color = last_color
                self._apply_color_update(current, text_color, bar_color)

    def _apply_color_update(self, current: int, text_color: str, bar_color: str) -> None:
        if self.bar_style == "rich":
            self.progress.columns[1].complete_style = bar_color
        self.progress_column.style_name = bar_color
        self.time_column.style_name = bar_color
        self.remaining_column.style_name = bar_color
        self.current_style = bar_color
        self.progress.update(
            self.task,
            completed=current,
            description=f"[{text_color}]{self.description}"
        )

    def advance(self, task_id: int, advance: int = 1) -> None:
        try:
            self.progress.advance(task_id, advance)
            self.last_successful_progress += advance
        except Exception:
            self.progress.update(
                self.task,
                completed=self.last_successful_progress
            )

    def add_task(self, description: str, total: int) -> int:
        return self.progress.add_task(description, total=total)

    def __call__(self, func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            with self:
                return func(self, *args, **kwargs)
        return wrapper


# Example Usage and Tests
def test_unknown_progress() -> None:
    with ProgressBarManager(
        description="Unknown Progress...",
        total=None,
    ) as pb:
        for _ in range(20):
            pb.progress.update(pb.task, advance=1)
            time.sleep(0.05)


def test_unknown_progress_custom_style() -> None:
    with ProgressBarManager(
        description="Unknown Progress (Blue)...",
        total=None,
        unknown_style="blue_bold",
    ) as pb:
        for _ in range(20):
            pb.progress.update(pb.task, advance=1)
            time.sleep(0.05)


def test_colorful_progress() -> None:
    with ProgressBarManager(
        description="Colorful Progress...",
        total=100,
        colors={
            10: ("purple", "purple"),
            20: ("pink", "pink"),
            30: ("red", "red"),
            40: ("brown", "brown"),
            50: ("orange", "orange"),
            60: ("yellow", "yellow"),
            70: ("green", "green"),
            80: ("blue", "blue"),
            90: ("white", "white"),
            100: ("normal", "normal")
        },
        bar="blocks",
    ) as pb:
        for i in range(0, 101, 1):
            pb.update_style(i)
            time.sleep(0.05)


def test_simple_progress() -> None:
    with ProgressBarManager(
        description="Simple Progress...",
        total=10,
        bar="bubble"
    ) as pb:
        for i in range(10):
            pb.update_style(i)
            time.sleep(0.05)


def test_custom_progress() -> None:
    with ProgressBarManager(
        description="Custom Progress...",
        total=50,
        bar="custom",
        custom_chars=("﷼", " ")
    ) as pb:
        for i in range(50):
            pb.update_style(i)
            time.sleep(0.05)


@ProgressBarManager(description="Decorator Progress...", total=50)
def test_decorator_progress(progress_bar: ProgressBarManager) -> None:
    for i in range(50):
        progress_bar.update_style(i)
        time.sleep(0.05)


if __name__ == "__main__":
    test_unknown_progress()
    test_unknown_progress_custom_style()
    test_colorful_progress()
    test_simple_progress()
    test_custom_progress()
    test_decorator_progress()
