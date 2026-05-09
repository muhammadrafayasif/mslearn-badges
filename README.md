# 🏅 Microsoft Learn Badges GitHub Action

Automatically scrape your **MS Learn badges** and generate a neat grid that you can use in your GitHub profile README.

---

## ✨ Features
- Scrapes all badges from a given **MS Learn username**  
- Dynamically updates the README of your profile to include all MS Learn badges
- Runs **daily** or on manual dispatch  
- Can be used as a **GitHub Action** or standalone script  

---

## 🚀 Usage

Add the following workflow to `.github/workflows/daily-badges.yml` in your repo:

>[!NOTE]
> Replace `mslearn-username` with your username from MS Learn

```yaml
name: Daily Microsoft Learn Badges

on:
  schedule:
    - cron: '0 12 * * *'  # runs daily at 12:00 UTC
  workflow_dispatch:       # manual trigger

jobs:
  fetch-badges:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v3

      - name: Fetch MS Learn Badges
        uses: muhammadrafayasif/MS Learn-badges@main
        with:
          mslearn-username: "[username]"
          output-path: "badges"
          
      - name: Commit updated badges
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add README.md
          git commit -m "chore: update MS Learn badges [skip ci]" || echo "No changes to commit"
          git push
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```
## 🖼️ Demonstration
<!-- START_MICROSOFT_LEARN_BADGES -->
<table border="0" cellspacing="0" cellpadding="0" width="800"><tr><td align="center" width="200"><a href="https://learn.microsoft.com/en-us/users/muhammadrafayasif"><img src="https://learn.microsoft.com/en-us/training/achievements/create-machine-learning-models.svg" height="100"/></a><br/><sub><b>Create machine learning models</b></sub></td><td align="center" width="200"><a href="https://learn.microsoft.com/en-us/users/muhammadrafayasif"><img src="https://learn.microsoft.com/en-us/training/achievements/train-and-evaluate-deep-learning-models.svg" height="100"/></a><br/><sub><b>Train and evaluate deep learning models</b></sub></td><td align="center" width="200"><a href="https://learn.microsoft.com/en-us/users/muhammadrafayasif"><img src="https://learn.microsoft.com/en-us/training/achievements/train-and-evaluate-regression-models.svg" height="100"/></a><br/><sub><b>Train and evaluate regression models</b></sub></td><td align="center" width="200"><a href="https://learn.microsoft.com/en-us/users/muhammadrafayasif"><img src="https://learn.microsoft.com/en-us/training/achievements/train-and-evaluate-clustering-models.svg" height="100"/></a><br/><sub><b>Train and evaluate clustering models</b></sub></td></tr></table><table border="0" cellspacing="0" cellpadding="0" width="800"><tr><td align="center" width="200"><a href="https://learn.microsoft.com/en-us/users/muhammadrafayasif"><img src="https://learn.microsoft.com/en-us/training/achievements/explore-and-analyze-data-with-python.svg" height="100"/></a><br/><sub><b>Explore and analyze data with Python</b></sub></td><td align="center" width="200"><a href="https://learn.microsoft.com/en-us/users/muhammadrafayasif"><img src="https://learn.microsoft.com/en-us/training/achievements/train-and-evaluate-classification-models.svg" height="100"/></a><br/><sub><b>Train and evaluate classification models</b></sub></td></tr></table>
<!-- END_MICROSOFT_LEARN_BADGES -->
