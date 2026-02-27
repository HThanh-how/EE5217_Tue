@echo off
color 0A
echo =======================================================
echo KHOI DONG SERVER CHO TRINH CHIEU SLIDE
echo (Giai phap de trinh duyet khong chan CORS khi load file local)
echo =======================================================
echo.

REM Kiem tra xem may co cai san Python khong
python --version >nul 2>&1
if %errorlevel% == 0 (
    echo [INFO] Phat hien Python. Dang khoi tao HTTP Server cong 8000...
    start http://localhost:8000
    python -m http.server 8000
    goto :eof
)

REM Neu khong co python xai thu npx cua NodeJS
npx --version >nul 2>&1
if %errorlevel% == 0 (
    echo [INFO] Phat hien NodeJS. Dang khoi tao HTTP Server cong 8000...
    start http://localhost:8000
    npx serve -l 8000
    goto :eof
)

REM Neu khong co ca 2
echo [CẢNH BÁO] May ban khong cai san Python hoac NodeJS. 
echo Bat buoc ban phai dung Chrome hoac Edge de mo thang file index.html tuy nhien co the bi loi trang trang vi CORS.
pause
