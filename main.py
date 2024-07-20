def time_with_font(time_str: str) -> str:
    font_number = {
        "0": "𝟎",
        "1": "𝟏",
        "2": "𝟐",
        "3": "𝟑",
        "4": "𝟒",
        "5": "𝟓",
        "6": "𝟔",
        "7": "𝟕",
        "8": "𝟖",
        "9": "𝟗"
    }
    
    formatted_str = ":".join("".join(font_number[char] for char in part) for part in time_str.split(":"))
    
    return formatted_str

print(time_with_font("22:43"))
