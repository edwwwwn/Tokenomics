import sys
import tiktoken

def count_tokens(text, model="gpt-4"):
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

def optimize_prompt(prompt):
    words = prompt.split()

    filler_words = [
        "please", "could", "would", "kindly",
        "i want", "i need", "make sure",
        "create", "generate"
    ]

    filtered = [w for w in words if w.lower() not in filler_words]

    if len(filtered) > 50:
        filtered = filtered[:50]

    return " ".join(filtered)

def analyze_tokens(num_tokens):
    if num_tokens < 100:
        return "🟢 Barato"
    elif num_tokens < 500:
        return "🟡 Medio"
    else:
        return "🔴 Caro"

def load_prompt():
    if len(sys.argv) > 1:
        try:
            with open(sys.argv[1], "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return sys.argv[1]
    else:
        print("❌ Uso: tokenomics prompt.txt o tokenomics \"tu prompt\"")
        sys.exit()

def main():
    prompt = load_prompt()

    tokens = count_tokens(prompt)
    optimized = optimize_prompt(prompt)
    optimized_tokens = count_tokens(optimized)

    print("\n--- RESULTADO ORIGINAL ---")
    print(f"Tokens: {tokens} → {analyze_tokens(tokens)}")

    print("\n--- PROMPT OPTIMIZADO ---")
    print(optimized)

    print("\n--- RESULTADO OPTIMIZADO ---")
    print(f"Tokens: {optimized_tokens} → {analyze_tokens(optimized_tokens)}")

if __name__ == "__main__":
    main()
