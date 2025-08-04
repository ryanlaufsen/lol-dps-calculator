# lol-dps-calculator

Live basic-attack DPS calculator for *League of Legends*.

The project reads a screenshot of the game's HUD, extracts the combat stats
(attack damage, attack speed and critical-strike chance) using a bit of image
processing and [Tesseract OCR](https://github.com/tesseract-ocr/tesseract), and
then computes the average DPS.  A small PyQt5 GUI displays the values and keeps
them updated every second.

For convenience the repository contains `in-game-screenshot.png`, a captured HUD
segment that allows the project to be demonstrated without having the game
running.  By default all scripts operate on this image, but a different
screenshot can be supplied if desired.

## Running the demo

```
python app-test.py
```

The above command launches the GUI and refreshes the DPS calculation once per
second.  The OCR step is cached, so repeated refreshes of an unchanged
screenshot return instantly without re-reading the file.
