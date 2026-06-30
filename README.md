# Restaurant Resource Planning System – Self-Learning Forecaster

## Overview

This project was developed as a solution to the Restaurant Resource Planning System challenge.

The goal is to help a restaurant make better operational decisions by forecasting customer demand and using that forecast to plan staffing and inventory requirements. The system also includes a feedback mechanism that allows managers to submit actual results, enabling the forecasting process to improve over time.

The application predicts:

* Expected customer covers
* Staff requirements
* Ingredient demand
* Inventory replenishment needs

while taking shelf life and supplier lead times into account.

---

## Problem Statement

Restaurants often lose money due to poor planning.

Overestimating demand can result in:

* Excess staff scheduling
* Unused inventory
* Ingredient spoilage

Underestimating demand can result in:

* Staff shortages
* Stock shortages
* Poor customer experience

This project aims to reduce both problems by forecasting demand and generating resource planning recommendations.

---

## Approach

The solution is divided into four main stages:

1. Demand Forecasting
2. Staff Planning
3. Inventory Planning
4. Feedback-Based Learning

Historical sales data is used to train a forecasting model. The predicted customer count is then used to determine staffing requirements and ingredient demand. Inventory availability, shelf life, and supplier lead times are considered before generating ordering recommendations.

Managers can submit feedback when actual demand differs from the forecast. This feedback updates condition-specific coefficients that influence future predictions.

---

## System Architecture

```text
Historical Sales Data
          │
          ▼
   Demand Forecasting
      (XGBoost)
          │
          ▼
   Predicted Covers
          │
          ▼
   Resource Planner
      ├── Staff Planner
      ├── Menu Mix Planner
      └── Inventory Planner
          │
          ▼
 Resource Recommendations

          ▲
          │
      Feedback
          │
          ▼
  Coefficient Learning
          │
          ▼
 Future Forecast Adjustment
```

---

## Technologies Used

* Python
* FastAPI
* XGBoost
* Pandas
* Scikit-Learn
* Joblib
* Uvicorn

---

## Dataset

The dataset used for this project was generated for the assessment and simulates restaurant operations over a one-year period.

Files included:

```text
data/

historical_sales.csv
inventory.csv
recipes.csv
suppliers.csv
menu_mix.csv
feedback.csv
coefficients.json
```

### Historical Sales Data

Contains:

* Date
* Hour
* Day of Week
* Weather
* Promotion Flag
* Event Flag
* Covers

The generated data includes realistic patterns such as:

* Higher lunch demand
* Higher dinner demand
* Increased weekend traffic
* Weather impact
* Promotion impact
* Event impact

---

## Forecasting Model

An XGBoost Regressor is trained using historical sales data.

Features:

* Hour
* Day of Week
* Weather
* Promotion
* Event

Target:

* Covers

The model predicts expected customer demand for a given time period.

---

## Staff Planning

Staff requirements are calculated using simple business rules.

Example:

```text
1 Waiter per 20 customers
1 Chef per 40 customers
1 Bartender per 30 customers
```

The staffing recommendation is generated directly from the forecasted customer count.

---

## Inventory Planning

The system estimates menu item demand using a predefined menu mix.

Example:

```text
35% Beef Burger
25% Chicken Burger
25% French Fries
15% Soft Drink
```

Menu demand is converted into ingredient demand using recipe definitions.

The system then compares required ingredients with current inventory levels and generates ordering recommendations.

---

## Shelf Life Handling

Each ingredient contains shelf life information.

Example:

```text
Lettuce → 3 days
Tomato → 4 days
Burger Bun → 2 days
```

Shelf life information is included in the inventory planning output so that short-lived ingredients can be managed appropriately.

---

## Supplier Lead Times

Each ingredient has an associated supplier lead time.

Example:

```text
Burger Bun → 1 day
Beef Patty → 2 days
French Fries → 3 days
```

Lead times are included in inventory recommendations to support purchasing decisions.

---

## Self-Learning Feedback Loop

The forecasting system is designed to improve over time.

Managers can submit:

```json
{
  "predicted": 120,
  "actual": 85,
  "reason": "Rain"
}
```

The system calculates:

```text
Error
Error Ratio
```

Condition-specific coefficients are then updated.

Example:

```json
{
  "Rain": 0.78
}
```

Future forecasts are adjusted using these learned coefficients.

This creates a simple feedback loop that allows the system to adapt based on operational experience.

---

## API Endpoints

### Resource Planning

```http
POST /planner/plan-resources
```

Generates:

* Demand forecast
* Staff plan
* Ingredient demand
* Inventory recommendations

---

### Feedback Submission

```http
POST /feedback
```

Records actual results and updates learning coefficients.

---

### View Learned Coefficients

```http
GET /coefficients
```

Returns the current learned coefficients used by the forecasting system.

---

## Running the Project

Clone the repository:

```bash
git clone https://github.com/sreeku1993/Restaurant-Resource-Planning-System.git

cd Restaurant-Resource-Planning-System
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn main:app --reload
```

Swagger UI:

```text
http://localhost:8000/docs
```

---

## Assumptions

* Customer demand can be estimated using historical sales patterns.
* Menu mix percentages remain relatively stable.
* Staffing ratios are fixed business rules.
* Generated datasets are used for demonstration purposes.
* Coefficient learning is intentionally lightweight and designed to demonstrate feedback-driven adaptation.

---

## Future Improvements

Possible future enhancements include:

* Real weather API integration
* Holiday calendar integration
* Multi-restaurant support
* Automated retraining pipelines
* More advanced forecasting models
* Inventory optimization based on shelf-life windows
* Forecast accuracy dashboards

---

## Repository

GitHub Repository:

https://github.com/sreeku1993/Restaurant-Resource-Planning-System
