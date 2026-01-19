import urllib.request
import zipfile
import os
import shutil

url = "https://github.com/cli/cli/releases/download/v2.40.0/gh_2.40.0_windows_amd64.zip"
zip_path = "gh.zip"
extract_path = "gh_temp"

print(f"Downloading {url}...")
try:
    urllib.request.urlretrieve(url, zip_path)
    print("Download complete.")

    print("Extracting...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    
    # Move gh.exe to current root
    # Structure is usually gh_2.40.0_windows_amd64/bin/gh.exe
    found = False
    for root, dirs, files in os.walk(extract_path):
        if "gh.exe" in files:
            src = os.path.join(root, "gh.exe")
            dst = "gh.exe"
            shutil.move(src, dst)
            print(f"Moved {src} to {dst}")
            found = True
            break
            
    if not found:
        print("Error: gh.exe not found in zip.")
    else:
        print("Success! gh.exe is ready.")
        
    # Cleanup
    os.remove(zip_path)
    shutil.rmtree(extract_path)

except Exception as e:
    print(f"Error: {e}")
