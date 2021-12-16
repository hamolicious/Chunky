from os import system

system('rmdir dist /s')
system('rmdir build /s')
system('py -m build')
system('py -m twine upload dist/* --verbose')

print('Dont forget to update README PYPI badge')

