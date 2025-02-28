import requests
import json
import matplotlib.pyplot as plt

USERNAME = "SELFANUJ"
GRAPHQL_URL = "https://leetcode.com/graphql"

HEADERS = {
    "Content-Type": "application/json",
    "Referer": "https://leetcode.com"
}

QUERY = """
{
    matchedUser(username: "%s") {
        submitStats {
            acSubmissionNum {
                difficulty
                count
            }
        }
    }
}
""" % USERNAME

def fetch_leetcode_stats():
    response = requests.post(GRAPHQL_URL, json={"query": QUERY}, headers=HEADERS)
    data = response.json()
    return data["data"]["matchedUser"]["submitStats"]["acSubmissionNum"]

def generate_graph(stats):
    difficulties = ["Easy", "Medium", "Hard"]
    counts = [stats[1]["count"], stats[2]["count"], stats[3]["count"]]

    plt.figure(figsize=(6, 4))
    plt.bar(difficulties, counts, color=["green", "orange", "red"])
    plt.xlabel("Difficulty")
    plt.ylabel("Problems Solved")
    plt.title(f"LeetCode Progress of {USERNAME}")
    plt.savefig("leetcode_graph.png")  # Save image
    print("✅ LeetCode graph saved as 'leetcode_graph.png'")

def update_readme(stats):
    readme_content = f"""
# 🚀 LeetCode Progress of {USERNAME}

![LeetCode Graph](leetcode_graph.png)

**Total Solved:** {stats[0]["count"]}  
- 🟢 Easy: {stats[1]["count"]}
- 🟠 Medium: {stats[2]["count"]}
- 🔴 Hard: {stats[3]["count"]}

| Difficulty | Problems Solved |
|------------|----------------|
| 🟢 Easy   | {stats[1]["count"]} |
| 🟠 Medium | {stats[2]["count"]} |
| 🔴 Hard   | {stats[3]["count"]} |

🔥 Updated daily with **GitHub Actions**!  
"""
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

if __name__ == "__main__":
    stats = fetch_leetcode_stats()
    generate_graph(stats)
    update_readme(stats)
    print("✅ README.md updated successfully!")
