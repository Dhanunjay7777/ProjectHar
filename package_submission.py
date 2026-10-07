import zipfile
import os

def package():
    zip_filename = 'capstone-submission.zip'
    if os.path.exists(zip_filename):
        os.remove(zip_filename)
        
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add evidence folder
        for root, dirs, files in os.walk('evidence'):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, '.')
                zipf.write(full_path, rel_path)
                
        # Add reflection brief
        zipf.write('reflection-brief-template.md', 'reflection-brief-template.md')
        
        # Add Project folder
        for root, dirs, files in os.walk('Project-Harness Engineering with Claude and Claude Code'):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, '.')
                zipf.write(full_path, rel_path)

    print(f"Created {zip_filename} successfully! Size: {os.path.getsize(zip_filename):,} bytes")

if __name__ == '__main__':
    package()
