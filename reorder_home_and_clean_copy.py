from pathlib import Path

root = Path('/home/ubuntu/swapphone')
app_path = root / 'client/src/App.tsx'
app = app_path.read_text()
category_start = app.index('<section className="container py-10 md:py-16">')
category_end = app.index('<section className="container py-12 md:py-20">', category_start)
category_block = app[category_start:category_end]
app_without_category = app[:category_start] + app[category_end:]
featured_start = app_without_category.index('<section className="bg-[#efeee9] py-20 md:py-28">')
app_reordered = app_without_category[:featured_start] + category_block + app_without_category[featured_start:]
app_path.write_text(app_reordered)

for folder in (root / 'client/src', root / 'client/public'):
    for path in folder.rglob('*'):
        if path.is_file() and path.suffix in {'.tsx', '.ts', '.css', '.html', '.json', '.md'}:
            text = path.read_text()
            cleaned = text.replace('\u2014', '')
            if cleaned != text:
                path.write_text(cleaned)
