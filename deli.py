sandwich_orders = ['Avacado sandwich','veg sandwich','egg katsu sandwich','grilled cheese sandwich']
finished_sandwichs = []

while sandwich_orders:
    ordered = sandwich_orders.pop()
    print("I made your " + ordered.title())
    finished_sandwichs.append(ordered)

for finished_sandwich in finished_sandwichs:
    print(finished_sandwich)