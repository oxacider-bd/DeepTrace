from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import hashlib

def extract_exif(image_path):
    """
    Extract EXIF metadata and generate MD5/SHA256 hashes
    """
    metadata = {}
    
    try:
        image = Image.open(image_path)
        exif_data = image._getexif() or {}

        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            metadata[tag] = value

        # GPS processing
        if "GPSInfo" in metadata:
            gps_info = {}
            for key in metadata["GPSInfo"]:
                decode = GPSTAGS.get(key, key)
                gps_info[decode] = metadata["GPSInfo"][key]
            metadata["GPSInfo"] = gps_info

        # Image resolution
        metadata["Resolution"] = image.size

        # Generate file hashes
        with open(image_path, "rb") as f:
            data = f.read()
            metadata["MD5"] = hashlib.md5(data).hexdigest()
            metadata["SHA256"] = hashlib.sha256(data).hexdigest()

    except Exception as e:
        metadata["Error"] = str(e)

    return metadata
