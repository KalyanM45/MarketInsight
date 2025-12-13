@echo off
echo Starting Market Insight...
echo.
echo [1/2] Starting Backend Server (Python FastAPI)...
start "Backend Server" cmd /k "python main.py"
timeout /t 3 /nobreak >nul
echo.
echo [2/2] Starting Frontend Server (Vite React)...
start "Frontend Server" cmd /k "cd frontend && npm run dev"
echo.
echo ========================================
echo Market Insight is starting!
echo ========================================
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:3000
echo ========================================
