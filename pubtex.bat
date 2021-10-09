@echo off
rem Compling papers IEEE or ACM format
rem Usage: build [file name base] [paper size] [switch]
rem paper size: letter or a4
rem switch: IEEE or ACM
rem save this file in root/windoze/commands folder

if "%1" == "" goto error
if "%2" == "" goto error
if "%3" == "" goto error

echo Starting first pass LaTex
	latex %1.tex
echo Done
echo 
echo Starting first pass bibTex
	bibtex %1
echo Done
echo 
echo Starting second pass LaTex
	latex %1.tex
echo Done
echo 
echo Starting third pass LaTex
	latex %1.tex
echo Done
echo 

if "%3" == "ACM" goto ACM
if "%3" == "IEEE" goto IEEE

:ACM
	echo Creating %1.ps from %1.dvi (ACM Style)
		 dvips -P cmz -t %2 -o %1.ps %1.dvi
	echo Done
	goto pdf
:IEEE
	echo Creating %1.ps from %1.dvi (IEEE Style)
		dvips -o %1.ps -G0 -t %2 %1
	echo Done
	goto pdf

:pdf

echo Creating %1.pdf from %1.ps...
	ps2pdf %1.ps %1.pdf
echo Done

goto end

:error
	echo Missing arguments
	echo Usage: build [file name base] [paper size] [switch]
	echo paper size: letter or a4
	echo switch: IEEE or ACM
:end

echo Cleaning up
	del /S *.*~
	del /S *.aux
	del /S *.log
	del /S *.blg
	del /S *.bak
	del /S *.dvi
	del /S *.ps
echo Done
echo All Done
@echo on
