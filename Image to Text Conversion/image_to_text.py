from config import HF_API_KEY
import requests, base64, os, re, time
from PIL import Image
from colorama import init, Fore, Style
init(autoreset=True)
ROUTER_URL = "https://router.huggingface.co/v1/chat/completions"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}", "Content-Type":"Application/json"}
VISION_MODELS = [
    "moonshotai/Kimi-K2.6:novita",
    "meta-llama/Llama-4-Maverick-17B-128E-Instruct:sambanova",
    "meta-llama/Llama-3.2-11B-Vision-Instruct:sambanova",
]
TEXT_MODELS = [
    "Qwen/Qwen2.5-7B-Instruct:togather",
    "Qwen/Qwen2.5-14B-Instruct:togather",
    "Qwen/Qwen2.5-32B-Instruct:togather",
    "mistralai/Mistral-7B-Instruct-v0.3:novita",
    "mistralai/Mistral-8x7B-Instruct-v0.1-vision:novita",
    "metta-llama/Llama-3-8B-Instruct",
    "MiniMaxAI/MiniMax-M1-80K"
]
def _data_url(path: str) -> str:
    with open(path, "rb") as f:
        return "data:image/jpeg;base64,"+base64.b64encode(f.read()).decode("utf-8")
def query_hf_api(payload: dict):
    try:
        r = requests.post(ROUTER_URL, headers = HEADERS, json = payload, timeout = 120)
    except requests.RequestException as e:
        return None, f"Request failed: {e}"
    if r.status_code != 200:
        try:
            j = r.json()
            msg = j.get("error", {}).get("message") or str(j)
        except Exception:
            msg = (r.text or "").strip() or r.reason or "Request failed"
        return None, f"Request failed with status code {r.status_code}: {msg}"
    try:
        return r.json(), None
    except Exception:
        return None, "Failed to parse response as JSON"
def _extract_text(data) -> str:
    msg = (data or {}).get("choices", [{}])[0].get("message", {}) or {}
    return (msg.get("content") or msg.get("text") or "").strip()
def _run_models(models, messages, max_tokens = 160, temprature = 0.3):
    last_err = None
    for moddel in models:
        data, err = query_hf_api({"model": moddel, "messages": messages, "max_tokens": max_tokens, "temperature": temprature})
        if err:
            last_err = err
            continue
        out = _extract_text(data)
        if out:
            return out, None
        last_err = "No text found in response"
    return None, last_err
def _words(text: str) -> int:
    return len(re.findall(r"\S+", text))

def _exact_n_words(text: str) -> str:
    t = (text or "").strip()
    if t and t[-1] not in ".!?":
        t += "."
    return t
def generate_text(prompt: str, max_new_tokens: int = 220):
    raise Exception("Part 2 code not added")
def get_basic_caption(image_path: str) -> str:
    print(f"{fore.yellow}🖼️ Generating basic caption...")
    msg = [{"role": "user", "content": f"Generate a short caption for the image at {image_path}."}]
    cap, err = _run_models(VISION_MODELS, msg, max_tokens = 90, temperature = 0.2)
    return cap if cap else f"[error] {err}"
def print_menu():
    print(f"""{style/BRIGHT}{Fore.GREEN}
========================= Image to Text Conversion ========================
Select an option:
1. Caption (5 words)
2. Description (30 words)
3. Summary (50 words)
4. Exit
===========================================================================""")
def main():
    image_path = input(f"{Fore.BLUE}Enter the path of the image (e.g., test.jpg): {Style.RESET_ALL}")
    if not os.path.exists(image_path):
        print(f"{Fore.RED}Error: The specified image path does not exist.")
        return
    try:
        Image.open(image_path)
    except Exception as e:
        print(f"{Fore.RED}❌ Failed to open image: {e}")