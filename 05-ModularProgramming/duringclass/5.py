import statistics as st
zarobki = [21600, 4350, 3920, 5590, 3250, 4010]

print(f'Średnia: {st.mean(zarobki)}')
print(f'Mediana: {st.median(zarobki)}')
print(f'Odchylenie standardowe: {st.stdev(zarobki)}')