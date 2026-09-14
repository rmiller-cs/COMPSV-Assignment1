from product_data import products

# lets the user input their preferences and stores them
customer_preferences = []
response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    customer_preferences.append(preference)
    response = input("Do you want to add another preference? (Y/N): ").upper()


# converts the preferences to a set to remove duplicates
converted_preferences = set(customer_preferences)


# converts the product tags to sets to allow for faster comparisons
converted_products = []
for product in products:
    product["tags"] = set(product["tags"])
    converted_products.append(product)

# determines the number of mathching tags for a product
def count_matches(product_tags, customer_tags):
    matches = product_tags.intersection(customer_tags)
    return len(matches)


# returns the products that match the customer's preferences
def recommend_products(products, customer_tags):
    recommended_products = []
    for product in products:
        matches = count_matches(product["tags"], customer_tags)
        if matches > 0:
            recommended_products.append([product["name"], matches])
    return recommended_products


# runs the function and prints recommended products
print(recommend_products(converted_products, converted_preferences), sep="\n")


# DESIGN MEMO:
# 1. What core operations did you use (e.g., intersections, loops)? Why?
# Loops were used for most of the functions in order to iterate over lists. 
# A loop is used to iterate over each product and convert their tags into a set.
# recommend_products iterates over each product to check if they match the customer's preferences.
# An intersection is used in the count_matches function since it concisely filters which tags match the customer's preferences.
#
# 2. How might this code change if you had 1000+ products?
# If there were significantly more products, I would consider adding additional options to the product recommendations.
# One idea is an option to only suggesting products that match all recommendations 
# in order to reduce the amount of products the consumer has to sift through.
# Another thing I would change is sorting based on the amount of matching tags, since it is currently unsorted.
