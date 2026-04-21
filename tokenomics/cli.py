import tiktoken
import sys

def count_tokens(text, model="gpt-4"):
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

def optimize_prompt(prompt):
    words = prompt.split()
    filler_words = ["please","could","would","kindly","i want","i need","make sure","create","generate"]
    filtered = [w for w in words if w.lower() not in filler_words]
    return " ".join(filtered[:50])

def analyze_tokens(n):
    if n < 100:
        return "🟢 Barato"
    elif n < 500:
        return "🟡 Medio"
    return "🔴 Caro"

def get_input():
    print("Pega tu prompt (ENTER ENTER para terminar):\n")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return "\n".join(lines)

def main():
    prompt = get_input()

    if not prompt.strip():
        print("Empty prompt")
        return

    tokens = count_tokens(prompt)
    optimized = optimize_prompt(prompt)
    opt_tokens = count_tokens(optimized)

    print("\n--- ORIGINAL ---")
    print(tokens, analyze_tokens(tokens))

    print("\n--- OPTIMIZED ---")
    print(optimized)

    print("\n--- OPTIMIZED TOKENS ---")
    print(opt_tokens, analyze_tokens(opt_tokens))

if __name__ == "__main__":
    main()
