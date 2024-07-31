import re
from lexanalyzer import analysis

EXAMPLE_CODE_PATH = "assets/example.☀️"

tokens = analysis.analyze_file(EXAMPLE_CODE_PATH)

for token in tokens:
    print(token)
