import sys

import jamo

from jamo import hangul_to_jamo

hangul = hangul_to_jamo(sys.stdin.readline())
