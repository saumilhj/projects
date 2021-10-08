from bs4 import BeautifulSoup
import requests as req
import csv

MAIN_URL = "https://www.allrecipes.com/recipes/"
main_res = req.get(MAIN_URL)
main_soup = BeautifulSoup(main_res.content, "html.parser")
all_categories_names = [category.text for category in main_soup.select(".recipeCarousel__listItem .carouselNav__linkText")]
# print(all_categories_names)
all_categories_links = [link.get("href") for link in main_soup.select(".recipeCarousel__listItem .recipeCarousel__link")]
# print(all_categories_links)
total_recipes_per_category = []
for link in all_categories_links:
    new_url = link
    new_res = req.get(new_url)
    new_soup = BeautifulSoup(new_res.content, "html.parser")
    total = len(new_soup.select(".recipeCarousel__list .recipeCarousel__listItem"))
    total_recipes_per_category.append(total)
# print(total_recipes_per_category)
all_rows = [['SN', 'Category', 'Link', 'Total Recipes']]
for i in range(0, len(all_categories_names)):
    new_row = [i, all_categories_names[i], all_categories_links[i], total_recipes_per_category[i]]
    all_rows.append(new_row)
with open("recipe.csv", mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(all_rows)
