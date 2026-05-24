# Vendor Management System

A Django + DRF REST API for managing vendors, purchase orders, and rolling performance metrics (on-time delivery, quality, response time, fulfilment rate).

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python)](https://www.python.org)
[![Django](https://img.shields.io/badge/Django-4.2-092E20?logo=django)](https://www.djangoproject.com)
[![DRF](https://img.shields.io/badge/Django_REST_Framework-3.14-A30000)](https://www.django-rest-framework.org)
[![Postgres](https://img.shields.io/badge/Database-PostgreSQL-336791?logo=postgresql)](https://www.postgresql.org)

---

## What it does

Tracks vendors and the purchase orders raised against them, and automatically maintains four performance metrics per vendor:

| Metric                     | How it's computed                                            |
|----------------------------|--------------------------------------------------------------|
| On-time delivery rate      | % of completed POs delivered on or before the delivery date  |
| Quality rating average     | Mean `quality_rating` across the vendor's completed POs      |
| Average response time      | Mean delta between `issue_date` and `acknowledgment_date`    |
| Fulfilment rate            | % of POs that reached `completed` (vs cancelled/pending)     |

A `HistoricalPerformance` row is snapshotted via Django signals so trends are queryable over time.

---

## Tech

- **Framework**: Django 4.2 + Django REST Framework 3.14
- **Database**: PostgreSQL (SQLite works for local dev too)
- **Config**: `python-dotenv` for environment-driven settings
- **Patterns**: class-based views, serializers, signals (`post_save` on `PurchaseOrder` recalculates metrics)

---

## Models

```
Vendor
├── name, contact_details, address, vendor_code (unique)
└── on_time_delivery_rate, quality_rating_avg,
    average_response_time, fulfillment_rate

PurchaseOrder
├── po_number (unique), vendor (FK), order_date, delivery_date
├── items (JSONField), quantity, status
└── quality_rating, issue_date, acknowledgment_date

HistoricalPerformance
├── vendor (FK), date
└── on_time_delivery_rate, quality_rating_avg,
    average_response_time, fulfillment_rate
```

---

## API Endpoints

| Method | Path                                         | Purpose                          |
|--------|----------------------------------------------|----------------------------------|
| GET / POST  | `/api/vendors/`                         | List or create vendors           |
| GET / PUT / DELETE | `/api/vendors/<vendor_id>/`     | Retrieve, update, delete vendor  |
| GET / POST  | `/api/purchase_orders/`                 | List or create purchase orders   |
| GET / PUT / DELETE | `/api/purchase_orders/<po_id>/` | Retrieve, update, delete PO      |

---

## Running Locally

```bash
git clone https://github.com/buhtig47/VendorManagementSystem.git
cd VendorManagementSystem/vendor_management

# 1. Virtual environment
python -m venv venv
source venv/bin/activate           # Windows: venv\Scripts\activate

# 2. Dependencies
pip install -r requirements.txt

# 3. Environment
cp .env.example .env
# edit .env — set SECRET_KEY, DB credentials, etc.

# 4. Database
python manage.py migrate
python manage.py createsuperuser

# 5. Run
python manage.py runserver
```

- API: `http://localhost:8000/api/`
- Admin: `http://localhost:8000/admin/`

---

## Repository Layout

```
VendorManagementSystem/
├── README.md
├── .gitignore
└── vendor_management/             Django project root (run manage.py from here)
    ├── manage.py
    ├── requirements.txt
    ├── .env.example
    ├── vendor_management/         settings package
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py / asgi.py
    └── vendor/                    main app
        ├── models.py              Vendor, PurchaseOrder, HistoricalPerformance
        ├── serializers.py
        ├── views.py
        ├── urls.py
        ├── signals.py             auto-recalculates metrics on PO save
        ├── mixins.py
        └── migrations/
```

---

## Notes

- This was an assignment/portfolio project demonstrating Django + DRF fundamentals: REST endpoints, model relationships, signals for derived state, and `.env`-driven configuration.
- For production use, add JWT/token auth, pagination, request validation, and rate limiting on the API.
