print("Le package 'mon_package' a été chargé")

from .math_utils import addition, soustraction, division, multiplication
from .stats_utils import moyenne, mediane
__all__ = ["math_utils", "stats_utils"]