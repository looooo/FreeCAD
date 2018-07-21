#!/usr/bin/env bash

FEEDSTOCK_ROOT=$(cd "$(dirname "$0")"; pwd;)
SOURCE_DIR=${FEEDSTOCK_ROOT}/../..
echo ${SOURCE_DIR}

docker info

config=$(cat <<CONDARC

channels:
 - conda-forge
 - defaults

show_channel_urls: true

CONDARC
)

HOST_USER_ID=$(id -u)


if hash docker-machine 2> /dev/null && docker-machine active > /dev/null; then
    HOST_USER_ID=$(docker-machine ssh $(docker-machine active) id -u)
fi

rm -f "$FEEDSTOCK_ROOT/build_artefacts/conda-forge-build-done"

cat << EOF | docker run -i \
                        -v "${SOURCE_DIR}":/source \
                        -e HOST_USER_ID="${HOST_USER_ID}" \
                        -a stdin -a stdout -a stderr \
                        condaforge/linux-anvil \
                        bash || exit 1

set -x
export PYTHONUNBUFFERED=1

echo "$config" > ~/.condarc

conda clean --lock

conda install --yes --quiet conda-build conda-forge-pinning wget

# installing some libraries which are not shipped by conda:
/usr/bin/sudo -n yum install -y libXt-devel libXmu-devel libXi-devel mesa-libGLU-devel

# build the conda-package
conda build /source/package/conda -m /opt/conda/conda_build_config.yaml --python=3.6


# build an appimage from the conda-packages

#1 create a new environment in the AppDir
conda create -p AppDir/usr freecad-daily blas=*=openblas --use-local --copy -y

## this will create a huge env. We have to find some ways to make the env smaller
## deleting some packages explicitly?

#2 delete unnecessary stuff
rm -rf AppDir/usr/include
find AppDir/usr -name \*.a -delete
mv AppDir/usr/bin AppDir/usr/bin_tmp
mkdir AppDir/usr/bin
cp AppDir/usr/bin_tmp/FreeCAD AppDir/usr/bin/FreeCAD
cp AppDir/usr/bin_tmp/python AppDir/usr/bin/
rm -rf AppDir/usr/bin_tmp
#+ deleting some specific libraries not needed. eg.: stdc++

#3 create the appimage
wget https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage
chmod +x appimagetool-x86_64.AppImage
./appimagetool-x86_64.AppImage --appimage-extract

ARCH=x86_64 squashfs-root/AppRun  AppDir

#4 setting rights for the appimage
chmod +x FreeCAD-x86_64.AppImage

#5 delete the created environment
rm -rf AppDir/usr
rm -rf squashfs-root/
rm -rf appimagetool-x86_64.AppImage

echo "############## APPIMAGE-FILE-SIZE ################"
stat --printf="%s" FreeCAD-x86_64.AppImage

EOF