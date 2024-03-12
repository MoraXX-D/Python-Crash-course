def print_model(unprinted_model,completed_model):
    while unprinted_model:
        current_design = unprinted_model.pop()
        print("printing " + 
              current_design.title() + " is in progress")
        completed_model.append(current_design)

def show_model(completed_model):
    for models in completed_model:
        print(models.title() + " is printed successfully")

unprinted_model = ['iphone case', 'samsung case', 'pendent',]
unprinted_model_copy = unprinted_model[:]  #copy of original list using slice
completed_model = []

print_model(unprinted_model_copy,completed_model)
show_model(completed_model)

#original list is entact
print(unprinted_model)
print(completed_model)