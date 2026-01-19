
input_file = r"C:\Users\ys-ro\.gemini\antigravity\brain\7f46ae57-0ef3-4d73-ad2a-82282870f7e0\parsed_history_raw.txt"
output_file = r"C:\Users\ys-ro\.gemini\antigravity\brain\7f46ae57-0ef3-4d73-ad2a-82282870f7e0\targeted_conversation_history.txt"
start_marker = "Medical_City_Global_Ascent_Strategy.pdf"

print(f"Searching for marker '{start_marker}' in {input_file}...")

try:
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    index = content.find(start_marker)
    
    if index != -1:
        print(f"Found marker at index {index}. Extracting...")
        # Extract from the marker onwards
        extracted_content = content[index:]
        
        # Write to output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(extracted_content)
            
        print(f"Success! Extracted {len(extracted_content)} chars.")
        print(f"Saved to: {output_file}")
    else:
        print("Marker not found in file.")

except Exception as e:
    print(f"Error: {e}")
