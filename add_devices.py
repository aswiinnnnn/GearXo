import json
from pathlib import Path

root = Path('/home/ubuntu/swapphone/client/public/data')
models_path = root / 'models.json'
products_path = root / 'products.json'

new_models = [
    {"id":"iphone-14","brandId":"apple","name":"iPhone 14","storageOptions":["128GB","256GB"],"colors":[{"name":"Midnight","hex":"#252525"},{"name":"Blue","hex":"#9CB5CA"}],"specifications":{"screenSize":"6.1-inch","chip":"A15 Bionic"},"active":True},
    {"id":"iphone-14-pro","brandId":"apple","name":"iPhone 14 Pro","storageOptions":["128GB","256GB","512GB"],"colors":[{"name":"Space Black","hex":"#353536"},{"name":"Gold","hex":"#F0D6A8"}],"specifications":{"screenSize":"6.1-inch","chip":"A16 Bionic"},"active":True},
    {"id":"galaxy-s23-ultra","brandId":"samsung","name":"Galaxy S23 Ultra","storageOptions":["256GB","512GB"],"colors":[{"name":"Phantom Black","hex":"#202124"},{"name":"Cream","hex":"#E6E1D6"}],"specifications":{"screenSize":"6.8-inch","chip":"Snapdragon 8 Gen 2"},"active":True},
    {"id":"galaxy-s23","brandId":"samsung","name":"Galaxy S23","storageOptions":["128GB","256GB"],"colors":[{"name":"Green","hex":"#687668"},{"name":"Cream","hex":"#E6E1D6"}],"specifications":{"screenSize":"6.1-inch","chip":"Snapdragon 8 Gen 2"},"active":True},
    {"id":"oneplus-11","brandId":"oneplus","name":"OnePlus 11","storageOptions":["128GB","256GB"],"colors":[{"name":"Titan Black","hex":"#252525"},{"name":"Eternal Green","hex":"#4E675C"}],"specifications":{"screenSize":"6.7-inch","chip":"Snapdragon 8 Gen 2"},"active":True},
    {"id":"pixel-7-pro","brandId":"google","name":"Pixel 7 Pro","storageOptions":["128GB","256GB"],"colors":[{"name":"Obsidian","hex":"#292A2B"},{"name":"Hazel","hex":"#9A9585"}],"specifications":{"screenSize":"6.7-inch","chip":"Google Tensor G2"},"active":True},
    {"id":"phone-3a","brandId":"nothing","name":"Phone (3a)","storageOptions":["128GB","256GB"],"colors":[{"name":"Black","hex":"#242424"},{"name":"White","hex":"#E8E8E4"}],"specifications":{"screenSize":"6.77-inch","chip":"Snapdragon 7s Gen 3"},"active":True},
    {"id":"edge-50-pro","brandId":"motorola","name":"Edge 50 Pro","storageOptions":["256GB","512GB"],"colors":[{"name":"Luxe Lavender","hex":"#B8A7C5"},{"name":"Black Beauty","hex":"#242424"}],"specifications":{"screenSize":"6.7-inch","chip":"Snapdragon 7 Gen 3"},"active":True},
    {"id":"razr-50-ultra","brandId":"motorola","name":"Razr 50 Ultra","storageOptions":["512GB"],"colors":[{"name":"Spring Green","hex":"#B9C9A8"},{"name":"Midnight Blue","hex":"#29384F"}],"specifications":{"screenSize":"6.9-inch","chip":"Snapdragon 8s Gen 3"},"active":True}
]

models = json.loads(models_path.read_text())
known = {m['id'] for m in models}
models.extend(m for m in new_models if m['id'] not in known)
models_path.write_text(json.dumps(models, ensure_ascii=False, separators=(',', ':')) + '\n')

images = [
    '/manus-storage/swapphone-listing-desk_edf860e4.png',
    '/manus-storage/swapphone-listing-hand_4fcacd41.png',
    '/manus-storage/swapphone-hero_c76449fc.png',
    '/manus-storage/swapphone-mobile-hero-seamless_8f04ff0e.png',
]
locations = [
    ('Bengaluru','Karnataka'), ('Mumbai','Maharashtra'), ('Pune','Maharashtra'),
    ('Delhi','Delhi'), ('Hyderabad','Telangana'), ('Chennai','Tamil Nadu')
]
entries = [
    ('iphone-14-pro-max','iPhone 14 Pro Max','256GB','Silver', '#D6D6D1', 89999, 104999, 'excellent', 93, 6, 'featured'),
    ('iphone-14','iPhone 14','128GB','Midnight', '#252525', 59999, 69999, 'very-good', 88, 6, 'recommended'),
    ('iphone-14','iPhone 14','256GB','Blue', '#9CB5CA', 66999, 75999, 'excellent', 91, 6, 'recommended'),
    ('iphone-14-pro','iPhone 14 Pro','128GB','Space Black', '#353536', 74999, 89999, 'very-good', 87, 3, 'recommended'),
    ('galaxy-s24-ultra','Galaxy S24 Ultra','256GB','Titanium Black', '#252626', 86999, 99999, 'excellent', 94, 6, 'featured'),
    ('galaxy-s24-ultra','Galaxy S24 Ultra','512GB','Titanium Gray', '#777875', 94999, 109999, 'very-good', 89, 6, 'recommended'),
    ('galaxy-s23-ultra','Galaxy S23 Ultra','256GB','Phantom Black', '#202124', 69999, 84999, 'excellent', 92, 6, 'featured'),
    ('galaxy-s23','Galaxy S23','128GB','Green', '#687668', 44999, 54999, 'very-good', 88, 3, 'recommended'),
    ('oneplus-12','OnePlus 12','256GB','Emerald', '#6D8275', 52999, 64999, 'excellent', 95, 6, 'recommended'),
    ('oneplus-12','OnePlus 12','512GB','Silky Black', '#272727', 58999, 69999, 'very-good', 89, 3, 'recommended'),
    ('oneplus-11','OnePlus 11','128GB','Titan Black', '#252525', 37999, 49999, 'good', 84, 3, 'recommended'),
    ('pixel-8-pro','Pixel 8 Pro','128GB','Obsidian', '#292A2B', 59999, 75999, 'excellent', 93, 6, 'featured'),
    ('pixel-8-pro','Pixel 8 Pro','256GB','Porcelain', '#E8E2D7', 64999, 79999, 'very-good', 88, 3, 'recommended'),
    ('pixel-7-pro','Pixel 7 Pro','128GB','Hazel', '#9A9585', 39999, 54999, 'good', 83, 3, 'recommended'),
    ('phone-2','Phone (2)','128GB','Dark Gray', '#4C4F50', 29999, 39999, 'very-good', 90, 3, 'recommended'),
    ('phone-2','Phone (2)','256GB','White', '#E6E7E4', 34999, 44999, 'excellent', 94, 6, 'recommended'),
    ('phone-3a','Phone (3a)','128GB','Black', '#242424', 27999, 32999, 'excellent', 97, 6, 'featured'),
    ('edge-50-pro','Edge 50 Pro','256GB','Luxe Lavender', '#B8A7C5', 34999, 44999, 'excellent', 92, 6, 'recommended'),
    ('edge-50-pro','Edge 50 Pro','512GB','Black Beauty', '#242424', 38999, 49999, 'very-good', 87, 3, 'recommended'),
    ('razr-50-ultra','Razr 50 Ultra','512GB','Midnight Blue', '#29384F', 69999, 89999, 'excellent', 91, 6, 'featured'),
]

products = json.loads(products_path.read_text())
existing_ids = {p['id'] for p in products}
for i, (model_id, name, storage, color_name, color_hex, price, original, grade, battery, months, tag) in enumerate(entries, start=9):
    product_id = f'SP-{i:06d}'
    if product_id in existing_ids:
        continue
    model = next(m for m in models if m['id'] == model_id)
    image = images[(i - 9) % len(images)]
    discount = round((1 - price / original) * 100)
    city, state = locations[(i - 9) % len(locations)]
    products.append({
        'id': product_id,
        'brandId': model['brandId'],
        'modelId': model_id,
        'name': name,
        'storage': storage,
        'color': {'name': color_name, 'hex': color_hex},
        'pricing': {'price': price, 'originalPrice': original, 'discountPercent': discount, 'currency': 'INR'},
        'condition': {'grade': grade, 'description': {'excellent':'Minimal signs of use','very-good':'Minor signs of use','good':'Visible signs of use'}[grade]},
        'battery': {'healthPercent': battery},
        'warranty': {'available': months > 0, 'months': months},
        'delivery': {'free': True, 'estimatedDays': '2 to 4 business days'},
        'sellerId': 'seller-001',
        'location': {'city': city, 'state': state},
        'images': {'primary': image, 'gallery': [image, images[(i - 8) % len(images)]]},
        'specifications': {**model['specifications'], 'camera': '50MP', 'sim': 'eSIM + Physical SIM'},
        'description': f'{name} in {color_name}, checked by Care Plus and ready for its next owner.',
        'status': 'active',
        'tags': [tag]
    })

products_path.write_text(json.dumps(products, ensure_ascii=False, separators=(',', ':')) + '\n')
print(f'products={len(products)} models={len(models)} added=20')
