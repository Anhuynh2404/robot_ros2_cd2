from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'robotcd_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include all launch files from the launch directory
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
        # Include all world files from the worlds directory
        (os.path.join('share', package_name, 'worlds'), glob(os.path.join('worlds', '*.world'))),
        # Include all model files from the models directory (và các thư mục con nếu có)
        (os.path.join('share', package_name, 'models'), glob(os.path.join('models', '*.*'))),
        # Nếu model có cấu trúc thư mục phức tạp hơn (ví dụ: models/my_robot/model.sdf, models/my_robot/meshes/...)
        # bạn có thể cần các dòng glob phức tạp hơn hoặc liệt kê rõ ràng hơn.
        # Ví dụ đơn giản cho models/your_robot.sdf:
        #(os.path.join('share', package_name, 'models'), glob(os.path.join('models', 'your_robot.sdf'))), # <<< Đổi tên file SDF
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='an',
    maintainer_email=' huynhcongan2442004@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
