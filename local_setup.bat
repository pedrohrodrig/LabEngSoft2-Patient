echo off
echo VERIFIQUE EM QUAL PYTHON O PIPENV SERA INSTALADO!
echo.
echo Sera utilizado:
py --version
echo.
echo Se este Python nao for o correto, aperte Cntrl+C para sair
pause
mkdir backend
cd backend
py -m pip install pipenv
pipenv run pre-commit install --python 3.10
pipenv install django
pipenv install djangorestframework
