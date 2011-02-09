if __name__ == '__main__':
    setup(
        version="1.0",
        description="Design and check sets of edit metric sequence tags.",
        author="Brant Faircloth",
        author_email="brant.faircloth+edittag@gmail.com ",
        url="http://baddna.github.com/edittag/",
        license="BSD",
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Operating System :: OS Independent',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python',
            'Topic :: Scientific/Engineering :: Bio-Informatics',
             ],
        requires=['NumPy (>=1.3)',],
        long_description=open('README.txt').read(),
        packages=['edittag',
                'edittag.tests',
                'edittag.test-data',
                'edittag.primer3'
                ],
        scripts=['bin/add_tags_to_adapters.py',
                'add_tags_to_primers.py',
                'design_edit_metric_tags.py',
                'estimate_sequencing_error_effects.py',
                'get_tag_flows_for_454.py',
                'validate_edit_metric_tags.py'
                ]
        )