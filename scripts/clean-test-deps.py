import os
import re
from pathlib import Path

def find_gradle_files(start_path: Path):
    return list(start_path.rglob("build.gradle.kts"))

def clean_test_dependencies(file_path: Path):
    with file_path.open('r', encoding='utf-8') as f:
        lines = f.readlines()

    output_lines = []
    inside_dependencies = False
    brace_count = 0
    removed_lines = []

    for line in lines:
        stripped = line.strip()

        # 进入 dependencies 块
        if not inside_dependencies and stripped.startswith("dependencies"):
            inside_dependencies = True

        if inside_dependencies:
            brace_count += line.count("{") - line.count("}")

            # 判断是否是 testImplementation 或 androidTestImplementation 行（非注释）
            is_test_line = re.match(r'\s*(testImplementation|androidTestImplementation)\s*\(.*\)', stripped)
            if is_test_line:
                removed_lines.append(line.rstrip())
                continue  # 跳过该行

            output_lines.append(line)

            if brace_count == 0:
                inside_dependencies = False
        else:
            output_lines.append(line)

    if removed_lines:
        with file_path.open('w', encoding='utf-8') as f:
            f.writelines(output_lines)

        print(f"🧹 清理文件: {file_path}")
        for rline in removed_lines:
            print(f"   ✂️ 移除: {rline}")
    else:
        print(f"✅ 无需清理: {file_path}")

def main():
    script_path = Path(__file__).resolve()
    project_root = script_path.parent.parent

    print(f"🔍 正在扫描路径: {project_root}")
    gradle_files = find_gradle_files(project_root)

    if not gradle_files:
        print("⚠️ 未找到 build.gradle.kts 文件")
        return

    for file in gradle_files:
        clean_test_dependencies(file)

if __name__ == '__main__':
    main()