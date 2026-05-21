import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'recommender.settings'
django.setup()



# import csv
# csv_file_path = 'flipkart_com-ecommerce_sample.csv'
# from home.models import *



# success_count = 0
# error_count = 0

# with open(csv_file_path, mode='r', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
    
#     for row in reader:
#         try:
#             product_name = row['product_name']
#             product_image = eval(row['image'])[0]  # First image from list
#             description = row['description']
#             category = row['product_category_tree'].split('>>')[0].strip('[]"')  # Extract last category
#             price = row['retail_price']

#             print(
#                 product_name,
#                 product_image,
#                 description,
#                 category,
#                 price,
#             )
#             #time.sleep(1)

#             # Create or update product
#             Product.objects.update_or_create(
#                 p_name=product_name,
#                 defaults={
#                     'p_image': product_image,
#                     'p_desc': description,
#                     'p_category': category,
#                     'p_price': price
#                  }
#             )
#             success_count+=1

#         except Exception as e:
#             error_count+=1
#             print(f"Error:{e}")

# print(f"{success_count} products imported successfully")
# print(f"{error_count} products failed")

from  sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from home.models import Product

def get_similar_products(product_id,top_n=10):
    vectorizer=TfidfVectorizer(stop_words="english") #it is used to skip regular english words such as "in , as , and , the ....."

    product_descriptions = Product.objects.all().values_list('p_desc',flat=True) #to get desc to rank all

    tfid_matrix= vectorizer.fit_transform(product_descriptions)   #this will generate a 2d array and assign values eg: [[],[]]

    target_product=Product.objects.get(id=product_id)

    #now comapare with all the products with target product

    all_products=list(Product.objects.all()) # convert to list to get the index

    target_index=all_products.index(target_product)# helps to find the index of the target product

    #now pass the target product into cosine similarity,here we passed the whole matrix (tfid_matrix) and the target product index(target_index)

    cos_sim= cosine_similarity(tfid_matrix[target_index],tfid_matrix).flatten()

    #here cos_sim.argsort() returns the indices in ascending order and [::-1] reverses it and [1:top_n+1] skips the first poroduct and returns the mext 10 products
    
    similar_indices=cos_sim.argsort()[::-1][1:top_n+1]

    similar_indices=[i for i in similar_indices if i != target_index]

    sim_product=[]
    for idi in similar_indices:
        sim_product.append(all_products[idi])
    return sim_product

print(get_similar_products(2616))