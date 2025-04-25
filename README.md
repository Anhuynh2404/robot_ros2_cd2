# **Yêu cầu**
Ros2 Humble

# **Các bước để run:**

## **Tải Project**
1.  Tạo thư mục workspace
    ```bash
    mkdir -p ~/ros2_ws/src
    ```
2.  Clone repo
    ```bash
    cd ~/ros2_ws
    git clone 
    ```
## **Build Workspace**

Bây giờ build workspace để ROS 2 nhận diện package mới và cài đặt các file (launch, world, sdf) vào đúng vị trí.

1.  Quay lại thư mục gốc của workspace:
    ```bash
    cd ~/ros2_ws
    ```
2.  Build workspace bằng `colcon`:
    ```bash
    colcon build --symlink-install
    ```
    *(Lệnh build có thể mất một lúc. `--symlink-install` giúp chỉnh sửa file Python/launch mà không cần build lại mỗi lần, nhưng đối với file world/sdf/XML thì vẫn cần build lại nếu thay đổi).*
3.  Nếu có lỗi, hãy đọc kỹ thông báo lỗi để sửa trong package (thường là lỗi cú pháp trong `package.xml`, `setup.py` hoặc launch file). Chạy lại `colcon build` sau khi sửa.

## **Source Workspace Mới**

Sau khi build thành công cần source workspace này **thay vì** source `/opt/ros/humble/setup.bash` trực tiếp, vì nó sẽ bao gồm cả môi trường ROS 2 gốc và package mới.

1.  Mở một **terminal mới** (hoặc trong terminal hiện tại nếu bạn muốn).
2.  Source file setup của workspace:
    ```bash
    source ~/ros2_ws/install/setup.bash
    ```
    *Lưu ý:* Mỗi khi mở terminal mới để chạy launch file này cần source file `setup.bash` của workspace (`~/ros2_ws/install/setup.bash`). Bạn cũng có thể thêm dòng này vào `~/.bashrc` để tự động source.

## **Chạy Launch File**

Bây giờ  đã sẵn sàng để khởi động mô phỏng!

1.  Trong terminal đã source workspace (ở Bước 6), chạy lệnh launch:
    ```bash
    ros2 launch robotcd_pkg my_robot_world.launch.py
    ```

## **Kiểm tra Kết quả**

* Gazebo (cả server và client) sẽ khởi động.
* Cửa sổ Gazebo sẽ hiển thị bản đồ từ file `house.world` của bạn.
* Sau một vài giây, robot từ file `model.sdf` sẽ xuất hiện trong Gazebo tại vị trí (`-x`, `-y`, `-z`, `-Y`) bạn đã chỉ định trong launch file.
* **Kiểm tra ROS 2 Topics:** Mở một terminal **khác**, source workspace (`source ~/ros2_ws/install/setup.bash`) và chạy `ros2 topic list`. Bạn sẽ thấy các topic cơ bản (`/clock`, `/parameter_events`, `/rosout`) và quan trọng là các topic do **plugin ROS trong file SDF của robot** tạo ra (ví dụ: `/odom`, `/scan`, `/cmd_vel`, `/camera/image_raw`, `/tf`, `/tf_static`...). Sự xuất hiện của các topic này xác nhận tích hợp ROS 2 đang hoạt động.
* **🚨 Lỗi**: Hiện đang bị lỗi robot bị quay tròn khi đưa vào world
  [Xem video](https://drive.google.com/file/d/18rGJSNRQNLvDDohoOOW-p8AeP6IT8ddi/view?usp=drive_link)
## **Bắt đầu Tự động hóa với ROS 2**

