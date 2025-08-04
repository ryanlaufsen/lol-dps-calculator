"""League of Legends DPS calculator.

This module provides a small helper that reads a screenshot of the in-game HUD
and extracts the four combat statistics needed to estimate a champion's
average basic-attack DPS.  The original project captured the screen directly
from a running client, but for the sake of portability this version simply
expects a path to a pre-captured screenshot.

The screenshot included in the repository (``in-game-screenshot.png``) was
used during development and contains the region of the HUD with the relevant
statistics.  ``calculate_dps`` crops that region, performs a little image
processing to improve OCR quality and then runs Tesseract to read the numbers.
Finally, the function computes critical damage and average DPS and returns all
of the values as floats.
"""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Tuple

import cv2  # type: ignore
import pytesseract  # type: ignore

# Path to the tesseract binary can be overridden by setting the environment
# variable ``TESSERACT_CMD``.  This keeps the script working on systems where
# tesseract is installed in a non-standard location.
import os
TESSERACT_CMD = os.getenv("TESSERACT_CMD")
if TESSERACT_CMD:
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD


@dataclass
class DpsStats:
    """Container for the relevant combat statistics."""

    attack_damage: float
    attack_speed: float
    crit_chance: float
    crit_multiplier: float
    average_dps: float


# Hard coded crop of the HUD region containing the four statistics.
_HUD_CROP = (558, 990, 32, 82)  # x, y, width, height


def _extract_numbers(image_path: Path) -> Tuple[float, float, float, float]:
    """Extract raw numbers from ``image_path`` using pytesseract.

    Parameters
    ----------
    image_path:
        Path to the screenshot containing the HUD.

    Returns
    -------
    tuple of four floats
        Attack damage, attack speed, crit chance and an unused placeholder.
    """

    img = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Could not load image: {image_path}")

    x, y, w, h = _HUD_CROP
    cropped = img[y : y + h, x : x + w]
    inverted = cv2.bitwise_not(cropped)
    processed = cv2.adaptiveThreshold(
        inverted, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 63, 4
    )

    text = pytesseract.image_to_string(
        processed, config="--psm 6 digits tessedit_char_whitelist=0123456789"
    )
    stats = text.split()
    if len(stats) < 4:
        raise ValueError(f"Unable to parse stats from image: {text!r}")

    atk_dmg = float(stats[0])
    atk_speed = float(stats[2])
    crit_chance = float(stats[3])
    placeholder = float(stats[1]) if len(stats) > 1 else 0.0
    return atk_dmg, atk_speed, crit_chance, placeholder


@lru_cache(maxsize=4)
def _cached_extract(image_path: str, mtime: float) -> Tuple[float, float, float, float]:
    """Cached wrapper around ``_extract_numbers``.

    ``mtime`` is included in the cache key so the OCR is rerun when the source
    image changes.
    """
    return _extract_numbers(Path(image_path))


def calculate_dps(image_path: str = "in-game-screenshot.png") -> DpsStats:
    """Calculate DPS values from a screenshot.

    Parameters
    ----------
    image_path:
        Path to the screenshot to analyse.  By default the bundled
        ``in-game-screenshot.png`` is used which allows the project to be
        demonstrated without the game client running.
    Caching is employed so repeated calls with an unchanged image avoid the
    expensive OCR step.  The cache key is the image path and its modification
    time, ensuring the numbers are re-read only when the file changes.
    """

    path = Path(image_path)
    mtime = path.stat().st_mtime

    atk_dmg, atk_speed, crit_chance, _ = _cached_extract(str(path), mtime)

    # Critical strike chance is represented as a percentage.  Each percent of
    # crit chance increases crit damage by 0.75% on top of the base 75%
    # bonus, matching the behaviour of League of Legends.
    bonus_crit_dmg = crit_chance * 0.75
    crit_multiplier = 1 + crit_chance * (0.75 + bonus_crit_dmg)
    average_dps = atk_speed * atk_dmg * crit_multiplier

    return DpsStats(atk_dmg, atk_speed, crit_chance, crit_multiplier, average_dps)


__all__ = ["calculate_dps", "DpsStats"]

if __name__ == "__main__":
    stats = calculate_dps()
    print(
        f"Attack Damage: {stats.attack_damage}\n"
        f"Attack Speed: {stats.attack_speed}\n"
        f"Crit Chance: {stats.crit_chance}\n"
        f"Crit Multiplier: {stats.crit_multiplier}\n"
        f"Average DPS: {stats.average_dps}"
    )
