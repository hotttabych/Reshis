import numpy as np
import matplotlib.pyplot as plt

n = 8  # кол-во страниц
k = 1000  # кол-во итераций
d = 0.85  # коэффициент затухания

nodes_s_outgoing_links = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['F', 'G'],
    'D': ['A', 'H'],
    'E': ['A', 'H'],
    'F': ['A'],
    'G': ['A'],
    'H': ['A']
}

# словарь кол-ва исходящих ссылок
outgoing_links_count = {key: len(nodes_s_outgoing_links[key]) for key in nodes_s_outgoing_links}

# матрица смежности
pages = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
index = {page: i for i, page in enumerate(pages)}

# создаём матрицу ссылок...
matrix_of_links = np.zeros((n, n))

# ...и заполняем её
for page, links in nodes_s_outgoing_links.items():
    i = index[page]
    for link in links:
        j = index[link]
        matrix_of_links[j, i] = 1 / outgoing_links_count[page]

# инициализируем значения рейтинга PageRank
pagerank = np.ones(n) / n

# тут будем хранить историю значений на каждой итерации
history = np.zeros((k, n))

# итерируем алгоритм ранжирования k раз
for it in range(k):
    # рассчитываем новый вектор значений
    pagerank = (1 - d) / n + d * matrix_of_links @ pagerank
    # сохраняем значения в историю
    history[it] = pagerank

# округляем финальные значения авторитетностей до двух знаков и выводим на экран
final_pagerank_ranks = {page: round(pagerank[index[page]], 2) for page in pages}
print("Финальные значения авторитетностей PageRank:")
for page, score in final_pagerank_ranks.items():
    print(f"{page}: {score}")

# строим график
plt.figure(figsize=(10, 6))
for i, page in enumerate(pages):
    plt.plot(history[:, i], label=f'Страница {page}')

plt.title("Изменение авторитетности страниц при k = 1000 итерациях")
plt.xlabel("Итерации")
plt.ylabel("Оценка алгоритма PageRank")
plt.legend()
plt.grid()
plt.show()

# готово! вы великолепны
