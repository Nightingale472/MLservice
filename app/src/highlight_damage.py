from PIL import Image, ImageDraw
import io

def highlight_damage(image_path: str, results: dict) -> bytes:
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    
    xmin = results.get("xmin")
    ymin = results.get("ymin")
    xmax = results.get("xmax")
    ymax = results.get("ymax")
    class_name = results.get("class_name")
    confidence = results.get("confidence")
    
    if xmin is not None and ymin is not None and xmax is not None and ymax is not None:
        draw.rectangle([(xmin, ymin), (xmax, ymax)], outline="red", width=3)
        text = f"{class_name} ({confidence:.2f})"
        draw.text((xmin, ymin - 10), text, fill="red")
    
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='JPEG')
    img_byte_arr.seek(0)
    
    return img_byte_arr.getvalue()
