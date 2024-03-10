sandwich_orders = ['Avacado sandwich','pastrami','veg sandwich','egg katsu sandwich','pastrami','grilled cheese sandwich','pastrami']
finished_sandwichs = []

print("Sorry we have run out of pastrami sandwich")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    ordered = sandwich_orders.pop()
    print("I made your " + ordered.title())
    finished_sandwichs.append(ordered)



for finished_sandwich in finished_sandwichs:
    print(finished_sandwich)