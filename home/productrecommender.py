from  sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import Product

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