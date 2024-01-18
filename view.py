import tkinter as tk
import model


def add_figure(length, width, list_figures: model.ListFigures):
    new_figure = model.Figure(length, width)
    list_figures.add_figure(new_figure)
    list_show_book.insert('end', list_figures.get_list_figures()[-1])


def change_figure(length, width, list_figures: model.ListFigures):
    selection = list_show_book.curselection()[0]
    ch_figure = list_figures.get_list_figures()[selection]
    ch_figure.update(length, width)
    list_show_book.delete(selection)
    list_show_book.insert(
        selection, list_figures.get_list_figures()[selection])


def delete_position(list_figures: model.ListFigures):
    selection = list_show_book.curselection()[0]
    list_show_book.delete(selection)
    list_figures.get_list_figures().pop(selection)


def update_result(list_figures):
    if len(list_figures) == 0:
        return 'Input figures'
    else:
        lbl_def_result['text'] = f'{model.all_area_figures(list_figures)} workpiece necessary'


def main_window(list_figures: model.ListFigures):
    global list_show_book
    global lbl_def_result
    window_main = tk.Tk()
    window_main.title('Settlement book')
    window_main.resizable(width=False, height=False)

    frm_spaces = tk.Frame(master=window_main)
    ent_length = tk.Entry(master=frm_spaces,
                          width=10)
    ent_width = tk.Entry(master=frm_spaces,
                         width=10)
    list_show_book = tk.Listbox(master=frm_spaces,
                                height=11,
                                width=40,
                                bg='white',
                                listvariable=tk.StringVar(value=list_figures.get_list_figures()))
    lbl_txt_length = tk.Label(master=frm_spaces,
                              text='Length:')
    lbl_txt_width = tk.Label(master=frm_spaces,
                             text='Width:')
    lbl_txt_result = tk.Label(master=frm_spaces,
                              text='Result:')
    lbl_def_result = tk.Label(master=frm_spaces,
                              text=update_result(list_figures))
    frm_buttons = tk.Frame(master=window_main)
    btn_add = tk.Button(master=frm_buttons,
                        text='Add figure',
                        command=lambda: add_figure(ent_length.get(), ent_width.get(), list_figures))
    btn_ch_figure = tk.Button(master=frm_buttons,
                              text='Change figure',
                              command=lambda: change_figure(ent_length.get(), ent_width.get(), list_figures))
    btn_result = tk.Button(master=frm_buttons,
                           text='Result',
                           command=lambda: update_result(list_figures))
    btn_delete_figure = tk.Button(master=frm_buttons,
                                  text='Delete figure',
                                  command=lambda: delete_position(list_figures))
    btn_exit = tk.Button(master=frm_buttons,
                         text='Exit',
                         command=window_main.destroy)

    frm_buttons.grid(row=0,
                     column=0)
    btn_add.grid(row=0,
                 column=0,
                 sticky='we',
                 pady=10,
                 padx=5)
    btn_ch_figure.grid(row=1,
                       column=0,
                       sticky='we',
                       pady=10,
                       padx=5)
    btn_delete_figure.grid(row=3,
                           column=0,
                           sticky='we',
                           pady=10,
                           padx=5)
    btn_result.grid(row=4,
                    column=0,
                    sticky='we',
                    pady=10,
                    padx=5)
    btn_exit.grid(row=5,
                  column=0,
                  sticky='we',
                  pady=10,
                  padx=5)

    frm_spaces.grid(row=0,
                    column=1)
    lbl_txt_length.grid(row=0,
                        column=0,
                        sticky='w',
                        padx=5)
    ent_length.grid(row=0,
                    column=1,
                    sticky='w',
                    padx=5)
    lbl_txt_width.grid(row=0,
                       column=2,
                       sticky='w',
                       padx=5)
    ent_width.grid(row=0,
                   column=3,
                   sticky='w',
                   padx=5,)
    list_show_book.grid(row=1,
                        column=0,
                        columnspan=4,
                        pady=10,
                        sticky='w')
    lbl_txt_result.grid(row=2,
                        column=0,
                        sticky='w',
                        padx=5,
                        pady=10)
    lbl_def_result.grid(row=2,
                        column=1,
                        columnspan=3,
                        sticky='w',
                        padx=5,
                        pady=10)
    return window_main
