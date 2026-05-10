# 🏅 Microsoft Learn Badges GitHub Action

Automatically scrape your **Microsoft Learn badges** and generate a neat grid that you can use in your GitHub profile README.

---

## ✨ Features
- Scrapes all badges from a given **Microsoft Learn username**  
- Dynamically updates the README of your profile to include all MS Learn badges
- Runs **daily** or on manual dispatch  
- Can be used as a **GitHub Action** or standalone script  

---

## 🚀 Usage

Add the following workflow to `.github/workflows/daily-badges.yml` in your repo:

>[!NOTE]
> Replace `mslearn-username` with your username from Microsoft Learn

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

      - name: Fetch Microsoft Learn Badges
        uses: muhammadrafayasif/mslearn-badges@main
        with:
          mslearn-username: "[username]"
          output-path: "badges"
          
      - name: Commit updated badges
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add README.md
          git commit -m "chore: update Microsoft Learn badges [skip ci]" || echo "No changes to commit"
          git push
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```
## 🖼️ Demonstration
<!-- START_MICROSOFT_LEARN_BADGES -->
<a href="learn.microsoft.com/en-us/users/muhammadrafayasif/achievements"><img alt="Create machine learning models" src="https://learn.microsoft.com/en-us/training/achievements/create-machine-learning-models.svg" height="100" width="100"/></a>
<a href="learn.microsoft.com/en-us/users/muhammadrafayasif/achievements"><img alt="Train and evaluate deep learning models" src="https://learn.microsoft.com/en-us/training/achievements/train-and-evaluate-deep-learning-models.svg" height="100" width="100"/></a>
<a href="learn.microsoft.com/en-us/users/muhammadrafayasif/achievements"><img alt="Train and evaluate regression models" src="https://learn.microsoft.com/en-us/training/achievements/train-and-evaluate-regression-models.svg" height="100" width="100"/></a>
<a href="learn.microsoft.com/en-us/users/muhammadrafayasif/achievements"><img alt="Train and evaluate clustering models" src="https://learn.microsoft.com/en-us/training/achievements/train-and-evaluate-clustering-models.svg" height="100" width="100"/></a>
<a href="learn.microsoft.com/en-us/users/muhammadrafayasif/achievements"><img alt="Explore and analyze data with Python" src="https://learn.microsoft.com/en-us/training/achievements/explore-and-analyze-data-with-python.svg" height="100" width="100"/></a>
<a href="learn.microsoft.com/en-us/users/muhammadrafayasif/achievements"><img alt="Train and evaluate classification models" src="https://learn.microsoft.com/en-us/training/achievements/train-and-evaluate-classification-models.svg" height="100" width="100"/></a>
<!-- END_MICROSOFT_LEARN_BADGES -->
