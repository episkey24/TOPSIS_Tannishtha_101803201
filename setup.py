from distutils.core import setup

setup(
  name = 'TOPSIS_Tannishtha_101803201', 
  packages = ['TOPSIS_Tannishtha_101803201'], 
  version = '1.0.0',  
  license='MIT', 
  description = 'Topsis score calculator',
  long_description=open("readme.txt").read(),
  author = 'Tannishtha',               
  author_email = 'ttannishtha_be18@thapar.edu', 
  keywords = ['topsis', 'thapar', 'rank', 'topsis score'], 
  install_requires=["pandas"],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers', 
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
