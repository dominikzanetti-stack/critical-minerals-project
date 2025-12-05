# Critical Minerals Project - Design Document

## 1. Project Overview
An interactive web application to visualize critical minerals, their supply chains, and market data.
**Goal:** Educational tool to explore mining locations, refining capacity, and economic importance of rare earth elements.

## 2. User Flow
1.  **Landing Page:**
    * Visual Periodic Table.
    * Elements color-coded by category (e.g., Critical, Rare Earth, Strategic).
    * User clicks an element symbol (e.g., "Li").
2.  **Detail Page:**
    * Redirects to a specific view for that element.
    * **Map:** Displays top 5-10 producing and refining countries.
    * **Charts:** Commodity price history (last 10 years).
    * **Info:** Wikipedia link, main uses, and importance text.

## 3. Tech Stack
* **Language:** Python
* **Interface:** Streamlit
* **Data Handling:** Pandas

## 4. Data Requirements (To Do)
We need a data structure that can hold:
* Basic Element Info (Symbol, Name, Category).
* Production Data (Country List + Market Share percentages).
* Price Data (Year + Price for the last 10 years).
* Text Content (Description, Uses, Wiki Links).