import re
import sys

def extract_strings(filename, min_length=4):
    with open(filename, 'rb') as f:
        content = f.read()
    
    # Try to decode as utf-8, ignoring errors to skip binary data
    # This is a naive "strings" implementation
    text = ""
    current_string = []
    
    for byte in content:
        # Check for printable ASCII or UTF-8 start bytes
        if 32 <= byte <= 126 or byte >= 128 or byte == 10 or byte == 13:
            current_string.append(byte)
        else:
            if len(current_string) >= min_length:
                try:
                    s = bytes(current_string).decode('utf-8')
                    # Filter for likely dialogue lines (simple heuristic)
                    if len(s.strip()) > 0:
                        text += s + "\n"
                except:
                    pass
            current_string = []
            
    if len(current_string) >= min_length:
        try:
            text += bytes(current_string).decode('utf-8') + "\n"
        except:
            pass
            
    return text

input_file = r"C:\Users\ys-ro\.gemini\antigravity\brain\7f46ae57-0ef3-4d73-ad2a-82282870f7e0\raw_conversation_history.pb"
output_file = r"C:\Users\ys-ro\.gemini\antigravity\brain\7f46ae57-0ef3-4d73-ad2a-82282870f7e0\parsed_history_raw.txt"

print(f"Extracting strings from {input_file}...")
extracted_text = extract_strings(input_file)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(extracted_text)

print(f"Done. Saved to {output_file}")
