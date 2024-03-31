import reflex as rx
from dataPortfolio.pages.index import index
from dataPortfolio.pages.pokedata import pokedata

app = rx.App()

app.add_page(index)
app.add_page(pokedata, route="/pokedata")