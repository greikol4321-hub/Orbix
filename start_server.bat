@echo off
echo Iniciando servidor Orbix...
echo.
echo Servidor disponible en:
echo - Presentacion: http://localhost:5000/
echo - Ae.N.K.I.: http://localhost:5000/aenki
echo - Sentinel Dashboard: http://localhost:5000/sentinel
echo - Portafolio: http://localhost:5000/portafolio
echo - Blog: http://localhost:5000/blog
echo - Contacto + Chat: http://localhost:5000/contacto-chat
echo.
"D:/Proyectos Orbix/.venv/Scripts/python.exe" backend.py
pause
