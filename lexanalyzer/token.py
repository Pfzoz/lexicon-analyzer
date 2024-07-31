from dataclasses import dataclass
from typing import Any, Literal, Optional

TokenType = Literal[
    "op_arit",
    "op_logic",
    ")",
    "(",
    "=",
    "spacing",
    "☕",
    "🏳",
    "🏁",
    "char",
    "number",
    "number_literal",
    "string",
    "string_literal",
    "errors",
    "id",
    "if",
    "else",
    "loop",
    "commentary"
]

@dataclass
class Token:
    type: TokenType
    value: Optional[Any] = None
