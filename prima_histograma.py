import matplotlib.pyplot as plt
import numpy as np

lista_gauss = np.random.normal(0, 1, 1000)

plt.hist(lista_gauss, bins = 100 )
plt.show()