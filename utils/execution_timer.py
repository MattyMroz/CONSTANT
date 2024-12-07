"""
    Module execution_timer provides an ExecutionTimer class
        to measure the execution time of a code block.
    It offers two usage options: as a context manager and as a decorator.
    It also allows retrieving raw execution time values for custom formatting.

    Examples:
        # Using as a context manager
        with ExecutionTimer():
            main_context()
            time.sleep(1)

        # Using as a decorator
        @ExecutionTimer()
        def main_decorator():
            print('Example as decorator')
            time.sleep(1)
        main_decorator()

        # Using with time retrieval
        with ExecutionTimer(display_time=False) as timer:
            main_context()
            time.sleep(1)
            duration_ns: int = timer.get_duration_ns()
"""

from datetime import datetime
from time import perf_counter_ns
from typing import Optional, Tuple, Any, Callable

from dataclasses import dataclass
from rich.console import Console


@dataclass(slots=True)
class ExecutionTimer:
    """
    ExecutionTimer measures execution time of code blocks.

    Examples:
        >>> # Using as a context manager
        >>> with ExecutionTimer():
        ...     main_context()
        ...     time.sleep(1)

        >>> # Using as a decorator
        >>> @ExecutionTimer()
        ... def main_decorator():
        ...     print('Example as decorator')
        ...     time.sleep(1)
        ...
        >>> main_decorator()

        >>> # Using with time retrieval
        >>> with ExecutionTimer(display_time=False) as timer:
        ...     main_context()
        ...     time.sleep(1)
        ...     duration_ns: int = timer.get_duration_ns()
    """

    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    start_time_ns: Optional[int] = None
    end_time_ns: Optional[int] = None
    display_time: bool = True
    console: Console = Console()

    def __post_init__(self) -> None:
        self.start_date = datetime.now()
        self.start_time_ns = perf_counter_ns()

    def __enter__(self) -> 'ExecutionTimer':
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        try:
            self.end_date = datetime.now()
            self.end_time_ns = perf_counter_ns()
            if self.display_time:
                self._display_time()
        except AttributeError:
            print('An error occurred: __exit__')

    def __call__(self, func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            with self:
                result: Any = func(*args, **kwargs)
            return result
        return wrapper

    def get_duration_ns(self) -> int:
        """Returns raw duration in nanoseconds"""
        if not self.end_time_ns:
            self.end_time_ns = perf_counter_ns()
        return self.end_time_ns - self.start_time_ns

    @staticmethod
    def current_datetime(date: datetime) -> str:
        """
            Formats a datetime object as a string in the format 'YYYY-MM-DD HH:MM:SS'.
        """

        return f'[yellow]{date.year}-{date.month:02d}-{date.day:02d}' \
               f' [white bold]{date.hour:02d}:{date.minute:02d}:{date.second:02d}'

    def calculate_duration(self) -> str:
        """
            Calculates the duration of the code block in hours, minutes, seconds, milliseconds,
            microseconds, and nanoseconds.
        """

        duration_ns: int = self.get_duration_ns()
        duration_s: int
        duration_ns_remainder: int
        duration_s, duration_ns_remainder = map(
            int, divmod(duration_ns, 1_000_000_000))

        duration_ms: int
        duration_ns_remainder2: int
        duration_ms, duration_ns_remainder2 = map(
            int, divmod(duration_ns_remainder, 1_000_000))

        duration_us: int
        duration_ns_final: int
        duration_us, duration_ns_final = map(
            int, divmod(duration_ns_remainder2, 1_000))

        hours: int
        remainder: int
        hours, remainder = map(int, divmod(duration_s, 3600))

        minutes: int
        seconds: int
        minutes, seconds = map(int, divmod(remainder, 60))

        return f'[white bold]{hours:02d}:{minutes:02d}:{seconds:02d}:' \
               f'{duration_ms:03d}:{duration_us:03d}:{duration_ns_final:03d}'

    def calculate_duration_alt(self) -> Tuple[float, float, float]:
        """
            Calculates the duration of the code block in hours, minutes, and seconds
            using an alternative method.
        """

        duration_ns: int = self.get_duration_ns()
        hours_alt: float = duration_ns / 1_000_000_000 / 60 / 60
        minutes_alt: float = duration_ns / 1_000_000_000 / 60
        seconds_alt: float = duration_ns / 1_000_000_000

        return hours_alt, minutes_alt, seconds_alt

    def _display_time(self) -> None:
        """
            Displays the start date, end date, and duration of the code block execution.
        """

        start_date_str: str = self.current_datetime(self.start_date)
        end_date_str: str = self.current_datetime(self.end_date)
        duration: str = self.calculate_duration()
        hours_alt: float
        minutes_alt: float
        seconds_alt: float
        hours_alt, minutes_alt, seconds_alt = self.calculate_duration_alt()

        self.console.print(
            '\n[bold white]╚═══════════ EXECUTION TIME ═══════════╝')
        self.console.print(
            '[bold bright_yellow]        YYYY-MM-DD HH:MM:SS:ms :µs :ns')
        self.console.print(
            f'[bright_red bold][[bold white]START[bright_red bold]] {start_date_str}')
        self.console.print(
            f'[bright_red bold][[bold white]END[bright_red bold]]   {end_date_str}')
        self.console.print(
            f'[bright_red bold][[bold white]TIME[bright_red bold]]  [bold bright_yellow]YYYY-MM-DD {duration}')
        self.console.print('[bright_red bold]                   ^^^^^^^^^^^^')
        self.console.print(
            f'[bright_red bold][[bold white]TIME[bright_red bold]]  [white bold]{hours_alt:.9f} hours')
        self.console.print(
            f'[bright_red bold][[bold white]TIME[bright_red bold]]  [white bold]{minutes_alt:.9f} minutes')
        self.console.print(
            f'[bright_red bold][[bold white]TIME[bright_red bold]]  [white bold]{seconds_alt:.9f} seconds')


def main() -> None:
    """
        Examples of using ExecutionTimer as a decorator and context manager
    """
    import time

    @ExecutionTimer()
    def main_decorator() -> None:
        print('Example as decorator')
        time.sleep(1)

    def main_context() -> None:
        print('\nExample as context manager')
        time.sleep(1)

    main_decorator()

    with ExecutionTimer():
        main_context()

    with ExecutionTimer(display_time=False) as timer:
        main_context()
        duration_ns: int = timer.get_duration_ns()
        print(f"\nRaw duration: {duration_ns} nanoseconds")


if __name__ == '__main__':
    main()
