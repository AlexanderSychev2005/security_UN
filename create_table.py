import pandas as pd

p = 31
elements = list(range(1, p))

df = pd.DataFrame(index=elements, columns=elements)

# a^j mod p
for a in elements:
    for j in elements:
        df.at[a, j] = pow(a, j, p)


df.to_csv("gf31_table.csv", index_label=r"a \ j")
print("Table for GF(31) is ready!")
