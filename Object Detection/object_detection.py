import os, io, time, random, requests, mimetypes
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from config import HF_API_KEY
MODEL = "facebook/detr-resnet-101"
API = f"https://router.huggingface.co/hf-inference/models/{MODEL}"
ALLOWED, MAX_MB = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp", ".tiff"}, 8
EMOJI = {"person" : "🙍", "car" : "🚗", "truck" : "🛻", "bus" : "🚌", "bicycle" : "🚲", "motorcycle" : "🏍️", "dog" : "🐕", "cat" : "🐈", "bird" : "🐦", "horse" : "🐎", "sheep" : "🐑", "cow" : "🐄", "bear" : "🐻", "giraffe" : "🦒", "zebra" : "🦓", "banana" : "🍌", "apple" : "🍎", "orange" : "🍊", "pizza" : "🍕", "broccoli" : "🥦", "book" : "📕", "laptop" : "💻", "tv" : "📺", "bottle" : "🍼", "cup" : "☕"}
def font(sz = 18):
    for f in ("DejaVuSans.ttf", "arial.ttf"):
        try:
            return ImageFont.truetype(f, sz)
        except:
            pass
    return ImageFont.load_default()
def ask_image():
    print("\n🎯 Pick an Image (JPG/PNG/WebP/BMP/TIFF ≤ 8MB) from this folder.")
    while True:
        p = input("Image path: ").strip().strip('"').strip("'")
        if not p or not os.path.isfile(p):
            print("⚠️ Corrupted Image."); continue
        if os.path.splitext(p)[1].lower() not in ALLOWED:
            print("⚠️ Unsupported type."); continue
        if os.path.getsize(p)/(1024*1024) > MAX_MB:
            print("⚠️ Too big (>8MB)."); continue
        try:
            Image.open(p).verify()
        except:
            print("⚠️ Corrupted Image."); continue
        return p
def infer(path, img_bytes, tries = 8):
    mime, _ = mimetypes.guess_type(path)
    for _ in range(tries):
        if mime and mime.startwith("image/"):
            r = requests.post(API, headers = {"Authorization": f"bearer {HF_API_KEY}", "Content-Type": mime}, data = img_bytes, timout = 60)
        else:
            r = requests.post(API, headers = {"Authorization": f"bearer {HF_API_KEY}"}, files = {"inputs": (os.path.basename(path), img_bytes, "application/octet-stream")}, timeout = 60)
        if r.status_code == 200:
            d = r.json()
            if isinstance(d, dict) and "error" in d:
                raise RuntimeError(d["error"])
            if not isinstance(d, list):
                RuntimeError("Bad API Response.")
            return d
        if r.status_code == 503:
            time.sleep(2); continue
        raise RuntimeError(f"API {r.status_code}")