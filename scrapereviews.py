import requests
from dotenv import load_dotenv
import os
import json
import time

load_dotenv()

def get_reviews(asin):
    url = "https://real-time-amazon-data.p.rapidapi.com/product-reviews"
    querystring = {
        "asin": asin,
        "country": "US",
        "sort_by": "TOP_REVIEWS",
        "star_rating": "ALL",
        "verified_purchases_only": "false",
        "images_or_videos_only": "false",
        "current_format_only": "false",
        "page": "1"
    }
    headers = {
        "x-rapidapi-key": os.getenv('RAPID_API_KEY'),
        "x-rapidapi-host": "real-time-amazon-data.p.rapidapi.com"
    }
    
    print(f"Fetching reviews for ASIN: {asin}")
    response = requests.get(url, headers=headers, params=querystring)
    print(f"Response status code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        reviews = data.get('data', {}).get('reviews', [])
        simplified_reviews = [{
            'review_title': review.get('review_title'),
            'review_comment': review.get('review_comment'),
            'review_star_rating': review.get('review_star_rating'),
            'helpful_vote_statement': review.get('helpful_vote_statement')
        } for review in reviews]
        return simplified_reviews
    else:
        print(f"Error response: {response.text}")
    return []

# Read the bestsellers file
try:
    with open('bestsellers.json', 'r') as file:
        bestsellers = json.load(file)
        total_items = sum(len(category['items']) for category in bestsellers)
        print(f"Loaded {len(bestsellers)} categories with {total_items} total items")
except Exception as e:
    print(f"Error loading bestsellers.json: {e}")
    exit(1)

# Process each item in each category
for category in bestsellers:
    print(f"\nProcessing category: {category['category']}")
    for item in category['items']:
        asin = item.get('asin')
        if asin:
            print(f"Processing item with ASIN: {asin}")
            time.sleep(1)
            reviews = get_reviews(asin)
            item['amazon_reviews'] = reviews
            print(f"Added {len(reviews)} reviews")

# Save the updated data back to file
try:
    with open('bestsellers_with_reviews.json', 'w') as file:
        json.dump(bestsellers, file, indent=2)
        print("\nSuccessfully saved bestsellers_with_reviews.json")
except Exception as e:
    print(f"Error saving file: {e}")