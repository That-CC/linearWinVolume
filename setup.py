from setuptools import setup, find_packages
setup(
 name='linearwinvolume',
 version='1.0.0',
 description="A Python implementation of pycaw that doesn't function on a logarithmic scale",
 url='https://github.com/That-CC/linearWinVolume', 
 author='Adrian Ornelas',
 author_email='afornelas@outlook.com',
 classifiers=[
   'Intended Audience :: Education',
   'Operating System :: Windows 10/11',
   'License :: OSI Approved :: MIT License',
   'Programming Language :: Python :: 3',
 ],
 keywords=['python', 'pycaw', 'volume', 'windows volume','windows volume control'],
 packages=find_packages(),
 install_requires = ['pycaw','comtypes', 'enum34;python_version<"3.4"', 'psutil', 'future']
)