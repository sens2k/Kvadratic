from PySide import QtCore, QtGui
import sys
from redact import Ui_Form
from math import sqrt
#---------------------------------
app = QtGui.QApplication(sys.argv)
Form = QtGui.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()
#---------------------------------
def resh():
	ui.label_x1.clear()
	ui.label_x2.clear()
	#-----------------------------
	try:
		a = float(ui.a_in.text())
	except ValueError:
		a = 1
	try:
		a = float(ui.b_in.text())
	except ValueError:
		b = 1
	a = float(ui.a_in.text())
	b = float(ui.b_in.text())
	c = float(ui.c_in.text())
	d = float(b**2-4*a*c)
	#-----------------------------
	if d < 0 :
		ui.label_resh.setText('Решение :')
		if a == 1:
			ui.uravn_label.setText('x²+'+str(b)+'x'+'+'+str(c)+' = 0')
			if b == 1:
				ui.uravn_label.setText('x²+'+'x'+'+'+str(c)+' = 0')
		else:
			ui.uravn_label.setText(str(a)+'x²+'+str(b)+'x'+'+'+str(c)+' = 0')
			if b == 1:
				ui.uravn_label.setText(str(a)+'x²+'+'x'+'+'+str(c)+' = 0')

		ui.label_disc.setText('Найдем дискриминант квадратного уравнения :')
		ui.label_5.setText('D = b² - 4ac = '+str(int(b**2))+' - '+str(int(4*a*c))+' = '+str(d))
		ui.label_korni.setText('Дискриминант меньше нуля, корней нет')
	if d >= 0 :
		x1 = float((-b+sqrt(d))/(2*a))
		x1 =("%.4f" % x1)
		x2 = float((-b-sqrt(d))/(2*a))
		x2 =("%.4f" % x2)
		d = str(d)
		#-----------------------------
		ui.label_resh.setText('Решение :')
		if a == 1:
			ui.uravn_label.setText('x²+'+str((b))+'x'+'+'+str((c))+' = 0')
		else:
			ui.uravn_label.setText(str(a)+'x²+'+str((b))+'x'+'+'+str((c))+' = 0')
		ui.label_disc.setText('Найдем дискриминант квадратного уравнения :')
		ui.label_5.setText('D = b² - 4ac = '+str(int(b**2))+' - '+str(int(4*a*c))+' = '+str(d))
		ui.label_korni.setText('Дискриминант больше нуля, 2 корня :')
		ui.label_x1.setText('x1 = ' + str(x1))
		ui.label_x2.setText('x2 = ' + str(x2))
ui.butt.clicked.connect(resh)
#---------------------------------
sys.exit(app.exec_())