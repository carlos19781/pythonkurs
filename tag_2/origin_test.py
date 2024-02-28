"""
https://pypi.org/project/originpro/

Dieses Paket enthält eine High-Level-API für die Interaktion 
mit der Origin-Software über die COM-Schnittstelle des Origin 
Automation Server. Die Funktionalität umfasst (ist aber nicht beschränkt auf) 
das Lesen, Schreiben und Ändern von Daten sowie das Erstellen und 
Exportieren von Diagrammen. Eine Instanz von Origin wird gestartet 
(entweder sichtbar oder versteckt), wenn dieses Paket verwendet wird.

pip install originpro
"""
import originpro

import os
import originpro as op

op.set_show()

x_vals = [1,2,3,4,5,6,7,8,9,10]
y_vals = [23,45,78,133,178,199,234,278,341,400]

wks = op.new_sheet('w')

wks.from_list(0, x_vals, 'X Values')
wks.from_list(1, y_vals, 'Y Values')

gp = op.new_graph()
gl = gp[0]
gl.add_plot(wks, 1, 0)
gl.rescale()

fpath = op.path('u') + 'simple.png'
gp.save_fig(fpath)
print(f'{gl} is exported as {fpath}')

op.exit()