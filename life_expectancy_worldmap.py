# 1/10/2020 @huszar.tony

import csv

from pygal.maps.world import World
from pygal.style import RotateStyle, LightColorizedStyle

from country_codes import get_country_code

filename = 'life_expectancy_globaly.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    cc_life_expectancy = {}
    for line in reader:
        country_name = line[0]
        code = get_country_code(country_name)
        try:
            value = int(float(line[4]))
        except ValueError:
            pass
        if code:
            cc_life_expectancy[code] = value

    cc_pop1, cc_pop2, cc_pop3 = {}, {}, {}
    for country, age in cc_life_expectancy.items():
        if age < 35:
            cc_pop1[country] = age
        elif age < 50:
            cc_pop2[country] = age
        else:
            cc_pop3[country] = age

    print(len(cc_pop1), len(cc_pop2), len(cc_pop3))

wm_style = RotateStyle("#336699", base_style=LightColorizedStyle)
wm = World(style=wm_style)
wm.title = "Life expectancy during the 1960s \nWorld Wide"
wm.add("0-35", cc_pop1)
wm.add("0-50", cc_pop2)
wm.add(">50", cc_pop3)

wm.render_to_file('life_expectancy1960.svg')

































































