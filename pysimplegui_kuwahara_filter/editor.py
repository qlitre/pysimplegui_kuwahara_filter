import PySimpleGUI as sg
from pysimplegui_kuwahara_filter.kuwahara import get_kuwahara_filtered_pic
from pysimplegui_kuwahara_filter import utils
from pysimplegui_kuwahara_filter.gui_frontend import Frontend
from pathlib import Path
import os
from PIL import Image
from PySimpleGUI import Window


class Editor:
    window_title = 'Pysimple Kuwahara Editor'
    window_size = (1300, 600)
    layout = Frontend().layout()

    def __init__(self):
        self.file_name = ''
        self.parameter = 5
        self.kuwahara_image = None
        self.window = self.window()

    def set_file_name(self, file_name: str) -> None:
        self.file_name = file_name

    def set_parameter(self, param: int) -> None:
        self.parameter = param

    def set_kuwahara_image(self, kuwahara_image: Image) -> None:
        self.kuwahara_image = kuwahara_image

    def window(self) -> Window:
        return sg.Window(self.window_title, size=self.window_size).Layout(self.layout)

    def show_image(self) -> None:
        pic = utils.get_image_by_file_name(self.file_name)
        pic_data = utils.get_picture_data(pic)
        self.window.find_element("image_input").Update(data=pic_data)

    def show_kuwahara_image(self) -> None:
        filtered_pic = get_kuwahara_filtered_pic(self.file_name, r=self.parameter)
        kuwahara_image = utils.get_image_by_kuwahara_filter(filtered_pic)
        self.set_kuwahara_image(kuwahara_image)
        kuwahara_data = utils.get_picture_data(kuwahara_image)
        self.window.find_element("image_output").Update(data=kuwahara_data)

    def save_picture(self) -> None:
        save_dir = utils.make_save_dir()
        pic_name = os.path.basename(self.file_name)
        pic_name, extension = pic_name.lower().split(".")
        save_file_name = f'{pic_name}_kuwahara.{extension}'
        self.kuwahara_image.save(Path(save_dir, save_file_name))
        msg = f'successfully save kuwahara picture\n{save_dir}/{save_file_name}'
        sg.Popup(msg)

    def start(self) -> None:
        folder = ''
        while True:
            event, values = self.window.Read()
            if event == "photo_folder":
                if values["photo_folder"] != "":
                    if os.path.isdir(values["photo_folder"]):
                        folder = values["photo_folder"]
                        image_files = utils.get_image_files_list(values["photo_folder"])
                        self.window.find_element("files_listbox").Update(values=image_files)
            if event == "files_listbox":
                full_filename = os.path.join(folder, values["files_listbox"][0])
                self.set_file_name(full_filename)
                self.show_image()

            if event == "parameter":
                param = values['parameter']
                if param:
                    self.set_parameter(param)

            if event == 'filter':
                if self.file_name and self.parameter:
                    self.show_kuwahara_image()

            if event == 'save':
                if self.kuwahara_image:
                    self.save_picture()

            if event is None or event == 'Exit':
                return None
