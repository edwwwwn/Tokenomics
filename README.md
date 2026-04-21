Tokenomics - Quick Installation & Usage Guide ⚡
================================================

⚡ Tokenomics is a lightweight CLI tool to analyze, count, and optimize AI prompts.
It estimates token usage and cost for models like GPT.

================================================
🚀 INSTALLATION / INSTALACIÓN (COPY & PASTE)
================================================

👉 1. Clone the repository
git clone https://github.com/edwwwwn/Tokenomics.git
cd Tokenomics

----------------------------------------

👉 2. Create virtual environment
python3 -m venv venv

----------------------------------------

👉 3. Activate environment

Mac / Linux:
source venv/bin/activate

Windows:
venv\Scripts\activate

----------------------------------------

👉 4. Install dependencies
pip install -r requirements.txt

================================================
▶️ HOW TO RUN / CÓMO EJECUTARLO
================================================

👉 Step 1: Make sure you're inside the project folder
cd Tokenomics

----------------------------------------

👉 Step 2: Activate the virtual environment (IMPORTANT)

Mac / Linux:
source venv/bin/activate

Windows:
venv\Scripts\activate

----------------------------------------

👉 Step 3: Run the tool
python3 tokenomics.py

----------------------------------------

👉 Step 4: Use the tool
- Paste your prompt in the terminal
- Press CTRL + D to finish input
- Wait for analysis results

================================================
🧠 HOW IT WORKS / CÓMO FUNCIONA
================================================

1. Run the tool
2. Paste your prompt
3. Finish input with CTRL + D
4. Get token analysis instantly

================================================
💡 EXAMPLE
================================================

Input:
Create a detailed prompt for a 3D dog model in Blender

Output:
- Token count
- Estimated cost
- Optimized prompt version

================================================
⚠️ COMMON ISSUES / PROBLEMAS COMUNES
================================================

❌ Error: ModuleNotFoundError: tiktoken

Fix:
pip install tiktoken

----------------------------------------

❌ Wrong folder / carpeta incorrecta

Fix:
cd Tokenomics

----------------------------------------

❌ Python not found / versión incorrecta

Check:
python3 --version

================================================
🧩 REQUIREMENTS
================================================

- Python 3.9+
- pip
- venv (recommended)

================================================
🚀 PHILOSOPHY
================================================

Minimal ⚡ Fast ⚡ Terminal-first ⚡ No bloat

Tokenomics is built to be simple:
just run it, paste your prompt, get results.
