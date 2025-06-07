from __future__ import annotations

from collections.abc import Sequence

__version__: str

class DustMasker:
    """
    Identify and mask low-complexity regions in nucleotide sequences using the
    symmetric DUST algorithm from DustMasker.

    Parameters
    ----------
    sequence : str
        A string representing the nucleotide sequence to be processed. Characters
        other than 'A', 'C', 'G', 'T', 'a', 'c', 'g', 't' will be considered
        ambiguous bases. The minimum allowed sequence length is 4 bases.
    window_size : int, default: 64
        The length of the window used by symmetric DUST algorithm. The minimum
        allowed value is 3.
    score_threshold : int, default: 20
        Score threshold for subwindows. The minimum allowed value is 0.

    Attributes
    ----------
    sequence : str
        A string representing the nucleotide sequence that was provided as input.
    window_size : int
        The length of the window used by symmetric DUST algorithm.
    score_threshold : int
        Score threshold for subwindows.
    intervals: list of tuples
       A immutable list of tuples representing the start and end positions of
       the low-complexity regions identified in the sequence.
    n_masked_bases : int
        The total number of bases that were masked.

    Methods
    -------
    mask
        Returns the sequence with low-complexity regions masked.

    Raises
    ------
    ValueError
       If the input sequence is too short (less than 4 characters) or if the
       window size is too small (less than 3).
    TypeError
       If the input parameters are not of the expected type.
    OverflowError
       If a negative integer is passed as the window size or score threshold.
    """

    sequence: str
    window_size: int
    score_threshold: int
    intervals: Sequence[tuple[int, int]]

    def __init__(
        self, sequence: str, window_size: int = 64, score_threshold: int = 20
    ) -> None: ...
    @property
    def n_masked_bases(self) -> int: ...
    def mask(self, hard: bool) -> str:
        """
        Returns the sequence with low-complexity regions masked.

        Parameters
        ----------
        hard : bool, default: False
            If True, low-complexity regions will be masked with 'N' characters.
            By default, bases within low-complexity regions are converted to
            lowercase (i.e., soft-masking).

        Raises
        ------
        TypeError
           If the input parameters are not of the expected type.
        """
        pass

    def __repr__(self) -> str: ...
