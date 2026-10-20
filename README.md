# OSRS ITEM LOOKUP

![GitHub Release](https://img.shields.io/github/v/release/DaRealDSA/OSRSItemLookUp)
![GitHub branch status](https://img.shields.io/github/checks-status/DaRealDSA/OSRSItemLookUp/master)
![GitHub Repo stars](https://img.shields.io/github/stars/DaRealDSA/OSRSItemLookUp)

Notice: This project is at its early stage of development, so bugs may expected

- Adding items into local JSON file
- Desktop notification system
- More item details

## ⚔️ OSRS API-Connected Item Lookup Tool

A robust, real-time data engine that connects your application to the live Old School RuneScape (OSRS) economy and game cache. This utility resolves item names into unique game IDs to pull instantly updated Grand Exchange (GE) market metrics, margins, and equipment metadata.

## 🚀 Key Features

• Real-Time Market Tracking: Fetches live, crowdsourced transaction data directly from the official OSRS Wiki Prices engine.
• Name Matching: Resolves human-readable item names (e.g., "Abyssal whip") into precise Jagex game IDs (4151).
• Margin Calculations: Automatically extracts the latest instant-sell (high) and instant-buy (low) thresholds to find high-yield trading spreads.

## 💻 Quick Start

### Install
1. Clone the repository:
   ```bash
   git clone https://github.com/DaRealDSA/OSRSItemLookUp && cd OSRSItemLookUp
   ```

### Prerequisites
Make sure you have the `requests` library installed in your python environment:
   ```bash
   pip install requirements.txt
   ```

2. Run:
   ```bash
   python3 main.py
   ```
