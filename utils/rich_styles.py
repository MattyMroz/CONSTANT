"""
Rich Styles Module +

This module provides a comprehensive set of utilities for creating stylized console output using the rich library.
It includes color themes, progress bars, and logging configurations.

Key Components:
    - Console configuration with custom color themes
    - Progress bar implementations (bubble, blocks, arrows, custom)
    - Progress tracking columns and managers
    - Logging configuration with rich formatting

Classes:
    - ProgressBar: Static methods for different progress bar styles
    - ColoredProgressColumn: Custom progress percentage column
    - ColoredTimeColumn: Custom elapsed time column
    - ColoredRemainingColumn: Custom remaining time column
    - ProgressBarManager: Main class for managing progress bars

Example Usage:
    * console
        from utils.rich_styles import console
        console.print("Hello, World!")

        from utils.rich_styles import print_available_styles
        print_available_styles()

    * Progress bar with unknown total steps
        from utils.rich_styles import ProgressBarManager
        with ProgressBarManager(
            description="Unknown Progress...",
            total=None,
        ) as pb:
            for _ in range(20):
                pb.progress.update(pb.task, advance=1)
                time.sleep(0.05)

    * Progress bar with unknown total and custom style
        from utils.rich_styles import ProgressBarManager
        with ProgressBarManager(
            description="Unknown Progress (Blue)...",
            total=None,
            unknown_style="blue_bold",
        ) as pb:
            for _ in range(20):
                pb.progress.update(pb.task, advance=1)
                time.sleep(0.05)

    * Progress bar with color transitions
        from utils.rich_styles import ProgressBarManager
        with ProgressBarManager(
            description="Colorful Progress...",
            total=100,
            colors={
                8: ("purple_bold", "purple_bold"),
                16: ("pink_bold", "pink_bold"),
                24: ("ruby_red_bold", "ruby_red_bold"),
                32: ("red_bold", "red_bold"),
                40: ("brown_bold", "brown_bold"),
                48: ("orange_bold", "orange_bold"),
                56: ("yellow_bold", "yellow_bold"),
                64: ("green_bold", "green_bold"),
                72: ("blue_bold", "blue_bold"),
                80: ("white_bold", "white_bold"),
                88: ("normal_bold", "normal_bold"),
                96: ("black_bold", "black_bold"),
                100: ("gray_bold", "gray_bold")
            },
            bar="blocks",
        ) as pb:
            for i in range(0, 101, 1):
                pb.update_style(i)
                time.sleep(0.05)

    * Progress bar with bubble style
        from utils.rich_styles import ProgressBarManager
        with ProgressBarManager(
            description="Bubble Progress...",
            total=10,
            bar="bubble"
        ) as pb:
            for i in range(10):
                pb.update_style(i)
                time.sleep(0.05)

    * Progress bar with blocks style
        from utils.rich_styles import ProgressBarManager
        with ProgressBarManager(
            description="Blocks Progress...",
            total=10,
            bar="blocks"
        ) as pb:
            for i in range(10):
                pb.update_style(i)
                time.sleep(0.05)

    * Progress bar with arrows style
        from utils.rich_styles import ProgressBarManager
        with ProgressBarManager(
            description="Arrows Progress...",
            total=10,
            bar="arrows"
        ) as pb:
            for i in range(10):
                pb.update_style(i)
                time.sleep(0.05)

    * Progress bar with custom style
        from utils.rich_styles import ProgressBarManager
        with ProgressBarManager(
            description="Custom Progress...",
            total=10,
            bar="custom",
            custom_chars=("*", " ")
        ) as pb:
            for i in range(10):
                pb.update_style(i)
                time.sleep(0.05)

    * Progress bar as decorator
        from utils.rich_styles import ProgressBarManager
        @ProgressBarManager(description="Decorator Progress...", total=10)
        def process_data(progress_bar: ProgressBarManager) -> None:
            for i in range(10):
                progress_bar.update_style(i)

    * Rich logging configuration with various log levels
        from utils.rich_styles import console
        import logging
        from rich.logging import RichHandler

        logging.basicConfig(
            level=logging.DEBUG,
            format="%(message)s",
            datefmt="[%Y-%m-%d %H:%M:%S]",
            handlers=[RichHandler(rich_tracebacks=True, console=console)]
        )

        logger = logging.getLogger("rich")

        # Basic logging levels
        logger.debug("🔍 Debug message with details")
        logger.info("ℹ️ Normal program operation info")
        logger.warning("⚠️ Warning - something might go wrong!")
        logger.error("❌ Critical error in module XYZ")
        logger.critical("💥 CRITICAL ERROR - immediate action required!")

        # Logging with extra data
        extra_data = {"user": "admin", "ip": "192.168.1.1"}
        logger.info("🔐 Login attempt", extra=extra_data)

        # Exception logging
        try:
            x = 1 / 0
        except Exception as e:
            logger.exception("💀 Unexpected error occurred:")

        # Logging with timestamp
        logger.info(f"⏰ Action completed at: {time.strftime('%H:%M:%S')}")

        # Progress logging
        logger.info("📊 Operation progress: 75%")
"""

import logging
import time
from typing import Any, Callable

from rich.console import Console
from rich.logging import RichHandler
from rich.progress import BarColumn, Progress, ProgressColumn, TextColumn
from rich.table import Table
from rich.text import Text
from rich.theme import Theme

# Rich print styles
console: Console = Console(theme=Theme({
    "purple": "purple",
    "purple_bold": "purple bold",
    "purple_italic": "purple italic",
    "pink": "pale_violet_red1",
    "pink_bold": "pale_violet_red1 bold",
    "pink_italic": "pale_violet_red1 italic",
    "ruby_red": "rgb(224,34,103)",
    "ruby_red_bold": "rgb(224,34,103) bold",
    "ruby_red_italic": "rgb(224,34,103) italic",
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

    "info": "dodger_blue2 bold",
    "logging.level.info": "dodger_blue2 bold",

    "warning": "bright_yellow bold",
    "logging.level.warning": "bright_yellow bold",

    "error": "bright_red bold",
    "logging.level.error": "bright_red bold",

    "success": "green bold",

    "debug": "green bold",
    "logging.level.debug": "green bold",

    "critical": "rgb(0,0,0) on bright_red bold",
    "logging.level.critical": "rgb(0,0,0) on bright_red bold",

    "log.time": "rgb(224,34,103) italic",
    "log.level": "rgb(224,34,103) bold",
}))


def print_available_styles() -> None:
    """
        Print a table showing all available text styles with examples.
        The table includes normal, bold and italic variants for each color.
    """
    table: Table = Table(title="Available Styles")
    table.add_column("Color", justify="center")
    table.add_column("Normal", justify="center")
    table.add_column("Bold", justify="center")
    table.add_column("Italic", justify="center")

    styles: list[tuple[str, str, str, str]] = [
        ("Purple", "purple", "purple_bold", "purple_italic"),
        ("Pink", "pink", "pink_bold", "pink_italic"),
        ("Ruby Red", "ruby_red", "ruby_red_bold", "ruby_red_italic"),
        ("Red", "red", "red_bold", "red_italic"),
        ("Brown", "brown", "brown_bold", "brown_italic"),
        ("Orange", "orange", "orange_bold", "orange_italic"),
        ("Yellow", "yellow", "yellow_bold", "yellow_italic"),
        ("Green", "green", "green_bold", "green_italic"),
        ("Blue", "blue", "blue_bold", "blue_italic"),
        ("White", "white", "white_bold", "white_italic"),
        ("Normal", "normal", "normal_bold", "normal_italic"),
        ("Black", "black", "black_bold", "black_italic"),
        ("Gray", "gray", "gray_bold", "gray_italic")
    ]

    for color_name, normal, bold, italic in styles:
        table.add_row(
            color_name,
            f"[{normal}]{normal}[/{normal}]",
            f"[{bold}]{bold}[/{bold}]",
            f"[{italic}]{italic}[/{italic}]"
        )

    console.print(table)

# Progress Bar Styles


class ProgressBar:
    """
        Collection of static methods for rendering different progress bar styles.
        Each method takes width, progress and color parameters to generate a styled progress bar.
    """

    @staticmethod
    def bubble(width: int, progress: float, color: str, empty_color: str = "gray_bold") -> str:
        """
            Create a bubble-style progress bar using filled and empty circles.

            Args:
                width: Width of the progress bar in characters
                progress: Progress value between 0 and 1
                color: Color style for filled bubbles
                empty_color: Color style for empty bubbles

            Returns:
                Formatted string containing the bubble progress bar
        """
        filled: int = int(width * progress)
        empty: int = width - filled
        return f"[{color}]{'●' * filled}[/{color}][{empty_color}]{'○' * empty}[/{empty_color}]"

    @staticmethod
    def blocks(width: int, progress: float, color: str, empty_color: str = "gray_bold") -> str:
        """
            Create a block-style progress bar using solid and empty blocks.

            Args:
                width: Width of the progress bar in characters
                progress: Progress value between 0 and 1
                color: Color style for filled blocks
                empty_color: Color style for empty blocks

            Returns:
                Formatted string containing the block progress bar
        """
        filled: int = int(width * progress)
        empty: int = width - filled
        return f"[{color}]{'█' * (filled-1)}{'▌' if filled > 0 else ''}[/{color}][{empty_color}]{'░' * empty}[/{empty_color}]"

    @staticmethod
    def arrows(width: int, progress: float, color: str, empty_color: str = "gray_bold") -> str:
        """
            Create an arrow-style progress bar using arrow characters.

            Args:
                width: Width of the progress bar in characters
                progress: Progress value between 0 and 1
                color: Color style for filled arrows
                empty_color: Color style for empty arrows

            Returns:
                Formatted string containing the arrow progress bar
        """
        filled: int = int(width * progress)
        empty: int = width - filled
        return f"[{color}]{'﷼' * filled}[/{color}][{empty_color}]{'﷼' * empty}[/{empty_color}]"

    @staticmethod
    def custom(width: int, progress: float, color: str, empty_color: str, filled_char: str, empty_char: str) -> str:
        """
            Create a custom progress bar using specified characters.

            Args:
                width: Width of the progress bar in characters
                progress: Progress value between 0 and 1
                color: Color style for filled section
                empty_color: Color style for empty section
                filled_char: Character to use for filled section
                empty_char: Character to use for empty section

            Returns:
                Formatted string containing the custom progress bar
        """
        filled: int = int(width * progress)
        empty: int = width - filled
        return f"[{color}]{filled_char * filled}[/{color}][{empty_color}]{empty_char * empty}[/{empty_color}]"


# Progress Column Components
class ColoredProgressColumn(ProgressColumn):
    """
        Custom progress column that displays percentage with configurable color.

        Args:
            style_name: Name of the color style to use
    """

    def __init__(self, style_name: str) -> None:
        self.style_name: str = style_name
        super().__init__()

    def render(self, task) -> Text:
        """Render the progress percentage."""
        if task.total is None:
            return Text("---%", style=self.style_name)
        percentage: int = min(100, int(task.percentage))
        return Text(f"{percentage:>3d}%", style=self.style_name)


class ColoredTimeColumn(ProgressColumn):
    """
        Custom column showing elapsed time with configurable color.

        Args:
            style_name: Name of the color style to use
    """

    def __init__(self, style_name: str) -> None:
        self.style_name: str = style_name
        super().__init__()

    def render(self, task) -> Text:
        """Render the elapsed time in HH:MM:SS.mmm format."""
        elapsed: float = task.elapsed
        if elapsed is None:
            return Text("00:00:00.000", style=self.style_name)
        hours: int = int(elapsed // 3600)
        minutes: int = int((elapsed % 3600) // 60)
        seconds: int = int(elapsed % 60)
        milliseconds: int = int((elapsed % 1) * 1000)
        return Text(f"| {hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}", style=self.style_name)


class ColoredRemainingColumn(ProgressColumn):
    """
        Custom column showing remaining time with configurable color.

        Args:
            style_name: Name of the color style to use
    """

    def __init__(self, style_name: str) -> None:
        self.style_name: str = style_name
        super().__init__()

    def render(self, task) -> Text:
        """Render the remaining time in HH:MM:SS format."""
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
    """
        Main class for managing progress bars with various styles and colors.

        Args:
            description: Text description of the progress
            colors: Dictionary mapping progress thresholds to color styles
            total: Total number of steps (None for unknown total)
            bar: Progress bar style ('rich', 'bubble', 'blocks', 'arrows', 'custom')
            custom_chars: Tuple of (filled, empty) characters for custom style
            unknown_style: Color style for progress bars with unknown total

        Examples:
            >>> # Progress bar with unknown total and blue style
            >>> with ProgressBarManager(
            ...     description="Unknown Progress (Blue)...", 
            ...     total=None,
            ...     unknown_style="blue_bold"
            ... ) as pb:
            ...     for _ in range(20):
            ...         pb.progress.update(pb.task, advance=1)
            ...         time.sleep(0.05)

            >>> # Custom progress bar with color transitions
            >>> with ProgressBarManager(
            ...     description="Custom Colorful Progress...",
            ...     total=100,
            ...     colors={
            ...         33: ("red_bold", "red_bold"),
            ...         66: ("yellow_bold", "yellow_bold"), 
            ...         100: ("green_bold", "green_bold")
            ...     },
            ...     bar="custom",
            ...     custom_chars=("&", " ")
            ... ) as pb:
            ...     for i in range(0, 101, 1):
            ...         pb.update_style(i)
            ...         time.sleep(0.05)

            >>> # Using as a decorator with blocks style
            >>> @ProgressBarManager(
            ...     description="Blocks Decorator Progress...",
            ...     total=50,
            ...     bar="blocks"
            ... )
            >>> def process_data(progress_bar: ProgressBarManager) -> None:
            ...     for i in range(50):
            ...         progress_bar.update_style(i)
            ...         time.sleep(0.05)
    """

    def __init__(self,
                 description: str = "Processing...",
                 colors: dict = None,
                 total: int = None,
                 bar: str = "rich",
                 custom_chars: tuple = None,
                 unknown_style: str = "ruby_red_bold") -> None:

        self.total: int = total
        self._init_colors(colors, total, unknown_style)
        self._init_bar_style(total, bar, custom_chars)
        self._init_display_settings(description)
        self._init_columns()
        self._init_progress_bar()

    def _init_colors(self, colors: dict, total: int, unknown_style: str) -> None:
        """
            Initialize color settings for the progress bar.
        """
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
        """Initialize the progress bar style settings."""
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
        """
            Initialize display settings including width calculations.
        """
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
        """
            Initialize progress bar columns.
        """
        self.progress_column = ColoredProgressColumn(self.current_style)
        self.time_column = ColoredTimeColumn(self.current_style)
        self.remaining_column = ColoredRemainingColumn(self.current_style)

    def _init_progress_bar(self) -> None:
        """
            Initialize the main progress bar.
        """
        last_color: str = list(self.colors.values(
        ))[-1][1] if self.total is not None else self.current_style

        if self.bar_style == "rich":
            self._init_rich_progress_bar(last_color)
        else:
            self._init_custom_progress_bar()

    def _init_rich_progress_bar(self, last_color: str) -> None:
        """
            Initialize rich-style progress bar.
        """
        self.progress: Progress = Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(
                bar_width=self.bar_width,
                complete_style=self.current_style,
                finished_style=last_color,
                pulse_style=self.current_style if self.total is None else "ruby_red_bold"
            ),
            self.progress_column,
            self.remaining_column,
            self.time_column,
            console=console,
            expand=False
        )

    def _init_custom_progress_bar(self) -> None:
        """
            Initialize custom-style progress bar.
        """
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
        """
            Context manager entry point.
        """
        self.progress.start()
        self._init_task()
        return self

    def _init_task(self) -> None:
        """
            Initialize progress task.
        """
        if self.bar_style != "rich":
            self._init_custom_task()
        else:
            self.task: int = self.progress.add_task(
                f"[{self.current_style}]{self.description}",
                total=self.total
            )

    def _init_custom_task(self) -> None:
        """
            Initialize custom progress task.
        """
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
        """
            Context manager exit point.
        """
        if exc_type is not None:
            self.update_style(self.last_successful_progress)
        elif self.total:
            self.update_style(self.total)
        self.progress.stop()

    def update_style(self, current: int) -> None:
        """
            Update progress bar style based on current progress.

            Args:
                current: Current progress value
        """
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
        """
            Update progress bar appearance.
        """
        if self.bar_style != "rich":
            self._update_custom_bar(progress)

        self._update_colors(current, percentage)

    def _update_custom_bar(self, progress: float) -> None:
        """
            Update custom progress bar appearance.
        """
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
        """
            Update progress bar colors based on progress percentage.
        """
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
        """
            Apply color updates to progress bar components.
        """
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
        """
        Advance progress by specified amount.

        Args:
            task_id: ID of the task to advance
            advance: Amount to advance by
        """
        try:
            self.progress.advance(task_id, advance)
            self.last_successful_progress += advance
        except Exception:
            self.progress.update(
                self.task,
                completed=self.last_successful_progress
            )

    def add_task(self, description: str, total: int) -> int:
        """
            Add a new progress task.

            Args:
                description: Task description
                total: Total steps for the task

            Returns:
                Task ID
        """
        return self.progress.add_task(description, total=total)

    def __call__(self, func: Callable) -> Callable:
        """
            Decorator for using progress bar with functions.

            Args:
                func: Function to decorate

            Returns:
                Wrapped function
        """
        def wrapper(*args, **kwargs) -> Any:
            with self:
                return func(self, *args, **kwargs)
        return wrapper


# Example Usage
def test_unknown_progress() -> None:
    """
        Test progress bar with unknown total steps.
    """
    with ProgressBarManager(
        description="Unknown Progress...",
        total=None,
    ) as pb:
        for _ in range(20):
            pb.progress.update(pb.task, advance=1)
            time.sleep(0.05)


def test_unknown_progress_custom_style() -> None:
    """
        Test progress bar with unknown total steps and custom style.
    """
    with ProgressBarManager(
        description="Unknown Progress (Blue)...",
        total=None,
        unknown_style="blue_bold",
    ) as pb:
        for _ in range(20):
            pb.progress.update(pb.task, advance=1)
            time.sleep(0.05)


def test_colorful_progress() -> None:
    """
        Test progress bar with multiple color transitions.
    """
    with ProgressBarManager(
        description="Colorful Progress...",
        total=100,
        colors={
            8: ("purple_bold", "purple_bold"),
            16: ("pink_bold", "pink_bold"),
            24: ("ruby_red_bold", "ruby_red_bold"),
            32: ("red_bold", "red_bold"),
            40: ("brown_bold", "brown_bold"),
            48: ("orange_bold", "orange_bold"),
            56: ("yellow_bold", "yellow_bold"),
            64: ("green_bold", "green_bold"),
            72: ("blue_bold", "blue_bold"),
            80: ("white_bold", "white_bold"),
            88: ("normal_bold", "normal_bold"),
            96: ("black_bold", "black_bold"),
            100: ("gray_bold", "gray_bold")
        },
        bar="blocks",
    ) as pb:
        for i in range(0, 101, 1):
            pb.update_style(i)
            time.sleep(0.05)


def test_simple_progress_bubble() -> None:
    """
        Test simple progress bar with bubble style.
    """
    with ProgressBarManager(
        description="Bubble Progress...",
        total=10,
        bar="bubble"
    ) as pb:
        for i in range(10):
            pb.update_style(i)
            time.sleep(0.05)


def test_simple_progress_blocks() -> None:
    """
        Test simple progress bar with blocks style.
    """
    with ProgressBarManager(
        description="Blocks Progress...",
        total=10,
        bar="blocks"
    ) as pb:
        for i in range(10):
            pb.update_style(i)
            time.sleep(0.05)


def test_simple_progress_arrows() -> None:
    """
        Test simple progress bar with arrows style.
    """
    with ProgressBarManager(
        description="Arrows Progress...",
        total=10,
        bar="arrows"
    ) as pb:
        for i in range(10):
            pb.update_style(i)
            time.sleep(0.05)


def test_simple_progress_custom() -> None:
    """
        Test simple progress bar with custom style.
    """
    with ProgressBarManager(
        description="Custom Progress...",
        total=10,
        bar="custom",
        custom_chars=("*", " ")
    ) as pb:
        for i in range(10):
            pb.update_style(i)
            time.sleep(0.05)


@ProgressBarManager(description="Decorator Progress...", total=10)
def test_decorator_progress(progress_bar: ProgressBarManager) -> None:
    """
        Test progress bar as a decorator.
    """
    for i in range(10):
        progress_bar.update_style(i)
        time.sleep(0.05)


def test_logging() -> None:
    """
        Test rich logging configuration with various log levels.
    """
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(message)s",
        datefmt="[%Y-%m-%d %H:%M:%S]",
        handlers=[RichHandler(rich_tracebacks=True, console=console)]
    )

    logger = logging.getLogger("rich")

    logger.debug("🔍 Debug message with details")
    logger.info("ℹ️ Normal program operation info") 
    logger.warning("⚠️ Warning - something might go wrong!")
    logger.error("❌ Critical error in module XYZ")
    logger.critical("💥 CRITICAL ERROR - immediate action required!")

    extra_data = {"user": "admin", "ip": "192.168.1.1"}
    logger.info("🔐 Login attempt", extra=extra_data)

    try:
        x = 1 / 0
    except Exception as e:
        logger.exception("💀 Unexpected error occurred:")

    logger.info(f"⏰ Action completed at: {time.strftime('%H:%M:%S')}")

    logger.info("📊 Operation progress: 75%")


if __name__ == "__main__":
    print_available_styles()
    test_unknown_progress()
    test_unknown_progress_custom_style()
    test_colorful_progress()
    test_simple_progress_bubble()
    test_simple_progress_blocks()
    test_simple_progress_arrows()
    test_simple_progress_custom()
    test_decorator_progress()
    test_logging()
