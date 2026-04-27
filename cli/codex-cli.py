#!/usr/bin/env python3
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def audit_readme():
    print("\n[◈] AUDITING README.md for MONETIZATION...")
    if not os.path.exists("README.md"):
        print("[✕] ERROR: README.md not found in current directory.")
        return

    with open("README.md", "r") as f:
        content = f.read()

    checks = {
        "Elite Header": "⬡ ELITE ENGINEERING CODEX",
        "Sponsorship Link": "github.com/sponsors/",
        "Ko-fi Link": "ko-fi.com",
        "Enterprise Section": "ENTERPRISE",
        "License Section": "LICENSE"
    }

    score = 0
    for name, snippet in checks.items():
        if snippet in content:
            print(f"[✓] {name:20} : FOUND")
            score += 20
        else:
            print(f"[!] {name:20} : MISSING")
    
    print(f"\n[◈] MONETIZATION READINESS SCORE: {score}/100")
    if score < 100:
        print("💡 TIP: Use the Codex template to fill missing sections.")

def get_basic_prompt():
    prompt = """
═══ GEMINI ELITE PROMPT ═══
ROLE: Senior Software Architect
TASK: Analyze this codebase for architectural debt and security flaws.
CONTEXT: [Insert your files here]
OUTPUT: JSON report with 'severity', 'location', and 'fix_strategy'.
═══════════════════════════
    """
    print("\n[◈] GENERATED PROMPT:")
    print(prompt)
    print("Tip: Pipe this to the Gemini CLI for immediate analysis.")

def main():
    while True:
        # clear_screen()
        print("\n⬡ ELITE ENGINEERING CODEX CLI v1.1")
        print("──────────────────────────────────")
        print("1. [FREE] Audit Local README")
        print("2. [FREE] Get Engineering Prompt")
        print("3. [PREMIUM] Generate Monetization Flywheel")
        print("4. [PREMIUM] Enterprise SLA Deployment")
        print("5. Exit")
        
        choice = input("\nSelect command: ")
        
        if choice == '1':
            audit_readme()
        elif choice == '2':
            get_basic_prompt()
        elif choice in ['3', '4']:
            print("\n[✕] ACCESS DENIED")
            print("This feature requires a verified Sponsorship.")
            print("Link: https://github.com/sponsors/BoozeLee")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("\n[!] Invalid choice.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
