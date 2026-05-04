import argparse
from engine.orchestrator import run_investigation
from utils.banner import show_banner

def main():
    show_banner()

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username")
    parser.add_argument("-e", "--email")

    args = parser.parse_args()

    if not args.username and not args.email:
        print("Provide username or email")
        return

    result = run_investigation(args.username, args.email)

    print("\n[+] Risk Score:", result["risk_score"])
    print("[+] Report saved in output/report.json")

if __name__ == "__main__":
    main()