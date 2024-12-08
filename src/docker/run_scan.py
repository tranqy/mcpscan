import subprocess
import sys
import os
import json

def run_semgrep(clone_dir, output_file_name):
    results_dir = "./results"
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    """Run semgrep on the cloned repository."""
    rule_files = [
        "semgrep_rules/extract_https_strings.yml",
        "semgrep_rules/extract_http_strings.yml",
        "semgrep_rules/detect_obfuscated_code.yml",
        "semgrep_rules/detect_dangerous_code.yml"
    ]
    errors = []
    for rule_file in rule_files:
        output_file = os.path.join(results_dir, f"{os.path.basename(rule_file).replace('.yml', '')}_{output_file_name}")
        try:
            subprocess.run([
                "semgrep", 
                "--config", rule_file, 
                clone_dir, 
                "--json", 
                "-o", output_file
            ], check=True)
        except Exception as e:
            errors.append(f"Error running Semgrep with {rule_file}: {e}")

    if errors:
        with open(output_file, "a") as f:
            json.dump({"errors": errors}, f, indent=2)
        sys.exit(1)

if __name__ == "__main__":
    clone_dir = "./working"
    output_file = "./working/results.json"
    run_semgrep(clone_dir, output_file)