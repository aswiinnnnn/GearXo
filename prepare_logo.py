from pathlib import Path
from PIL import Image

src = Path('/home/ubuntu/upload/ChatGPTImageAug16,2026,02_46_45AM.png')
out_dir = Path('/home/ubuntu/webdev-static-assets')
out_dir.mkdir(parents=True, exist_ok=True)

image = Image.open(src).convert('RGBA')
alpha = image.getchannel('A')
bbox = alpha.getbbox()
if bbox:
    image = image.crop(bbox)

# Preserve the supplied mark and create web-sized variants with transparent padding.
variants = {
    'swapphone-logo.png': (320, 334),
    'swapphone-logo-header.png': (180, 188),
    'swapphone-logo-favicon.png': (64, 67),
}
for filename, size in variants.items():
    canvas = Image.new('RGBA', size, (0, 0, 0, 0))
    fitted = image.copy()
    fitted.thumbnail((size[0] - 8, size[1] - 8), Image.Resampling.LANCZOS)
    x = (size[0] - fitted.width) // 2
    y = (size[1] - fitted.height) // 2
    canvas.alpha_composite(fitted, (x, y))
    canvas.save(out_dir / filename, 'PNG', optimize=True, compress_level=9)

# Create graphite variants for the light SwapPhone surfaces while preserving the supplied silhouette and alpha.
dark_variants = {
    'swapphone-logo-dark.png': (320, 334),
    'swapphone-logo-dark-header.png': (180, 188),
    'swapphone-logo-dark-favicon.png': (64, 67),
}
for filename, size in dark_variants.items():
    canvas = Image.new('RGBA', size, (0, 0, 0, 0))
    fitted = image.copy()
    fitted.thumbnail((size[0] - 8, size[1] - 8), Image.Resampling.LANCZOS)
    pixels = fitted.load()
    for y in range(fitted.height):
        for x in range(fitted.width):
            r, g, b, a = pixels[x, y]
            if a:
                pixels[x, y] = (31, 36, 34, a)
    x = (size[0] - fitted.width) // 2
    y = (size[1] - fitted.height) // 2
    canvas.alpha_composite(fitted, (x, y))
    canvas.save(out_dir / filename, 'PNG', optimize=True, compress_level=9)

# Also create an optimized WebP for the header where supported.
header = Image.open(out_dir / 'swapphone-logo-dark-header.png').convert('RGBA')
header.save(out_dir / 'swapphone-logo-dark-header.webp', 'WEBP', lossless=True, method=6)
print('Prepared:', ', '.join(str(out_dir / name) for name in [*variants, 'swapphone-logo-header.webp', *dark_variants, 'swapphone-logo-dark-header.webp']))
