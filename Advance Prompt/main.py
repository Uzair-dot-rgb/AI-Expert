from hf import generate_response
import time


def temperature_prompt_activity():
    print("=" * 70)
    print("ADVANCED PROMPT ENGINEERING: TEMPERATUR + INSTRUCTIONS")
    print("=" * 70)
    print("\nPART 1: TEMPERATURE EXPLORATION")
    base = input("Enter a creative prompt: ").strip()

    for t, label in [(0.1, "LOW (0.1) - Deterministic"), (0.5, "MEDIUM (0.5) - Balanced"), (0.9, "HIGH (0.9) - Creative")]:
        print(f"\n--- {label} ---")
        print(generate_response(base, temperature = t, max_tokens = 512))
        time.sleep(1)

    print("\nPART 2: INSTRUCTION BASED PROMPTS")
    topic = input("Choose a topic (e.g., climate change, space exploration): ").strip()

    prompts = [
        f"Summarize key facts about {topic} in 3-4 sentences.",
        f"Explain {topic} as if I'm a 10 year old child.",
        f"Write a pro/con list about {topic}.",
        f"Create a fictional new headline from 2050 about {topic}.",

    ]

    for i, p in enumerate(prompts, 1):
        print(f"\n--- Instruction {i} ---\n{p}")
        print(generate_response(p, temperature = 0.7, max_tokens = 512))
        time.sleep(1)

    print("\nPART 3: YOUR OWN INSTRUCTION PROMPT")
    custom = input("Enter your instruction-based prompt: ").strip()

    try:
        temp = float(input("Enter a temperature (0.0 to 1.0): ").strip())
        if not (0.1 <= temp <= 1.0): raise ValueError

    except ValueError:
        print("Invalid temperature. Using default 0.7.")
        temp = 0.7

    print(f"\n--- YOUR PROMPT @ TEMP {temp} ---")
    print(generate_response(custom, temperature = temp, max_tokens = 512))  

    print("\nReflection:")
    print("1) How did the temperature affect the responses?")
    print("2) Which instruction prompt yielded the most interesting response?")
    print("3) How can you apply these techniques in your own projects or work?")
    print("\nChallenge: Try combining multiple instructions in a single prompt and observe the model's behavior.")
    print("Generate content -> rewrite -> summarize -> critique -> expand -> translate. Experiment with different combinations and see how the model responds.")


def pseudo_stream(text, delay = 0.013):
    for ch in text:
        print(ch, end = "", flush = True)
        time.sleep(delay)
    print()


def bonus_stream():
    choice = input("\nBONUS: streaming like output? (y/n): ").strip().lower()
    if choice == "y":
        print("\nStreaming output simulation:\n")
        pseudo_stream(generate_response("Write a short story about a robot learning to love.", temperature = 0.7, max_tokens = 512))


if __name__ == "__main__":
    temperature_prompt_activity()
    bonus_stream()