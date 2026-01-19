import re

input_file = r"C:\Users\ys-ro\.gemini\antigravity\brain\7f46ae57-0ef3-4d73-ad2a-82282870f7e0\raw_conversation_history.pb"
output_file = r"C:\Users\ys-ro\.gemini\antigravity\brain\7f46ae57-0ef3-4d73-ad2a-82282870f7e0\parsed_history_clean.txt"

print(f"Reading {input_file}...")
with open(input_file, 'rb') as f:
    data = f.read()

# Decode with replacement to handle binary data
text_content = data.decode('utf-8', errors='ignore')

# Now we have a huge string with a lot of garbage.
# We want to extract lines that look like actual text.
# Heuristic: Lines with at least 4 chars, composed of printable chars.

# Split by null bytes or common binary garbage delimiters
# But 'errors=ignore' just drops them. So we might have "validtextGarbagevalidtext" merged.
# Let's try to split by 'non-printable' control chars (except newline/tab).

pattern = re.compile(r'[\x20-\x7E\u4e00-\u9fff]{5,}')
matches = pattern.findall(text_content)

print(f"Found {len(matches)} text segments.")

with open(output_file, 'w', encoding='utf-8') as f:
    for m in matches:
        f.write(m + "\n")

print(f"Saved cleanly to {output_file}")
