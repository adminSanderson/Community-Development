# community development 

@echo off
echo Добро пожаловать в мою программу на языке cmd!
echo.
echo Текущая дата и время:
echo.
date /t
time /t
echo.
echo Выключить удаленный компьютер? (y/n)
set /p choice=
if "%choice%"=="y" (
    echo.
    echo Запуск команды для выключения удаленного компьютера...
    start /B shutdown /m \\ИМЯ_КОМПЬЮТЕРА /s /f /t 0
) else (
    echo.
    echo Выбрано не выключать компьютер.
)
echo.
echo Спасибо за использование программы!
pause
