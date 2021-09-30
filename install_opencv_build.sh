#!/bin/bash
wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.4.5.zip
unzip -qq opencv.zip

wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.4.5.zip
unzip -qq opencv_contrib.zip

cd opencv-3.4.5

mkdir build
cd build
PATH_BIN= binary

mkdir ${binary}

cmake -DBUILD_SHARED_LIBS=OFF -BUILD_opencv_apps=ON
-DOPENCV_ENABLE_NONFREE:BOOL=ON
-DCMAKE_BUILD_TYPE=Release
-DBUILD_opencv_python2=OFF
-DBUILD_opencv_python3=OFF
-DINSTALL_C_EXAMPLES=OFF
-DBUILD_TESTS=OFF
-DBUILD_PERF_TESTS=OFF ..
-DCMAKE_INSTALL_PREFIX=./../../path_install ..
-DOPENCV_EXTRA_MODULES_PATH=./../../opencv_contrib-3.4.5/modules ..

make -j4

make install

cmake -D CMAKE_CXX_FLAGS=-std=c++11 \
-D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_C_COMPILER=/usr/bin/gcc-9 \
-D CMAKE_INSTALL_PREFIX=./binary \
-D BUILD_SHARED_LIBS=OFF \
-D BUILD_opencv_apps=ON \
-D OPENCV_ENABLE_NONFREE:BOOL=ON \
-D INSTALL_PYTHON_EXAMPLES=OFF \
-D BUILD_opencv_python2=OFF \
-D BUILD_opencv_python3=OFF \
-D INSTALL_C_EXAMPLES=OFF \
-D BUILD_TESTS=OFF \
-D BUILD_opencv_cudacodec=OFF \
-D BUILD_EXAMPLES=OFF \
-D MAKE_BUILD_TYPE=Debug \
-D BUILD_opencv_stereo=OFF \
-D BUILD_opencv_bioinspired=OFF \
-D BUILD_opencv_fuzzy=OFF \
-D BUILD_java=OFF \
-D OPENCV_EXTRA_MODULES_PATH=./../../opencv_contrib-3.4.5/modules ..

