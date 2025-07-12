import tkinter as tk
from tkinter import ttk
from tkinter import *
from threading import Thread
import asyncio
from carScraper import runScraper
import os

root = tk.Tk()
root.title("Trademe CarScraperV2 🚗")
root.geometry("400x400")

title_frame = ttk.Frame(root)
title_frame.pack(pady=(20, 20))
ttk.Label(title_frame, text="trade", font=("Verdana", 18, "bold"), foreground="#4a5de4").pack(side=tk.LEFT, padx=(0, 0))
ttk.Label(title_frame, text="me", font=("Verdana", 18, "bold"), foreground="#f5a623").pack(side=tk.LEFT, padx=(0, 0))
ttk.Label(title_frame, text=" CarScraperV2", font=("Verdana", 18, "bold")).pack(side=tk.LEFT)

tk.Label(root, text="Car Brand").pack()
brand_entry = ttk.Entry(root)
brand_entry.pack()

tk.Label(root, text="Car Model").pack()
model_entry = ttk.Entry(root)
model_entry.pack()

tk.Label(root, text="Max Price").pack()
price_entry = ttk.Entry(root)
price_entry.pack()

tk.Label(root, text="Max Kilometers").pack()
km_entry = ttk.Entry(root)
km_entry.pack()

is_running = False
interval = None

def scraper_call():
    asyncio.run(runScraper(brand_entry.get().strip().lower(), model_entry.get().strip().lower().replace(" ", "-"), price_entry.get().strip(), km_entry.get().strip()))

def run_periodically():
    global interval
    thread = Thread(target=scraper_call)
    thread.start()
    interval = root.after(60000, run_periodically)

def start_scraper():
    global is_running, interval

    if not is_running:
        is_running = True
        scraper_button.config(text="Stop Scraper")
        run_periodically()
    else:
        is_running = False
        scraper_button.config(text="Start Scraper (runs every 60 seconds)")
        if interval:
            root.after_cancel(interval)
            interval = None

def clear_csv():
    if os.path.exists("carlist.csv"):
        os.remove("carlist.csv")

def open_csv():
    if os.path.exists("carlist.csv"):
        os.startfile("carlist.csv")

scraper_button = ttk.Button(root, text="Start Scraper (runs every 10 seconds)", command=start_scraper)
scraper_button.pack(pady=(20,0))

clear_button = ttk.Button(root, text="Clear CSV", command=clear_csv)
clear_button.pack(pady=(10, 0))

open_button = ttk.Button(root, text="Open CSV", command=open_csv)
open_button.pack(pady=(10, 0))

root.mainloop()
