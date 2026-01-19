
input_file = r"C:\Users\ys-ro\.gemini\antigravity\brain\7f46ae57-0ef3-4d73-ad2a-82282870f7e0\parsed_history_clean.txt"
output_file = r"C:\Users\ys-ro\.gemini\antigravity\brain\7f46ae57-0ef3-4d73-ad2a-82282870f7e0\FINAL_FULL_CHAT_LOG.txt"
# Use a shorter marker just in case spaces/underscores are weird
marker = "Medical_City"

print(f"Searching for marker '{marker}' in {input_file}...")

with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

found = False
start_index = 0
for i, line in enumerate(lines):
    if marker in line:
        start_index = i
        found = True
        print(f"Found marker at line {i}: {line.strip()}")
        break

if found:
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(lines[start_index:])
    print(f"Saved {len(lines) - start_index} lines to {output_file}")
else:
    print("Marker not found. Saving whole file instead.")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(lines)
