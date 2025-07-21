import numpy as np
import matplotlib.pyplot as plt

# Farklı kelimelerin hayali "özellik skorları"
categories = ["Canlılık", "Evcillik", "Boyut", "Tehlike", "Sevimlilik"]

kedi_scores = [0.9, 0.9, 0.3, 0.1, 0.8]
kopek_scores = [0.9, 0.95, 0.5, 0.2, 0.9]
aslan_scores = [0.9, 0.1, 0.8, 0.8, 0.4]
araba_scores = [0.0, 0.0, 0.6, 0.3, 0.2]

x = np.arange(len(categories))
width = 0.2

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x - 1.5 * width, kedi_scores, width, label="Kedi")
ax.bar(x - 0.5 * width, kopek_scores, width, label="Köpek")
ax.bar(x + 0.5 * width, aslan_scores, width, label="Aslan")
ax.bar(x + 1.5 * width, araba_scores, width, label="Araba")

ax.set_xlabel("Özellikler")
ax.set_ylabel("Skor")
ax.set_title("Kelimelerin Özellik Skorları (Basitleştirilmiş)")
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()
plt.show()
