import json
from pathlib import Path

root = Path('/home/ubuntu/swapphone/client/public/data')
remove_ids = {'nothing', 'motorola'}

for filename in ['brands.json', 'models.json', 'products.json']:
    path = root / filename
    data = json.loads(path.read_text())
    if filename == 'brands.json':
        data = [item for item in data if item.get('id') not in remove_ids]
    elif filename == 'models.json':
        data = [item for item in data if item.get('brandId') not in remove_ids]
    else:
        data = [item for item in data if item.get('brandId') not in remove_ids]
    path.write_text(json.dumps(data, ensure_ascii=False, separators=(',', ':')) + '\n')

homepage_path = root / 'homepage.json'
homepage = json.loads(homepage_path.read_text())
homepage['hero']['description'] = 'Tested second-hand iPhones, Samsung, OnePlus, Google and more. Clear condition grades, warranty coverage, and delivery across India.'
homepage_path.write_text(json.dumps(homepage, ensure_ascii=False, separators=(',', ':')) + '\n')
print('Removed Nothing and Motorola from brands, models, products, and homepage copy.')
