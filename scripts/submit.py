import os, zipfile, sys

def main():
    zipname = './submission/' + sys.argv[1] + '.zip'
    files = os.listdir()
    
    with zipfile.ZipFile(zipname, mode='w') as zip:
        for folder_name, _, filenames in os.walk(os.getcwd()):
            if 'submission' in folder_name or '.git' in folder_name:
                continue
            
            for filename in filenames:
                if '.zip' in filename:
                    continue
                
                file_path = os.path.join(folder_name, filename)
                zip.write(file_path, arcname=os.path.relpath(file_path, '.'))

main()
