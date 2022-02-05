from setuptools import setup

package_name = 'ir_sensor_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hle',
    maintainer_email='huyftw@aim.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "ir_dist_publisher = ir_sensor_pkg.ir_dist_publisher:main",
            "ir_dist_listener = ir_sensor_pkg.ir_dist_listener:main",
        ],
    },
)
