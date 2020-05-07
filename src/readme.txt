Projekt přikládám i s intrepreterm (virtual env.) raději
Pro spuštění je potřeba PyOpenGL, Pyglet a Python 3 (3.8)
Okno je nastaveno na 1280x920 lze případně zmenšit ve třídě Controller

Spouštěcí soubor je app.py

Exportovat (freeze) do exe se mi nepodařilo ani po mnoha pokusech (problém s cestami k resources), zkoušel jsem PyInstaller, cxfreeze, py2exe
Nicméně app.py by mělo spustit aplikaci bez nutnosti editoru.

Ovládání pohyb WASD + myš, dále viz. nápověda v app

Zameřil jsme se tedy na reprezentaci bludiště, kolize, textury, skybox, mlhu
Nejproblematičtější byly kolize, použil jsem jednoduchou AABB kolizi, ale vymyslet správnou reakci na ni mi přesto trvalo několik dní, 
dále mapovaní textur na cube_map, hlavně mimo jiné díky jinému počátku souřadnic textury, a využívaní vektorů

Skype
Silvestr Mikeska / live:ondramikeska
ondramikeska@gmail.com
