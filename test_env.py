"""Test environment variable configuration."""
import os

def check_environment():
    """Check if required environment variables are set."""

    print("=== Environment Variable Check ===\n")

    # Check ANTHROPIC_API_KEY
    anthropic_key = os.getenv('ANTHROPIC_API_KEY')
    if anthropic_key:
        print(f"✓ ANTHROPIC_API_KEY: Set ({len(anthropic_key)} chars)")
        print(f"  Preview: {anthropic_key[:10]}...{anthropic_key[-4:]}")
    else:
        print("✗ ANTHROPIC_API_KEY: NOT SET")
        print("  To set in PowerShell:")
        print("    $env:ANTHROPIC_API_KEY = 'sk-ant-api03-your-key-here'")

    # Check GITHUB_TOKEN
    github_token = os.getenv('GITHUB_TOKEN')
    if github_token:
        print(f"\n✓ GITHUB_TOKEN: Set ({len(github_token)} chars)")
        print(f"  Preview: {github_token[:10]}...{github_token[-4:]}")
    else:
        print("\n✗ GITHUB_TOKEN: NOT SET")
        print("  To set in PowerShell:")
        print("    $env:GITHUB_TOKEN = 'ghp_your-token-here'")

    print("\n=== Configuration Files ===")

    # Check config file
    config_path = "config/spark.yml"
    if os.path.exists(config_path):
        print(f"✓ Config file exists: {config_path}")
    else:
        print(f"✗ Config file missing: {config_path}")

    # Check .env file (optional)
    if os.path.exists(".env"):
        print("✓ .env file exists (optional)")
    else:
        print("○ .env file not found (optional)")

    print("\n=== Configuration Status ===")
    if anthropic_key and github_token:
        print("✓ All required variables are set!")
        print("\nYou can now run:")
        print("  spark unified --user markhazleton --include-ai-summaries")
        print("  spark analyze --user markhazleton")
        return True
    else:
        print("✗ Missing required variables")
        print("\nSet the missing variables and try again.")
        return False

if __name__ == "__main__":
    check_environment()
