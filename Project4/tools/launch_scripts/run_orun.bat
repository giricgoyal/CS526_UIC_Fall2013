@echo off
echo "Setting environment variables"
if "%OMEGALIB_PATH%" == "" set OMEGALIB_PATH=omegalib-windows-master
@if "%OMEGALIB_PATH%" == "" set OMEGALIB_PATH=D:\GitHub\CS526_UIC_Fall2013\omegalib-windows-master\bin
if "%EXAMPLE_PATH%" == "" set EXAMPLE_PATH=examples
@if "%EXAMPLE_PATH%" == "" set EXAMPLE_PATH=D:\github\CS526_UIC_Fall2013\examples
if "%PROJECT_PATH%" == "" set PROJECT_PATH=Project2
@if "%PROJECT_PATH%" == "" set PROJECT_PATH=D:\github\CS526_UIC_Fall2013\Project2

if "%1" == "" goto runExample 

:runMain
echo "Running : " + %1
cd ..\..\..\%OMEGALIB_PATH%
bin\orun.exe -s ..\%PROJECT_PATH%\%1
goto end

:runExample
echo "No file specified, running example.py"
cd ..\..\..\%OMEGALIB_PATH%
bin\orun.exe -s ..\%EXAMPLE_PATH%\example.py

:end
PAUSE