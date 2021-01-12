import pickle
sizes = []
for i in range(1,1_000_000):
    size = (i**2)*3
    sizes.append(size)
with open("sizes.pkl","wb") as f:
    pickle.dump(sizes,f)