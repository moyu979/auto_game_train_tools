@echo off
setlocal enabledelayedexpansion

rem 检查是否传入了视频文件作为参数
if "%~1"=="" (
    echo 请提供视频文件路径作为参数！
    echo 例如：bat video.mp4
    pause
    exit /b
)

rem 获取传入的视频文件路径
set "input_video=%~1"

rem 设置输出目录
set "output_dir=.\data"

rem 检查视频文件是否存在
if not exist "%input_video%" (
    echo 视频文件不存在：%input_video%
    pause
    exit /b
)

rem 创建输出目录（如果不存在）
if not exist "%output_dir%" (
    mkdir "%output_dir%"
)

rem 使用 ffmpeg 提取每秒一帧，文件名递增
ffmpeg -i "%input_video%" -vf "fps=1" "%output_dir%\frame_%%04d.png"

echo 提取完成！
pause
