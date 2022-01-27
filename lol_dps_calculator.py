from multiprocessing.connection import wait
from cv2 import waitKey
import pygetwindow
import pyautogui
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def calculateDPS():

    try:
        window = pygetwindow.getWindowsWithTitle('League of Legends (TM) Client')[0]
    except IndexError:
        print('League of Legends Client is not running!')
        print('Please start a game and try again.')
        exit()

    x1 = window.left
    y1 = window.top
    width = window.width
    height = window.height

    # LeagueisGoodGame HUD settings
    x1 = 558
    y1 = 990
    width = 32
    height = 82

    x2 = x1 + width
    y2 = y1 + height
    pyautogui.screenshot('screenshot.png')

    img = cv2.imread('screenshot.png', cv2.IMREAD_GRAYSCALE)
    img_cropped = img[y1:y2, x1:x2]
    img_invert = cv2.bitwise_not(img_cropped)
    img_processed = cv2.adaptiveThreshold(img_invert, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 63, 4)

    # cv2.imshow('img', img_processed)
    # waitKey(0)

    text = pytesseract.image_to_string(img_processed, config="--psm 6 digits tessedit_char_whitelist=0123456789")

    stats = text.split()

    atk_dmg = float(stats[0])
    atk_speed = float(stats[2])
    crit_chance = float(stats[3])
    bonus_crit_dmg = crit_chance * 0.75 # every percent of crit_chance gives an added 0.75 percent crit_dmg
    crit_multiplier = 1 + crit_chance * (0.75 + bonus_crit_dmg) # 0.75 is base crit_dmg

    average_dps = atk_speed * atk_dmg * crit_multiplier

    return atk_dmg, atk_speed, crit_chance, crit_multiplier, average_dps

    # print(text, stats)
    # print('Attack Damage: ' + str(atk_dmg) + ' | Attack Speed: ' + str(atk_speed) + ' | Crit Chance: ' + str(crit_chance * 100) + '%' + ' | Crit Multiplier: ' + str((crit_multiplier * 100)) + '%')
    # print('Current Avg DPS: ' + str(average_dps))

#     input('Press ENTER to exit')

# calculateDPS()