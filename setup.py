# setup.py:path/to/setup.py

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='agentxai',
    version='0.1.5',
    author='wickthumb',
    author_email='steven@wick3d.llc',
    description='An agent that uses XAI to achieve goals by executing tools',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/wickthumb/agentX',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
    install_requires=[
        'annotated-types==0.7.0',
        'anyio==4.6.2.post1',
        'build==1.2.2.post1',
        'certifi==2024.8.30',
        'charset-normalizer==3.4.0',
        'distro==1.9.0',
        'docutils==0.21.2',
        'h11==0.14.0',
        'httpcore==1.0.7',
        'httpx==0.27.2',
        'idna==3.10',
        'importlib_metadata==8.5.0',
        'jaraco.classes==3.4.0',
        'jaraco.context==6.0.1',
        'jaraco.functools==4.1.0',
        'jiter==0.7.1',
        'keyring==25.5.0',
        'markdown-it-py==3.0.0',
        'mdurl==0.1.2',
        'more-itertools==10.5.0',
        'nh3==0.2.18',
        'openai==1.55.0',
        'packaging==24.2',
        'pkginfo==1.10.0',
        'pydantic==2.10.1',
        'pydantic_core==2.27.1',
        'Pygments==2.18.0',
        'pyproject_hooks==1.2.0',
        'python-dotenv==1.0.1',
        'readme_renderer==44.0',
        'requests==2.32.3',
        'requests-toolbelt==1.0.0',
        'rfc3986==2.0.0',
        'rich==13.9.4',
        'setuptools==75.6.0',
        'sniffio==1.3.1',
        'tenacity==9.0.0',
        'tqdm==4.67.0',
        'twine==5.1.1',
        'typing_extensions==4.12.2',
        'urllib3==2.2.3',
        'zipp==3.21.0',
    ],
)