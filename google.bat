@echo off
setlocal

:: Set up temp file path
set FILENAME=%TEMP%\googles_resources.html

:: Write disguised HTML loader
(
echo ^<html lang="en"^>
echo ^<head^>
echo ^<title^>Googles Classroom^</title^>
echo ^<link rel="icon" href="https://www.google.com/favicon.ico"^>
echo ^<style^>html, body {margin:0;padding:0;height:100%%;} iframe {border:0;width:100%%;height:100%%;}^</style^>
echo ^</head^>
echo ^<body^>
echo ^<iframe src="https://unblocked-games.s3.amazonaws.com/index.html" allowfullscreen^>^</iframe^>
echo ^</body^>
echo ^</html^>
) > "%FILENAME%"

:: Launch the spoofed page
start "" "%FILENAME%"

echo [✓] Launching Googles Classroom Portal...
exit
