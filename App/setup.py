from cx_Freeze import setup, Executable
setup(name='reverse_shell',
      version='1.0',
      description='',
      executables=[Executable(r'main.pyw',  base="Win32GUI")])
