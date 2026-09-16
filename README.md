# Django Product Recommender

A product recommendation system built with Django and Django REST Framework. The application uses product descriptions from an e-commerce dataset to find and recommend similar products.

The recommendation logic is based on TF-IDF vectorization and cosine similarity.

## Overview

The goal of this project was to build a simple content-based recommendation system and integrate it into a Django application.

For a selected product, the system compares its description with the descriptions of other products and returns the most similar products.

The overall flow is:

```text
Product Dataset
      |
      v
Django Product Model
      |
      v
Product Descriptions
      |
      v
TF-IDF Vectorization
      |
      v
Cosine Similarity
      |
      v
Similar Products
```

## How It Works

### 1. Product Data

The project uses an e-commerce product dataset containing product information such as product name, description, category, price, and image.

The product data is stored and accessed through Django's ORM.



### 2. TF-IDF

The product descriptions are converted into numerical vectors using `TfidfVectorizer` from scikit-learn.

TF-IDF represents the importance of words within the product descriptions while reducing the influence of commonly occurring words.

### 3. Cosine Similarity

The TF-IDF representation of the selected product is compared with other product descriptions using cosine similarity.

Products with higher similarity scores are considered more relevant and are returned as recommendations.

The current implementation returns the top 10 similar products.

## API Endpoints

### Get Products

```http
GET /api/products/
```

Returns the available products.

### Get Product and Recommendations

```http
GET /api/products/<id>/
```

Returns the selected product along with similar product recommendations.

## Tech Stack

- Python
- Django
- Django REST Framework
- scikit-learn
- SQLite
- HTML
- CSS
- Git
- GitHub

## Project Structure

```text
django-product-recommender/
│
├── home/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── productrecommender.py
│   └── ...
│
├── recommender/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
│
├── scripts.py
├── manage.py
├── requirements.txt
└── README.md
```

## Running the Project Locally

### Clone the repository

```bash
git clone https://github.com/vinayGopalapuram/django-product-recommender.git
cd django-product-recommender
```

### Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run migrations

```bash
python manage.py migrate
```

### Start the development server

```bash
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

## Recommendation Logic

The recommendation process can be summarized as:

```text
Selected Product
       |
       v
Product Description
       |
       v
TF-IDF Vector
       |
       v
Compare With Other Products
       |
       v
Cosine Similarity Scores
       |
       v
Sort By Similarity
       |
       v
Top 10 Similar Products
```

## What I Learned

This project gave me practical experience with:

- Building a Django application
- Creating REST APIs using Django REST Framework
- Working with Django models and serializers
- Using Django ORM for database operations
- Processing product data
- Implementing TF-IDF
- Using cosine similarity for content-based recommendations
- Integrating recommendation logic into a web application

## Future Improvements

Some areas I would like to improve in the future:

- Add automated tests for the APIs and recommendation logic
- Improve recommendations by considering product categories and other attributes
- Add pagination and filtering to the product API
- Improve API error handling
- Containerize the application using Docker
- Deploy the application to AWS
- Explore more advanced recommendation approaches

## Author

Vinay Gopalapuram

GitHub: https://github.com/vinayGopalapuram
