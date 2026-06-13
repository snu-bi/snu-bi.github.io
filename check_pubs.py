import yaml
import re

with open('_data/publications.yaml', 'r') as f:
    content = f.read()

# Split by entries
entries = re.split(r'(?=^- id:)', content, flags=re.MULTILINE)
entries = [e for e in entries if e.strip().startswith('- id:')]

missing_image = []
missing_link = []
missing_buttons = []
missing_paper_button = []
no_buttons = []

for entry in entries:
    lines = entry.strip().split('\n')
    entry_id = None
    has_image = False
    has_link = False
    has_buttons = False
    has_paper_button = False
    
    for line in lines:
        if line.startswith('  id:'):
            entry_id = line.split(':', 1)[1].strip()
        elif line.startswith('  image:'):
            image_val = line.split(':', 1)[1].strip()
            if image_val and image_val != 'null':
                has_image = True
        elif line.startswith('  link:'):
            link_val = line.split(':', 1)[1].strip()
            if link_val and link_val != 'null':
                has_link = True
        elif line.startswith('  buttons:'):
            has_buttons = True
        elif has_buttons and '- type: paper' in line:
            has_paper_button = True
    
    if not has_image:
        missing_image.append(entry_id)
    if not has_link:
        missing_link.append(entry_id)
    if not has_buttons:
        no_buttons.append(entry_id)
    elif not has_paper_button and has_buttons:
        missing_paper_button.append(entry_id)

print(f"Missing images: {len(missing_image)}")
for id in sorted(missing_image)[:5]:
    print(f"  - {id}")
if len(missing_image) > 5:
    print(f"  ... and {len(missing_image) - 5} more")

print(f"\nMissing link field: {len(missing_link)}")
for id in sorted(missing_link)[:5]:
    print(f"  - {id}")
if len(missing_link) > 5:
    print(f"  ... and {len(missing_link) - 5} more")

print(f"\nNo buttons section: {len(no_buttons)}")
for id in sorted(no_buttons):
    print(f"  - {id}")

print(f"\nHas buttons but no paper link: {len(missing_paper_button)}")
for id in sorted(missing_paper_button)[:3]:
    print(f"  - {id}")
