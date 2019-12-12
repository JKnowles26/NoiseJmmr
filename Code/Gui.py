#!/usr/bin/env python3
import gi, os
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GdkPixbuf
from Wav2Png import Wav2Img
from Chunker import BigChunker

builder = Gtk.Builder()
builder.add_from_file("assets/UI.glade")
style_provider = Gtk.CssProvider()
css = open("assets/style.css", "rb")
css_data = css.read()
css.close()
style_provider.load_from_data(css_data)
Gtk.StyleContext.add_provider_for_screen(
    Gdk.Screen.get_default(), style_provider,
    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)

class Window:
    def __init__(self):
        self.window = builder.get_object("window")
        self.window.connect("delete-event", quit)

        wav_filter = Gtk.FileFilter()
        wav_filter.set_name("Wave (*.wav)")
        wav_filter.add_pattern("*.[Ww][Aa][Vv]")
        wav_filter.add_pattern("*.[Ww][Vv]")

        buttons = ("left", "right")
        for i, side in enumerate(buttons):
            label = builder.get_object(side + "_label")
            selector = builder.get_object(side + "_selector")
            selector.add_filter(wav_filter)
            selector.connect("file-set", self.file_selected, selector, label)
            button = builder.get_object(side + "_button")
            button.connect("clicked", self.button_click, button, selector)

        self.waveform_img = builder.get_object("waveform")
        self.spectrogram_img = builder.get_object("spectrogram")

        self.updater()

    def file_selected(self, file_selected, selector, label):
        file = selector.get_filename()
        label.set_text(file)
        selector_name = Gtk.Buildable.get_name(selector)
        if selector_name == 'left_selector':
            Wav2Img(file)
            self.waveform_img.set_from_file("/tmp/waveform.png")
            self.spectrogram_img.set_from_file("/tmp/spectrogram.png")

    def button_click(self, button_click, button, selector):
        file = selector.get_filename()
        print("Analysing", file)
        c = BigChunker(file)

    def updater(self):
        self.window.show_all()
        Gtk.main()

def quit(widget, event):
    Gtk.main_quit()
    os._exit(os.EX_OK)

if __name__ == "__main__":
    win = Window()
