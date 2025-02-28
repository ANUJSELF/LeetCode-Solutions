import requests
import json
import os

USERNAME = "SELFANUJ"
URL = f"https://leetcode.com/{USERNAME}"

headers = {
    "User-Agent": "Mozilla/5.0"
}

# Scrape solved problems from profile
response = requests.get(URL, headers=headers)
if response.status_code == 200:
    data = response.text
    solved_problems = set()
    
    start_idx = data.find('var pageData = ') + len('var pageData = ')
    end_idx = data.find('};', start_idx) + 1
    json_data = json.loads(data[start_idx:end_idx])

    if "submissionList" in json_data:
        for problem in json_data["submissionList"]:
            solved_problems.add(problem["title"])

    print("\n✅ Solved Problems List:")
    for problem in sorted(solved_problems):
        print(f"🔹 {problem}")

    # Update README.md
    with open("README.md", "w", encoding="utf-8") as file:
        file.write("# 🏆 LeetCode Solutions\n\n")
        file.write(f"✅ **Total Solved:** {len(solved_problems)} problems\n\n")
        file.write("## 🔹 Solved Problems\n")
        for problem in sorted(solved_problems):
            file.write(f"- {problem}\n")

    print("\n✅ README.md updated successfully!")

    # Commit & Push to GitHub
    os.system("git add README.md")
    os.system('git commit -m "Updated LeetCode Solutions"')
    os.system("git push origin main")

else:
    print("⚠️ Failed to fetch solved problems. Check if your profile is public.")
