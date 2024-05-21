## Using this to auto-rename Substack markdown post file names
## https://github.com/alexferrari88/sbstck-dl

import os
import re

def rename_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            # Extract the date and the rest of the filename
            match = re.match(r'(\d{8})_(\d{6})_(.*)\.md', filename)
            if match:
                date_part = match.group(1)
                title_part = match.group(3)

                # Reformat the date
                formatted_date = f"{date_part[:4]}-{date_part[4:6]}-{date_part[6:]}"

                # Reformat the title part
                formatted_title = title_part.replace("-", " ").title()

                # Create the new filename
                new_filename = f"{formatted_date} {formatted_title}.md"

                # Rename the file
                old_file = os.path.join(directory, filename)
                new_file = os.path.join(directory, new_filename)
                os.rename(old_file, new_file)
                print(f"Renamed: {old_file} -> {new_file}")

# Specify directory with markdown files
directory = "TKTK"

# Call function
rename_files(directory)
