from infra.repository.filmes_repository import FilmesRepository

repo = FilmesRepository()

repo.insert("Hulk", "Acao", 2002)
repo.delete("Vingadores")
repo.update("Vingadores 2", 2036)


data = repo.select()

print(data)
