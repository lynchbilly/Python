def main():
    filename = input("File name: ").strip().lower()

    # Define our "Map" of extensions to media types
    # This is much cleaner than 7 different 'elif' statements!
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }

    # Deep Think: How do we find the match?
    # We loop through the keys in our dictionary
    found = False
    for ext in media_types:
        if filename.endswith(ext):
            print(media_types[ext])
            found = True
            break
    
    # If no match was found after checking all extensions
    if not found:
        print("application/octet-stream")

if __name__ == "__main__":
    main()