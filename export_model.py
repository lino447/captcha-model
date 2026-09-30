#!/usr/bin/env python3
import ddddocr, os, shutil

pkg_dir = os.path.dirname(ddddocr.__file__)
print(f"ddddocr 目錄: {pkg_dir}")

onnx_files = [f for f in os.listdir(pkg_dir) if f.endswith('.onnx')]
if not onnx_files:
    print("找不到 .onnx 檔案")
else:
    for fname in onnx_files:
        src = os.path.join(pkg_dir, fname)
        size = os.path.getsize(src) / 1024 / 1024
        shutil.copy(src, fname)
        print(f"複製: {fname}  ({size:.1f} MB)")

print("\n把上面的 .onnx 放到你的 GitHub repo")
print("然後把腳本的 @resource 改成你自己的 raw URL")
