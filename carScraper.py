import asyncio
from playwright.async_api import async_playwright
from models.car import Car
import pandas as pd
from dataclasses import asdict

async def runScraper(searchterm: str, maxprice: str, maxkm: str):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        page = await browser.new_page()
        carlist = []
        for page_num in range(1, 2):
            await page.goto(f"https://www.trademe.co.nz/a/motors/cars/search?search_string={searchterm}&price_max={maxprice}&odometer_max={maxkm}&page={page_num}", wait_until="load")

            carqueries = []
            for cls in [
                "a.tm-tiered-search-card__link.o-card"
            ]:
                carqueries.extend(await page.query_selector_all(cls))

            if not carqueries:
                break

            for listing in carqueries:
                link = await listing.get_attribute("href")
                car = Car(
                    title=await (await listing.query_selector(".tm-motors-search-card-title__title")).inner_text(),
                    location=await (await listing.query_selector_all(".tm-search-card-attributes__attribute-text"))[0].inner_text(),
                    mileage=await (await listing.query_selector_all(".tm-search-card-attributes__attribute-text"))[1].inner_text(),
                    price=(await (await listing.query_selector(".tm-search-card-price__price")).inner_text()).replace("\n", " "),
                    url= f"https://www.trademe.co.nz{link}"
                )
                carlist.append(car)
                print(car)

        old_df = pd.read_csv("carlist.csv")
        new_df = pd.DataFrame([asdict(car) for car in carlist])
        keys = ["title", "location", "price"]
        new_df_keys = new_df[keys].apply(tuple, axis=1)
        old_df_keys = old_df[keys].apply(tuple, axis=1)
        new_listings = new_df[~new_df_keys.isin(old_df_keys)]
        if not new_listings.empty:
            print("New listings found:")
            print(new_listings)
        new_df.to_csv("carlist.csv", index=False)
        print("Done")
