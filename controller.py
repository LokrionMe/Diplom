import view
import model


def start():
    list_figures = model.ListFigures()
    table = view.main_window(list_figures)
    table.mainloop()
