# Vendor Management System

## Overview

This project is a Vendor Management System built using Django and Django REST Framework. It includes models for managing vendor profiles, purchase orders, and historical performance metrics.

## Features

- **Vendor Profiles:** Store essential information about each vendor, including performance metrics.
- **Purchase Orders:** Capture details of each purchase order and calculate various performance metrics.
- **Historical Performance:** Optionally store historical data on vendor performance for trend analysis.

## Project Structure

The project consists of the following Django apps:

- `vendor`: The main app containing models for Vendor, PurchaseOrder, and HistoricalPerformance.
- `api`: A Django app for handling API views and serializers.

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd vendor_management
    ```

2. Create a virtual environment and install dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Apply database migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Create a superuser for the Django admin:

    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the Django admin at `http://localhost:8000/admin/` to manage vendors, purchase orders, and historical performance.

7. Access the API at `http://localhost:8000/api/` for CRUD operations on vendors, purchase orders, and historical performance.

## API Endpoints

- `/api/vendors/`: List and create vendor profiles.
- `/api/purchase-orders/`: List and create purchase orders.
- `/api/vendor-performance/<int:pk>/`: Retrieve and update historical performance for a vendor.

## Additional Notes

- The project includes Django REST Framework for building the API.
- Authentication and authorization mechanisms are recommended for securing API endpoints in a production environment.

