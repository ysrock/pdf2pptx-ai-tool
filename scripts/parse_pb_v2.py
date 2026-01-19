import re

input_file = r"C:\Users\ys-ro\.gemini\antigravity\brain\7f46ae57-0ef3-4d73-ad2a-82282870f7e0\raw_conversation_history.pb"
output_file = r"C:\Users\ys-ro\.gemini\antigravity\brain\7f46ae57-0ef3-4d73-ad2a-82282870f7e0\parsed_history_clean.txt"

print(f"Reading {input_file}...")
with open(input_file, 'rb') as f:
    data = f.read()

# Find strings of readable characters (at least 4 chars long)
# Including Chinese characters range \u4e00-\u9fff
regex = re.compile(b'[\x20-\x7E\u4e00-\u9fa5]{4,}')

print("Extracting text...")
matches = regex.findall(data)

with open(output_file, 'w', encoding='utf-8') as f:
    for m in matches:
        try:
            # Try to decode utf-8
            s = m.decode('utf-8')
            f.write(s + "\n")
        except:
            # If basic utf-8 decode fails, try decoding as latin-1 or just skip
            try:
                 s = m.decode('latin-1')
                 # Filter out likely garbage (too many non-alphanumeric)
                 if len(s) > 4:
                     f.write(s + "\n")
            except:
                pass

print(f"Done. Saved to {output_file}")
