script_dir=$(cd $(dirname $0); pwd)

rm -rf Python-2.7.1
rm -rf Python-2.7.1_build

#wget http://www.python.org/ftp/python/2.7.1/Python-2.7.1.tar.bz2 -O Python-2.7.1.tar.bz2
#wget http://www.cnx-software.com/patch/python-2.7.1-cross-compile.patch -O ./python-2.7.1-cross-compile.patch

mkdir Python-2.7.1_build
tar xjvf Python-2.7.1.tar.bz2

cd Python-2.7.1
patch -p1 < ../python-2.7.1-cross-compile_taisyo.patch

./configure
make python Parser/pgen
mv python hostpython
mv Parser/pgen Parser/hostpgen
make distclean

CC=arm-openwrt-linux-muslgnueabi-gcc CXX=arm-openwrt-linux-muslgnueabi-g++ AR=arm-openwrt-linux-muslgnueabi-ar RANLIB=arm-openwrt-linux-muslgnueabi-ranlib ./configure -host=arm-none-linux -prefix=/python
make HOSTPYTHON=./hostpython HOSTPGEN=./Parser/hostpgen BLDSHARED="arm-openwrt-linux-muslgnueabi-gcc -shared" CROSS_COMPILE=arm-openwrt-linux-muslgnueabi- CROSS_COMPILE_TARGET=yes
make install HOSTPYTHON=./hostpython BLDSHARED="arm-openwrt-linux-muslgnueabi-gcc -shared" CROSS_COMPILE=arm-openwrt-linux-muslgnueabi- CROSS_COMPILE_TARGET=yes prefix=$script_dir/python2.7.1_build
