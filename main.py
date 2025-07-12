from playwright.sync_api import sync_playwright, Playwright

from carScraper import runScraper

with sync_playwright() as playwright:
    runScraper(playwright)


    