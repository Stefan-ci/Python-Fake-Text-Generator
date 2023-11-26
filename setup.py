from setuptools import setup

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.md") as history_file:
    history = history_file.read()

requirements = []

test_requirements = []

setup(
    author="Stéphane Claver DIBY",
    author_email="kiuv.abraj@gmail.com",
    description="Generate random text that looks like Latin/English (like the given language).",
    include_package_data=True,
    install_requires=requirements,
    keywords="Random text placeholder",
    license="MIT",
    long_description=readme + "\n\n\n" + history,
    name="fake-text",
    package_dir={"fake_text": "fake_text"},
    packages=["fake_text"],
    python_requires=">=3.3",
    test_suite="tests",
    tests_require=test_requirements,
    version="1.0",
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: Linguistic",
    ]
)
