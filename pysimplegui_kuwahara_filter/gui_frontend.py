import PySimpleGUI as sg


class Frontend:

    @staticmethod
    def column_left() -> list:
        widget_spin_label = sg.Text('Param')
        spin_values = [i for i in range(1, 21)]
        widget_spin_box = sg.Spin(values=spin_values,
                                  initial_value=5,
                                  size=(5, 5),
                                  key='parameter',
                                  enable_events=True)

        col_param = sg.Column([[widget_spin_label],
                               [widget_spin_box]], vertical_alignment='bottom')

        widget_exit_button = sg.Button('Exit', key='exit', pad=((0, 0), (10, 0)))
        widget_show_kuwahara_button = sg.Button('Filter', key='filter')
        widget_save_button = sg.Button('Save', key='save')
        col_control = sg.Column([[widget_show_kuwahara_button, widget_save_button]], vertical_alignment='bottom')
        frame_control = sg.Frame('control', [
            [col_param, col_control]
        ])

        widget_folder_name = sg.InputText(key="photo_folder", change_submits=True, size=(15, 1))
        widget_folder_browse = sg.FolderBrowse(target="photo_folder")
        widget_list_box = sg.Listbox(values=[''],
                                     change_submits=True,  # trigger an event whenever an item is selected
                                     size=(15, 15),
                                     font=("Helvetica", 12),
                                     key="files_listbox")
        frame_file_list = sg.Frame('Choice Folder And Picture', [
            [widget_folder_name, widget_folder_browse],
            [widget_list_box]
        ])

        return [
            [frame_file_list],
            [sg.T('Input Param And Update...', pad=((0, 0), (10, 0)))],
            [frame_control],
            [widget_exit_button]
        ]

    @staticmethod
    def column_center() -> list:
        return [[sg.Image(key="image_input", size=(800, 600))]]

    @staticmethod
    def column_right() -> list:
        return [[sg.Image(key="image_output", size=(800, 600))]]

    def layout(self) -> list:
        return [
            [sg.Column(self.column_left(), pad=(0, 0), vertical_alignment='t'),
             sg.Column(self.column_center(), pad=(10, 30), vertical_alignment='t'),
             sg.Column(self.column_right(), pad=(10, 30), vertical_alignment='t')],
        ]
