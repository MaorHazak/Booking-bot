import sys
import os
sys.path.append(os.path.abspath("./Booking"))  # הוספת התיקייה Booking לנתיב החיפוש של פייתון

from .starting import starting  # ייבוא הפונקציה מקובץ starting.py
from .first_phase import first_phase
from .second_phase import second_phase
from .third_phase import third_phase
from .last_phase import last_phase
