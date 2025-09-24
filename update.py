import os

def gen_resource_auto_md(source_path, output_file, base_url=""):
    with open(output_file, 'w', encoding='utf-8') as f:
        # f.write('# 资料(自动)\n')
        
        # 遍历文件夹结构
        for root, dirs, files in os.walk(source_path):
            relative_path = os.path.relpath(root, source_path)
            if relative_path == '.':
                continue  # 跳过根目录

            # 生成文件夹标题
            f.write(f'#### {os.path.basename(root)}\n')

            # 生成文件列表
            files.sort()
            for file in files:
                file_path = os.path.join(relative_path, file)
                link = os.path.join(base_url, file_path).replace("\\", "/") if base_url else file_path.replace("\\", "/")
                
                f.write(f'  - [{file}]({link})\n')
            f.write('\n')
    print(f"✅ Successfully generate: {output_file}")


# 生成 resource-auto.md
if __name__ == "__main__":
    source_path = '课程资料'         # 修改为实际路径
    output_file = 'docs/resource-auto.md' # 输出文件路径
    base_url = "https://github.com/haodongcui/xju-math-wiki/raw/main/课程资料"  # 基础URL
    
    gen_resource_auto_md(source_path, output_file, base_url)