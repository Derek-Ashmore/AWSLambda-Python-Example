#!/bin/bash

if [ $# -eq 0 ]
  then
    echo "Usage: /packIt.sh [build directory]"
    exit 1
fi

BUILD_DIR="$1"
if [ -d $BUILD_DIR ] 
then
    echo "cleaning out previous build"
    rm -Rf $BUILD_DIR/*
else
    echo "creating build directory $BUILD_DIR"
    mkdir $BUILD_DIR
fi

echo "copying sendpulse"
cp -r pysendpulse $BUILD_DIR
echo "copying python code"
cp *.py $BUILD_DIR
echo "unpacking dependent packages"
mkdir $BUILD_DIR/lib
unzip lambda-binary-dependencies.zip -d $BUILD_DIR/lib
echo "Zipping deployment"
zip -r $BUILD_DIR/AWSLambda-Email.zip $BUILD_DIR/*
