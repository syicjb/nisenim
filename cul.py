import os

# Function to check if folder only contains duplicate items
def folder_contains_only_duplicates(folder_path):
    items = os.listdir(folder_path)
    seen = set()
    for item in items:
        if item in seen:
            return True  # Found a duplicate item
        seen.add(item)
    return False  # No duplicate items found

# Example usage
folder_path = '/path/to/folder'
result = folder_contains_only_duplicates(folder_path)
print(result)
