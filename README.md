# ai-py-exe

一个使用 Python 编写的命令行工具：显示当前本地时间，并支持打包为 Windows `exe`，以及通过 GitHub Actions 自动发布 Release。

## 功能

- 显示当前本地时间（含时区）
- 可用 PyInstaller 打包为独立可执行文件（`exe`）
- 推送 `v*` 标签后自动创建 GitHub Release 并上传构建产物

## 本地运行

```bash
python3 time_tool.py
```

示例输出：

```text
2026-03-24 12:34:56 CST
```

## 本地打包 exe（在 Windows 上）

```bash
python -m pip install -r requirements-build.txt
pyinstaller --onefile --name time-tool time_tool.py
```

输出文件在：

```text
dist/time-tool.exe
```

## GitHub Release 自动发布

仓库已包含工作流：`.github/workflows/release.yml`

触发方式：推送版本标签（例如 `v1.0.0`）

```bash
git tag v1.0.0
git push origin v1.0.0
```

工作流会在 `windows-latest`、`ubuntu-latest`、`macos-latest` 上分别构建，并将产物上传到同一个 Release：

- Windows: `time-tool-windows.exe`
- Linux: `time-tool-Linux-x64`
- macOS: `time-tool-macOS-x64`
