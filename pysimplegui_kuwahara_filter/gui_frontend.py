import PySimpleGUI as sg
from PySimpleGUI import Window


class Widget:
    """
    GUI widget definition
    """
    # parameter input
    label_spin = sg.Text('Param')
    spin_box_param = sg.Spin(values=[i for i in range(1, 21)],
                             initial_value=5,
                             size=(5, 5),
                             key='parameter',
                             enable_events=True)

    # folder browse and show filelist
    input_folder_name = sg.InputText(key="photo_folder", change_submits=True, size=(15, 1))
    folder_browse = sg.FolderBrowse(target="photo_folder")
    list_box_files = sg.Listbox(values=[''],
                                change_submits=True,
                                size=(15, 15),
                                font=("Helvetica", 12),
                                key="files_listbox")

    # show kuwahara image button and save
    button_show_kuwahara = sg.Button('Filter', key='filter')
    button_save = sg.Button('Save', key='save')
    # exit button
    button_exit = sg.Button('Exit', key='exit', pad=((0, 0), (10, 0)))

    # input and output image
    image_input = sg.Image(key="image_input", size=(800, 600))
    image_output = sg.Image(key="image_output", size=(800, 600))


class Frontend(Widget):
    """
    GUI frontend(layout) definition
    """
    window_title: str = 'Pysimple Kuwahara Editor'
    window_size: tuple = (1300, 600)

    def column_left(self) -> list:
        """
        gui left side, its control area
        """
        col_param = sg.Column([[self.label_spin],
                               [self.spin_box_param]], vertical_alignment='bottom')

        col_control = sg.Column([[self.button_show_kuwahara, self.button_save]], vertical_alignment='bottom')
        frame_control = sg.Frame('control', [
            [col_param, col_control]
        ])

        frame_file_list = sg.Frame('Choice Folder And Picture', [
            [self.input_folder_name, self.folder_browse],
            [self.list_box_files]
        ])

        return [
            [frame_file_list],
            [sg.T('Input Param And Update...', pad=((0, 0), (10, 0)))],
            [frame_control],
            [self.button_exit]
        ]

    def column_center(self) -> list:
        """
        gui center, its input image area
        """
        return [[self.image_input]]

    def column_right(self) -> list:
        """
        gui right side, its output image are
        """
        return [[self.image_output]]

    def layout(self) -> list:
        """
        return GUI Layout
        """
        return [
            [sg.Column(self.column_left(), pad=(0, 0), vertical_alignment='t'),
             sg.Column(self.column_center(), pad=(10, 30), vertical_alignment='t'),
             sg.Column(self.column_right(), pad=(10, 30), vertical_alignment='t')],
        ]

    def window(self) -> Window:
        """
        return GUI Window
        """
        return sg.Window(self.window_title, size=self.window_size, finalize=True, layout=self.layout())
