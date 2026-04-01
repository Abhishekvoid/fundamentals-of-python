# Ride-Share API

Simple FastAPI backend for ride booking like Uber/Rapido. Built with Pydantic models and proper service layer.

## Quick Start

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://localhost:8000/docs for Swagger UI.

## API Endpoints

**POST /api/v1/rides**
```json
{
  "rider_id": "r1",
  "pickup": {"lat": 23.0225, "lng": 72.5714},
  "dropoff": {"lat": 23.0333, "lng": 72.5667},
  "vehicle_type": "bike"
}
```

**GET /api/v1/drivers** - List available drivers

## Features

- Pydantic models (User, Driver, RideRequest, Ride) with geo validation
- Haversine distance calculation between locations
- Fare estimation based on vehicle type + distance
- Driver matching within 5km radius
- pytest tests included
- Docker ready

## Tech Stack

- FastAPI 0.115+
- Pydantic v2
- Python 3.12

## Run Tests

```bash
pytest tests/ -v
```

## Local Development

Ahmedabad coordinates used for sample drivers:
- Driver Raj (bike): Navrangpura area  
- Auto Sharma: ~2km away

Works with your existing Django/Qdrant setup patterns.

---
Built for learning ride-sharing backend design.