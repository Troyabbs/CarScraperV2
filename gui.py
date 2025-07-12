import tkinter as tk
from tkinter import ttk
from threading import Thread
import asyncio
from carScraper import runScraper

root = tk.Tk()
root.title("Car Scraper")
root.geometry("400x400")

tk.Label(root, text="Search Term").pack()
search_entry = ttk.Entry(root)
search_entry.pack()

tk.Label(root, text="Max Price").pack()
price_entry = ttk.Entry(root)
price_entry.pack()

tk.Label(root, text="Max Kilometers").pack()
km_entry = ttk.Entry(root)
km_entry.pack()

is_running = False
interval = None

def scraper_call():
    asyncio.run(runScraper(search_entry.get(), price_entry.get(), km_entry.get()))

def run_periodically():
    global interval
    thread = Thread(target=scraper_call)
    thread.start()
    interval = root.after(60000, run_periodically)

def start_scraper():
    global is_running, interval

    if not is_running:
        is_running = True
        button.config(text="Stop Scraper")
        run_periodically()
    else:
        is_running = False
        button.config(text="Start Scraper (runs every 10 seconds)")
        if interval:
            root.after_cancel(interval)
            interval = None

label = ttk.Label(root, text="Car Scraper")
label.pack(pady=10)

button = ttk.Button(root, text="Start Scraper (runs every 10 seconds)", command=start_scraper)
button.pack(pady=10)

root.mainloop()
