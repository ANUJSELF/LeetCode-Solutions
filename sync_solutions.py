import json
import subprocess

# Run the PowerShell command to fetch LeetCode stats
command = """
$session = "<your_session_token>"
$csrftoken = "<your_csrf_token>"

$headers = @{
    "Content-Type" = "application/json"
    "Cookie" = "LEETCODE_SESSION=$session; csrftoken=$csrftoken"
    "Referer" = "https://leetcode.com"
    "X-CSRFToken" = $csrftoken
}

$query = @"
{
    "query": "query { matchedUser(username: \\"SELFANUJ\\") { submitStats { acSubmissionNum { difficulty count } } } }"
}
"@

$response = Invoke-RestMethod -Uri "https://leetcode.com/graphql" -Method Post -Headers $headers -Body $query
$response | ConvertTo-Json -Depth 10
"""

# Execute the command in PowerShell and get output
output = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)

# Extract JSON output
try:
    leetcode_data = json.loads(output.stdout)
    submission_stats = leetcode_data["data"]["matchedUser"]["submitStats"]["acSubmissionNum"]
except Exception as e:
    print("Error parsing LeetCode response:", e)
    exit(1)

# Create a new README content
readme_content = f"""
# LeetCode Solutions by SELFANUJ 🚀

## 📊 LeetCode Progress

| Difficulty | Problems Solved |
|------------|----------------|
"""

for stat in submission_stats:
    readme_content += f"| {stat['difficulty']} | {stat['count']} |\n"

# Write to README.md
with open("README.md", "w", encoding="utf-8") as file:
    file.write(readme_content)

print("✅ README.md updated successfully!")
