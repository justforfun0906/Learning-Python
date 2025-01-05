from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import random
import time

class GoogleMapsReviewScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
    
    def search_restaurants(self, location="台灣"):
        """Search for restaurants in the specified location"""
        self.driver.get("https://www.google.com/maps")
        
        # Wait for and find the search box
        search_box = self.wait.until(
            EC.presence_of_element_located((By.ID, "searchboxinput"))
        )
        search_box.clear()
        search_box.send_keys(f"餐廳 {location}")
        search_box.send_keys(Keys.RETURN)
        
        # Wait for results to load
        time.sleep(3)
    
    def get_random_restaurant(self):
        """Select a random restaurant from the results"""
        restaurants = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "div.V0h1Ob-haAclf")
            )
        )
        
        if restaurants:
            random_restaurant = random.choice(restaurants)
            random_restaurant.click()
            time.sleep(2)
            return True
        return False
    
    def get_reviews(self):
        """Get all reviews for the selected restaurant"""
        try:
            # Click on reviews button
            reviews_button = self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "button.HHrUdb-h3c3le")
                )
            )
            reviews_button.click()
            time.sleep(2)
            
            # Filter for 1-star reviews
            sort_button = self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "button[aria-label='排序評論']")
                )
            )
            sort_button.click()
            
            rating_filter = self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "span[aria-label='僅顯示 1 星評論']")
                )
            )
            rating_filter.click()
            time.sleep(2)
            
            # Collect reviews
            reviews = self.wait.until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, "span.wiI7pd")
                )
            )
            
            # Filter reviews with more than 10 words
            long_reviews = [
                review.text for review in reviews 
                if len(review.text.split()) > 10
            ]
            
            return long_reviews
        except TimeoutException:
            return []

    def get_random_long_one_star_review(self):
        """Main function to get a random 1-star review"""
        try:
            self.search_restaurants()
            
            if self.get_random_restaurant():
                reviews = self.get_reviews()
                
                if reviews:
                    return random.choice(reviews)
                else:
                    return "No long 1-star reviews found for this restaurant."
            else:
                return "No restaurants found."
                
        except Exception as e:
            return f"An error occurred: {str(e)}"
        
    def close(self):
        """Close the browser"""
        self.driver.quit()

def main():
    scraper = GoogleMapsReviewScraper()
    try:
        review = scraper.get_random_long_one_star_review()
        print("\nRandom 1-star review:")
        print("-" * 50)
        print(review)
        print("-" * 50)
    finally:
        scraper.close()

if __name__ == "__main__":
    main()