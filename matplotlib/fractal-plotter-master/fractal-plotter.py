#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright © 2016 Anton Karmanov <bergentroll@openmailbox.org>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from tkinter import Tk, Canvas, IntVar, BooleanVar, Scale, Menu
from tkinter.ttk import Button, Frame, Combobox, Entry,\
    Checkbutton, LabelFrame, Label, Style
from tkinter.messagebox import askokcancel, showwarning, showinfo
from tkinter.simpledialog import askstring
from tkinter.filedialog import asksaveasfilename
from tkinter.colorchooser import askcolor
from math import sin, cos, radians
from array import array
from colorsys import hsv_to_rgb
from gettext import gettext, bindtextdomain, textdomain
import json
import os

PRESETS = 'presets.json'

textdomain('fractal-plotter')
bindtextdomain('fractal-plotter', './lang')

bg_color = '#000000'
fg_color = '#ffffff'
global_scale_factor = 0.9
direction = 0
padding = 5
debug = False


def koch_curve(n, first_step):
    '''
    Generator of sequence of angles of turn.
    '''
    if n <= 1:
        yield from first_step
    else:
        yield from koch_curve(n - 1, first_step)
        for i in first_step:
            yield(i)
            yield from koch_curve(n - 1, first_step)


def fit_to_canvas(min_x, min_y, max_x, max_y, line_len):
    '''
    Calculate size for curve that will be plotted.
    Uses theoretical values from calc_curve.
    '''
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    curve_width = max_x - min_x
    curve_height = max_y - min_y
    kx = canvas_width / curve_width
    ky = canvas_height / curve_height
    scale_factor = min(kx, ky) * global_scale_factor
    line_len *= scale_factor
    start_x = 0.5 * canvas_width - (min_x + 0.5 * curve_width) * scale_factor
    start_y = 0.5 * canvas_height - (min_y + 0.5 * curve_height) * scale_factor
    if debug:
        canvas.create_rectangle(
            scale_factor * min_x + start_x,
            scale_factor * min_y + start_y,
            scale_factor * (min_x + curve_width) + start_x,
            scale_factor * (min_y + curve_height) + start_y,
            outline='red'
        )
    return(start_x, start_y, line_len)


def calc_curve(start_x, start_y, line_len):
    '''
    Calculate future curve to know it size and position.
    '''
    end_x = start_x + line_len
    end_y = start_y
    min_x = start_x
    min_y = start_y
    max_x = min_x
    max_y = min_y
    direction = 0
    for angle in sequence:
        min_x = min(min_x, end_x)
        min_y = min(min_y, end_y)
        max_x = max(max_x, end_x)
        max_y = max(max_y, end_y)
        direction -= angle
        start_x, start_y = end_x, end_y
        end_x = cos(radians(direction)) * line_len + start_x
        end_y = sin(radians(direction)) * line_len + start_y
    return(min_x, min_y, max_x, max_y, line_len)


def rainbow(n):
    '''
    Return sequence of colors for each next line in curve.
    '''
    hue = n / (len(sequence))
    rgb_color = hsv_to_rgb(hue, 1.0, 255)
    hex_color = '#{:02x}{:02x}{:02x}'.format(*(int(i) for i in rgb_color))
    return(hex_color)


def draw_line(start_x, start_y, end_x, end_y, color):
    '''
    Add lines to canvas.
    '''
    canvas.create_line(
                start_x, start_y, end_x, end_y,
                width=line_width.get(), fill=color, tag='line'
            )
    if debug:
        print(
            'start x, y: {:.2f}, {:.2f}'.format(start_x, start_y) +
            '\tend x, y: {:10.4f}, {:10.4f}'.format(end_x, end_y) +
            '\tcolor: {}'.format(color)
        )


def plot(start_x, start_y, line_len):
    '''
    Draw background rectangle that needs for exporting images.
    Execute the sequence of angles.
    '''
    canvas.create_rectangle(
        0, 0, canvas.winfo_width(), canvas.winfo_height(),
        fill=bg_color, outline=bg_color
    )
    end_x = start_x + line_len
    end_y = start_y
    direction = 0
    item_num = 0
    for angle in sequence:
        if color_flag.get():
            draw_line(start_x, start_y, end_x, end_y, rainbow(item_num))
            item_num += 1
        else:
            draw_line(start_x, start_y, end_x, end_y, fg_color)
        direction -= angle
        start_x, start_y = end_x, end_y
        end_x = cos(radians(direction)) * line_len + start_x
        end_y = sin(radians(direction)) * line_len + start_y


def parse_angles():
    '''
    Try to parse users sequence.
    '''
    try:
        angles = [int(i) for i in angles_input.get().split()]
    except ValueError:
        angles = [int(i) for i in angles_input.get().split(', ')]
    return(angles)


def load_presets():
    '''
    Loads JSON file with presets.
    '''
    global presets
    if not os.path.isfile(PRESETS):
        open(PRESETS, 'a').close()
    if os.stat(PRESETS).st_size > 0:
        with open(PRESETS, 'r') as presets_file:
            try:
                presets = json.load(presets_file)
            except json.decoder.JSONDecodeError:
                presets = {}
                print(gettext('Invalid presets file.'))
                presets_frame.state(['disabled'])
                presets_list.state(['disabled'])
                add_preset_button.state(['disabled'])
                del_preset_button.state(['disabled'])
    else:
        presets = dict()
    presets_list['values'] = sorted(tuple(presets.keys()))


def apply_preset(event):
    '''
    Apply data from presets file to variables.
    '''
    global bg_color, fg_color
    angles_input.delete(0, 'end')
    current_preset = presets_list.get()
    deep_scale.set(presets[current_preset]['deep'])
    angles_input.insert(0, presets[current_preset]['angles'])
    line_width_scale.set(presets[current_preset]['width'])
    bg_color = presets[current_preset]['background']
    fg_color = presets[current_preset]['foreground']
    update_color_buttons()
    if presets[current_preset]['rainbow']:
        color_flag.set('1')
    else:
        color_flag.set('0')


def add_preset():
    '''
    Write new preset to JSON file.
    '''
    current_preset = askstring(
        gettext('Preset name'),
        gettext('Name new preset:')
    )
    print(current_preset)
    if current_preset and current_preset not in presets.keys():
        preset_properties = {
            'deep': deep_scale.get(),
            'angles': angles_input.get(),
            'width': line_width_scale.get(),
            'background': bg_color,
            'foreground': fg_color,
            'rainbow': bool(color_flag.get())
        }
        presets[current_preset] = preset_properties
        with open(PRESETS, 'w') as presets_file:
            json.dump(presets, presets_file, indent=2, sort_keys=True)
        load_presets()
    elif current_preset is not None:
        showwarning(
            gettext('Invalid preset name.'),
            gettext(
                'Preset name can not be empty or equal to existed preset name.'
            )
        )


def del_preset():
    '''
    Remove preset from JSON file.
    '''
    current_preset = presets_list.get()
    if current_preset in presets.keys()\
       and askokcancel(
           gettext('Delete preset'),
           gettext('Do you really want to delete {}?'.format(current_preset))
       ):
        presets.pop(current_preset)
        with open(PRESETS, 'w') as presets_file:
            json.dump(presets, presets_file, indent=2, sort_keys=True)
        load_presets()


def export_image():
    '''
    Function asks name for image and try to export canvas to file.
    '''
    file = asksaveasfilename(
        parent=root,
        filetypes=(
            (gettext('Image'), '*.png'), (gettext('Postscript file'), '*.ps')
        ),
        title=gettext('Export image as..')
    )
    file_no_ext = file[0:file.rfind('.')]
    canvas.postscript(file=file_no_ext + '_raw.ps', colormode='color')
    # Try to crop ps with gs package.
    gs_fail = os.system(
        'ps2ps -dEPSCrop {}_raw.ps {}.ps'.format(file_no_ext, file_no_ext)
    )
    if gs_fail:
        print(
            gettext('You need ghostscript to crop ps and convert it to png.')
        )
    else:
        os.remove(file_no_ext + '_raw.ps')
    # If we choose png and gs is exist we convert ps to png.
    if file.endswith('png') and not gs_fail:
        os.system(
            'gs -dSAFER -dBATCH -dNOPAUSE -sDEVICE=png16m -r150' +
            ' -dGraphicsAlphaBits=4 -sOutputFile={}.png {}.ps'.format(
                file_no_ext, file_no_ext
            )
        )


def update_color_buttons():
    style.configure('FG.TButton', background=fg_color)
    style.configure('BG.TButton', background=bg_color)


def get_fg_color(event=False):
    global fg_color
    fg_color = askcolor(
        parent=root, color=fg_color,
        title=gettext('Foreground color')
    )[1]
    update_color_buttons()


def get_bg_color(event=False):
    global bg_color
    bg_color = askcolor(
        parent=root, color=bg_color,
        title=gettext('Background color')
    )[1]
    update_color_buttons()


def about():
    showinfo(
        gettext('About'),
        gettext(
            '''This script programm made just for fun
by Anton Karmanov (bergentroll@openmailbox.org).'''
        )
    )


def main():
    '''
    Mostly calls other functions.
    '''
    global sequence
    start_x, start_y = 0, 0
    line_len = 50
    canvas.delete('all')
    angles = parse_angles()
    sequence = array('h', koch_curve(deep_scale.get(), angles))
    sequence.append(0)
    start_x, start_y, line_len = \
        fit_to_canvas(*calc_curve(start_x, start_y, line_len))
    plot(start_x, start_y, line_len)

root = Tk()
root.title('Fractal plotter')

style = Style()

menu = Menu(root, tearoff='false', relief='flat')
root.config(menu=menu)

menu_file = Menu(menu, tearoff='false')
menu.add_cascade(label=gettext('File'), menu=menu_file)
menu_file.add_command(
    label=gettext('Export image...'), command=export_image
)
menu_file.add_command(
    label=gettext('Quit'), command=lambda: root.destroy()
)

menu.add_command(label=gettext('About'), command=about)

canvas = Canvas(
    root, bd=2, bg=bg_color, relief='ridge'
)
frame = Frame(root, width=120)

presets_frame = LabelFrame(frame, relief='ridge', text=gettext('Presets'))
presets_list = Combobox(
    presets_frame, state='readonly'
)
add_preset_button = Button(
    presets_frame, text=gettext('Add preset'),
    style='Switch.TButton',
    command=add_preset
)
del_preset_button = Button(
    presets_frame, text=gettext('Delete preset'),
    command=del_preset
)
presets_list.bind('<<ComboboxSelected>>', apply_preset)
angles_input_frame = LabelFrame(
    frame, relief='ridge', text=gettext('Initial sequence')
)
angles_input = Entry(angles_input_frame, text='60, -120, 60')
angles_input.delete(0, 'end')
angles_input.insert(0, '60 -120 60')
deep = IntVar()
deep_scale_frame = LabelFrame(
    frame, relief='ridge', text=gettext('Recursion deep')
)
deep_scale = Scale(
    deep_scale_frame, orient='horizontal', from_=1, to=8, variable=deep
)
deep_scale.set(3)

colors_frame = LabelFrame(frame, relief='ridge', text=gettext('Colors'))
bg_button_frame = Frame(colors_frame, relief='flat')
bg_button = Frame(
    bg_button_frame, style='BG.TButton',
    width=15, height=15,
)
bg_button.bind('<Button-1>', get_bg_color)
bg_button_label = Label(
    bg_button_frame, text=gettext('Background'), compound='left',
)
fg_button_frame = Frame(colors_frame, relief='flat')
fg_button = Frame(
    fg_button_frame, style='FG.TButton',
    width=15, height=15,
)
fg_button.bind('<Button-1>', get_fg_color)
fg_button_label = Label(
    fg_button_frame, text=gettext('Foreground'), compound='left',
)
update_color_buttons()

color_flag = BooleanVar(frame)
rainbow_checkbox = Checkbutton(
    colors_frame, text=gettext('Rainbow mode'), variable=color_flag
    )

line_width = IntVar()
line_width_scale_frame = LabelFrame(
    frame, relief='ridge', text=gettext('Line width')
    )
line_width_scale = Scale(
    line_width_scale_frame, orient='horizontal', from_=1, to=8,
    variable=line_width
)
line_width_scale.set(3)
plot_button = Button(
    frame, text=gettext('Plot'),
    command=main
)

load_presets()

canvas.pack(side='left', fill='both', expand=True)

frame.pack(fill='both', expand=True)
presets_frame.pack(fill='both', padx=padding, pady=padding)
angles_input_frame.pack(fill='both', padx=padding, pady=padding)

angles_input.pack(fill='both', padx=padding, pady=padding)
deep_scale_frame.pack(fill='both', padx=padding, pady=padding)
deep_scale.pack(fill='both', padx=padding, pady=padding)
presets_list.pack(fill='both', padx=padding, pady=padding)
add_preset_button.pack(side='left', fill='both', padx=padding, pady=padding)
del_preset_button.pack(fill='both', padx=padding, pady=padding)
colors_frame.pack(fill='both', padx=padding, pady=padding)
bg_button_frame.pack(fill='both')
bg_button.pack(side='left', padx=padding, pady=padding)
bg_button_label.pack(side='left', fill='both', padx=padding, pady=padding)
fg_button_frame.pack(fill='both')
fg_button.pack(side='left', padx=padding, pady=padding)
fg_button_label.pack(fill='both', padx=padding, pady=padding)
rainbow_checkbox.pack(anchor='w', padx=padding, pady=padding)
line_width_scale_frame.pack(fill='both', padx=padding, pady=padding)
line_width_scale.pack(fill='both', padx=padding, pady=padding)
plot_button.pack(padx=padding, pady=padding)

root.mainloop()
