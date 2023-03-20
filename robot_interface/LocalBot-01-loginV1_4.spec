# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['LocalBot-01-loginV1_4.py'],
             pathex=['D:\\Arquivos HD\\Projetos HD\\SD Labs\\JOBS\\Ahmd\\rocket\\rocket_kitchens_local_bot'],
             binaries=[],
            datas=[('D:\\Arquivos HD\\Projetos HD\\SD Labs\\JOBS\\Ahmd\\rocket\\rocket_kitchens_local_bot\\robot_interface\\*', 'dependencies'),
                    ('D:\\Arquivos HD\\Projetos HD\\SD Labs\\JOBS\\Ahmd\\rocket\\rocket_kitchens_local_bot\\robot_interface\\model\\robot_models\\*', 'robot_models'),
                    ('D:\\Arquivos HD\\Projetos HD\\SD Labs\\JOBS\\Ahmd\\rocket\\rocket_kitchens_local_bot\\robot_interface\\rocketKitchens.kv', '.'),
                     ('D:\\Arquivos HD\\Projetos HD\\SD Labs\\JOBS\\Ahmd\\rocket\\rocket_kitchens_local_bot\\robot_interface\\logo.jpg', '.')],
             hiddenimports=['kivymd', 'kivymd.icon_definitions', 'playwright', 'psycopg2'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='LocalBot',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='LocalBot')
