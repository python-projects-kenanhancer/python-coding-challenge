matrix = [[1, 2], [3, 4], [5, 6]]
flat = [item for row in matrix for item in row]
print(flat)


tags = ["Python", "python", "DevOps", "devops", "ML"]
unique_tags = {tag.lower() for tag in tags}
print(unique_tags)


tags_lower = [item.lower() for item in tags]
u_t = set(tags_lower)
print(u_t)


products_usd = {"apple": 1.0, "banana": 0.5}
USD_TO_GBP = 0.8
products_gbp = {
    product: round(price * USD_TO_GBP, 2) for product, price in products_usd.items()
}

print(products_gbp)
