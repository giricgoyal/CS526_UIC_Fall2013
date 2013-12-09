@echo off
echo "Setting environment variables"

if "%SQL_PATH%" == "" set SQL_PATH=..\data_processing
if "%1" == "" goto error

:runMain
cd %SQL_PATH%
cd
sqlite3.exe %1
goto end

:error
echo "No db file specified"
exit

:end
PAUSE