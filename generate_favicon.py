"""
Generate AL monogram favicon files for arthurclynch.com

Colors matched to site CSS variables:
  --navy:  #0A1628
  --white: #FFFFFF
  --gold:  #C5A55A

Design: "A" in white, "L" in gold on navy background
Font: DejaVu Serif Bold (closest available serif to Playfair Display)
"""

from PIL import Image, ImageDraw, ImageFont

# Exact site colors
NAVY = "#0A1628"
WHITE = "#FFFFFF"
GOLD = "#C5A55A"

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def create_monogram(size):
    """Create the AL monogram at the given size."""
    img = Image.new("RGBA", (size, size), NAVY)
    draw = ImageDraw.Draw(img)

    # Scale font size relative to canvas — letters should fill ~70% of height
    font_size = int(size * 0.52)
    font = ImageFont.truetype(FONT_PATH, font_size)

    # Measure each letter individually
    a_bbox = font.getbbox("A")
    l_bbox = font.getbbox("L")

    a_width = a_bbox[2] - a_bbox[0]
    l_width = l_bbox[2] - l_bbox[0]

    # Tight kerning — slight negative spacing for a cohesive monogram
    kern = int(size * -0.02)
    total_width = a_width + kern + l_width

    # Center the pair horizontally
    start_x = (size - total_width) // 2 - a_bbox[0]

    # Center vertically using the combined ascent
    a_top = a_bbox[1]
    a_height = a_bbox[3] - a_bbox[1]
    l_top = l_bbox[1]
    l_height = l_bbox[3] - l_bbox[1]
    max_height = max(a_height, l_height)
    baseline_y = (size - max_height) // 2 - min(a_top, l_top)

    # Draw "A" in white
    draw.text((start_x, baseline_y), "A", fill=WHITE, font=font)

    # Draw "L" in gold, right after the A with kerning
    l_x = start_x + a_width + kern
    draw.text((l_x, baseline_y), "L", fill=GOLD, font=font)

    return img


def main():
    import os

    root = os.path.dirname(os.path.abspath(__file__))

    # Generate at each required size
    sizes = {
        "favicon-512x512.png": 512,
        "apple-touch-icon.png": 180,
        "favicon-32x32.png": 32,
        "favicon-16x16.png": 16,
    }

    images = {}
    for filename, size in sizes.items():
        # Render at 4x for small sizes, then downscale with LANCZOS for crisp results
        if size <= 32:
            render_size = size * 8
        elif size <= 180:
            render_size = size * 4
        else:
            render_size = size

        img = create_monogram(render_size)

        if render_size != size:
            img = img.resize((size, size), Image.LANCZOS)

        filepath = os.path.join(root, filename)
        img.save(filepath, "PNG")
        images[size] = img
        print(f"  Created {filename} ({size}x{size})")

    # Create favicon.ico with both 16x16 and 32x32
    ico_path = os.path.join(root, "favicon.ico")
    images[32].save(ico_path, format="ICO", sizes=[(16, 16), (32, 32)],
                    append_images=[images[16]])
    print(f"  Created favicon.ico (16x16 + 32x32)")

    print("\nAll favicon files generated successfully.")


if __name__ == "__main__":
    main()
