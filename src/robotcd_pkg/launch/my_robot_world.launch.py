import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node as RosNode

def generate_launch_description():

    pkg_name = 'robotcd_pkg' 

    # --- Cấu hình Gazebo ---
    # Lấy đường dẫn đến package gazebo_ros
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')

    # Đường dẫn đến file world của bạn trong package

    world_file_path = os.path.join(get_package_share_directory(pkg_name), 'worlds', 'house.world') 

    # Khai báo đối số cho file world 
    declare_world_cmd = DeclareLaunchArgument(
        'world',
        default_value=world_file_path,
        description='Full path to the world file to load')

    # Include file launch gốc của Gazebo, truyền vào world tùy chỉnh
    start_gazebo_server_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')),
        launch_arguments={'world': LaunchConfiguration('world')}.items(),
    )

    start_gazebo_client_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py'))
    )

    # --- Cấu hình Spawn Robot ---
    # Đường dẫn đến file SDF của robot trong package
    robot_sdf_path = os.path.join(get_package_share_directory(pkg_name), 'models', 'model.sdf') 

    # Node để spawn robot từ file SDF
    spawn_robot_cmd = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-entity', 'my_robot',        # <<< Tên robot trong Gazebo (bạn có thể đổi)
            '-file', robot_sdf_path,
            '-x', '0.0',                 # <<< Vị trí X ban đầu
            '-y', '0.0',                 # <<< Vị trí Y ban đầu
            '-z', '0.5',                 # <<< Vị trí Z ban đầu (đảm bảo robot không bị rơi xuống đất)
            '-Y', '0.0'                  # <<< Hướng Yaw ban đầu (radian)
        ],
        output='screen',
    )
    
    # Đọc nội dung file model.sdf để đưa vào robot_description
    robot_description = ParameterValue(open(robot_sdf_path, 'r').read(), value_type=str)
    
    # Tạo node robot_state_publisher
    robot_state_publisher_node = RosNode(
    	package='robot_state_publisher',
    	executable='robot_state_publisher',
    	name='robot_state_publisher',
    	parameters=[{'robot_description': robot_description}],
    	output='screen'
    )


    # --- Tạo Launch Description ---
    ld = LaunchDescription()

    # Thêm các hành động vào launch description
    ld.add_action(declare_world_cmd)
    ld.add_action(start_gazebo_server_cmd)
    ld.add_action(start_gazebo_client_cmd)
    ld.add_action(spawn_robot_cmd)
    ld.add_action(robot_state_publisher_node)

    return ld
