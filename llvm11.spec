#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xA2C794A986419D8A (tstellar@redhat.com)
#
%define keepstatic 1
Name     : llvm11
Version  : 11.1.0
Release  : 132
URL      : https://github.com/llvm/llvm-project/releases/download/llvmorg-11.1.0/llvm-11.1.0.src.tar.xz
Source0  : https://github.com/llvm/llvm-project/releases/download/llvmorg-11.1.0/llvm-11.1.0.src.tar.xz
Source1  : https://github.com/KhronosGroup/SPIRV-LLVM-Translator/archive/bf7d21f9f4220643335d13117f3d601692093a96/SPIRV-11.1.0.tar.gz
Source2  : https://github.com/llvm/llvm-project/releases/download/llvmorg-11.1.0/clang-11.1.0.src.tar.xz
Source3  : https://github.com/llvm/llvm-project/releases/download/llvmorg-11.1.0/clang-tools-extra-11.1.0.src.tar.xz
Source4  : https://github.com/llvm/llvm-project/releases/download/llvmorg-11.1.0/compiler-rt-11.1.0.src.tar.xz
Source5  : https://github.com/llvm/llvm-project/releases/download/llvmorg-11.1.0/lld-11.1.0.src.tar.xz
Source6  : https://github.com/llvm/llvm-project/releases/download/llvmorg-11.1.0/openmp-11.1.0.src.tar.xz
Source7  : https://github.com/llvm/llvm-project/releases/download/llvmorg-11.1.0/llvm-11.1.0.src.tar.xz.sig
Summary  : Google microbenchmark framework
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT MPL-2.0 NCSA
Requires: llvm11-bin = %{version}-%{release}
Requires: llvm11-lib = %{version}-%{release}
Requires: llvm11-license = %{version}-%{release}
BuildRequires : Z3-dev
BuildRequires : Z3-dev32
BuildRequires : binutils-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : doxygen
BuildRequires : elfutils-dev
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : googletest-dev
BuildRequires : libffi-dev
BuildRequires : libffi-dev32
BuildRequires : libstdc++-dev
BuildRequires : libxml2-dev
BuildRequires : libxml2-dev32
BuildRequires : llvm
BuildRequires : llvm-dev
BuildRequires : ncurses-dev
BuildRequires : protobuf-dev
BuildRequires : pypi(sphinx)
BuildRequires : python3-dev
BuildRequires : valgrind-dev
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
Patch1: llvm-0001-CMake-Split-static-library-exports-into-their-own-ex.patch
Patch2: llvm-0002-Improve-physical-core-count-detection.patch
Patch3: llvm-0003-Produce-a-normally-versioned-libLLVM.patch
Patch4: llvm-0004-Allow-one-more-FMA-fusion.patch
Patch5: llvm-0005-Build-tablegen-component-as-a-shared-library.patch
Patch6: llvm-0006-add-missing-limits-inclusion.patch
Patch7: clang-0001-Build-a-single-shared-libclang.patch
Patch8: clang-0002-Detect-Clear-Linux-and-apply-Clear-s-default-linker-.patch
Patch9: clang-0003-Don-t-install-Clang-static-libraries.patch
Patch10: clang-0004-Make-Clang-default-to-Westmere-on-Clear-Linux.patch
Patch11: clang-0005-Add-the-LLVM-major-version-number-to-the-Gold-LTO-pl.patch
Patch12: clang-0006-Add-a-couple-more-f-instructions-that-GCC-has-that-C.patch
Patch13: compiler-rt-0001-libsanitizer-Remove-cyclades-inclusion-in-sanitizer.patch

%description
"llvm" directory contains a VS Code Extension for doing syntax highlighting of
TableGen files and LLVM IR files.

%package bin
Summary: bin components for the llvm11 package.
Group: Binaries
Requires: llvm11-license = %{version}-%{release}

%description bin
bin components for the llvm11 package.


%package dev
Summary: dev components for the llvm11 package.
Group: Development
Requires: llvm11-lib = %{version}-%{release}
Requires: llvm11-bin = %{version}-%{release}
Provides: llvm11-devel = %{version}-%{release}
Requires: llvm11 = %{version}-%{release}

%description dev
dev components for the llvm11 package.


%package extras
Summary: extras components for the llvm11 package.
Group: Default

%description extras
extras components for the llvm11 package.


%package extras-libllvm
Summary: extras-libllvm components for the llvm11 package.
Group: Default

%description extras-libllvm
extras-libllvm components for the llvm11 package.


%package extras-libllvmtablegen
Summary: extras-libllvmtablegen components for the llvm11 package.
Group: Default

%description extras-libllvmtablegen
extras-libllvmtablegen components for the llvm11 package.


%package lib
Summary: lib components for the llvm11 package.
Group: Libraries
Requires: llvm11-license = %{version}-%{release}

%description lib
lib components for the llvm11 package.


%package license
Summary: license components for the llvm11 package.
Group: Default

%description license
license components for the llvm11 package.


%prep
%setup -q -n llvm-11.1.0.src
cd %{_builddir}
tar xf %{_sourcedir}/clang-11.1.0.src.tar.xz
cd %{_builddir}
tar xf %{_sourcedir}/clang-tools-extra-11.1.0.src.tar.xz
cd %{_builddir}
tar xf %{_sourcedir}/lld-11.1.0.src.tar.xz
cd %{_builddir}
tar xf %{_sourcedir}/openmp-11.1.0.src.tar.xz
cd %{_builddir}
tar xf %{_sourcedir}/compiler-rt-11.1.0.src.tar.xz
cd %{_builddir}
tar xf %{_sourcedir}/SPIRV-11.1.0.tar.gz
cd %{_builddir}/llvm-11.1.0.src
mkdir -p tools/clang
cp -r %{_builddir}/clang-11.1.0.src/* %{_builddir}/llvm-11.1.0.src/tools/clang
mkdir -p tools/clang/tools/extra
cp -r %{_builddir}/clang-tools-extra-11.1.0.src/* %{_builddir}/llvm-11.1.0.src/tools/clang/tools/extra
mkdir -p tools/lld
cp -r %{_builddir}/lld-11.1.0.src/* %{_builddir}/llvm-11.1.0.src/tools/lld
mkdir -p projects/openmp
cp -r %{_builddir}/openmp-11.1.0.src/* %{_builddir}/llvm-11.1.0.src/projects/openmp
mkdir -p projects/compiler-rt
cp -r %{_builddir}/compiler-rt-11.1.0.src/* %{_builddir}/llvm-11.1.0.src/projects/compiler-rt
mkdir -p projects/SPIRV
cp -r %{_builddir}/SPIRV-LLVM-Translator-bf7d21f9f4220643335d13117f3d601692093a96/* %{_builddir}/llvm-11.1.0.src/projects/SPIRV
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%build
## build_prepend content
# Bootstrap Clang and the table generators
# See https://build.opensuse.org/package/view_file/devel:tools:compiler/llvm10/llvm10.spec?expand=1
mkdir clr-bootstrap-build
pushd clr-bootstrap-build
CFLAGS="`sed -E 's/-Wl,\S+\s//g; s/-Wp,-D_FORTIFY_SOURCE=2//' <<<$CFLAGS` -fno-integrated-as"
CXXFLAGS="`sed -E 's/-Wl,\S+\s//g; s/-Wp,-D_FORTIFY_SOURCE=2//' <<<$CXXFLAGS` -fno-integrated-as"
%cmake .. \
-DCMAKE_BUILD_TYPE=Release \
-DBUILD_SHARED_LIBS:BOOL=OFF \
-DCMAKE_C_COMPILER=clang \
-DCMAKE_C_FLAGS="$CFLAGS -g0" \
-DCMAKE_CXX_COMPILER=clang++ \
-DCMAKE_CXX_FLAGS="$CXXFLAGS -g0" \
-DLLVM_BUILD_LLVM_DYLIB:BOOL=OFF \
-DLLVM_LINK_LLVM_DYLIB:BOOL=OFF \
-DLLVM_BUILD_TOOLS:BOOL=OFF \
-DLLVM_BUILD_UTILS:BOOL=OFF \
-DLLVM_BUILD_EXAMPLES:BOOL=OFF \
-DLLVM_POLLY_BUILD:BOOL=OFF \
-DLLVM_TOOL_CLANG_TOOLS_EXTRA_BUILD:BOOL=OFF \
-DLLVM_INCLUDE_TESTS:BOOL=OFF \
-DLLVM_ENABLE_ASSERTIONS=OFF \
-DLLVM_TARGETS_TO_BUILD=Native \
-DCLANG_ENABLE_ARCMT:BOOL=OFF \
-DCLANG_ENABLE_STATIC_ANALYZER:BOOL=OFF \
-DCOMPILER_RT_BUILD_SANITIZERS:BOOL=OFF \
-DCOMPILER_RT_BUILD_XRAY:BOOL=OFF \
-DLLDB_DISABLE_PYTHON=ON \
-DCMAKE_SKIP_RPATH:BOOL=OFF \
-DLLVM_LIBDIR_SUFFIX=64 \
-DLLVM_BINUTILS_INCDIR=/usr/include \
-DLLVM_HOST_TRIPLE="x86_64-generic-linux" \
-DPYTHON_EXECUTABLE:FILEPATH=/usr/bin/python3
make  %{?_smp_mflags}  VERBOSE=1 clang llvm-tblgen clang-tblgen
popd

export PATH=/usr/lib64/ccache/bin/:${PWD}/clr-bootstrap-build/bin:${PATH}
#export CC=${PWD}/clr-bootstrap-build/bin/clang
#export CXX=${PWD}/clr-bootstrap-build/bin/clang++
export LLVM_AR=${PWD}/clr-bootstrap-build/bin/llvm-ar
export LLVM_RANLIB=${PWD}/clr-bootstrap-build/bin/llvm-ranlib
export LLVM_TABLEGEN=${PWD}/clr-bootstrap-build/bin/llvm-tblgen
export CLANG_TABLEGEN=${PWD}/clr-bootstrap-build/bin/clang-tblgen
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1647647080
unset LD_AS_NEEDED
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CC=clang
export CXX=clang++
export LD=ld.gold
CFLAGS=${CFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
CXXFLAGS=${CXXFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
export CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error -Wl,-z,max-page-size=0x1000 -march=westmere -mtune=haswell"
export CXXFLAGS=$CFLAGS
export FFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wno-error -Wl,-z,max-page-size=0x1000 -march=westmere -mtune=haswell"
export FCFLAGS=$FFLAGS
unset LDFLAGS
unset LDFLAGS
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DCMAKE_C_FLAGS="`sed -E 's/-Wl,\S+\s//g; s/-Wp,-D_FORTIFY_SOURCE=2//' <<<$CFLAGS`" \
-DCMAKE_CXX_FLAGS="`sed -E 's/-Wl,\S+\s//g; s/-Wp,-D_FORTIFY_SOURCE=2//' <<<$CXXFLAGS`" \
-DCMAKE_EXE_LINKER_FLAGS="$CXXFLAGS -Wl,--as-needed -Wl,--build-id=sha1" \
-DCMAKE_MODULE_LINKER_FLAGS="$CXXFLAGS -Wl,--as-needed -Wl,--build-id=sha1" \
-DCMAKE_SHARED_LINKER_FLAGS="$CXXFLAGS -Wl,--as-needed -Wl,--build-id=sha1" \
-DENABLE_LINKER_BUILD_ID=ON \
-DBUILD_SHARED_LIBS:BOOL=OFF \
-DLLVM_LINK_LLVM_DYLIB:BOOL=ON \
-DCLANG_LINK_CLANG_DYLIB:BOOL=ON \
-DLLVM_BUILD_RUNTIME:BOOL=ON \
-DLLVM_BUILD_TOOLS:BOOL=ON \
-DLLVM_ENABLE_CXX1Y=ON \
-DLLVM_ENABLE_FFI:BOOL=ON -DFFI_INCLUDE_DIR=`pkg-config --variable=includedir libffi` \
-DLLVM_ENABLE_LIBCXX:BOOL=OFF \
-DLLVM_ENABLE_RTTI:BOOL=ON \
-DLLVM_ENABLE_ZLIB:BOOL=ON \
-DLLVM_INSTALL_UTILS:BOOL=OFF \
-DLLVM_REQUIRES_RTTI:BOOL=ON \
-DLLVM_TABLEGEN=$LLVM_TABLEGEN \
-DCLANG_TABLEGEN=$CLANG_TABLEGEN \
-DLLVM_SPIRV_BUILD_EXTERNAL:BOOL=ON \
-DLLVM_LIBDIR_SUFFIX=64 \
-DLLVM_BINUTILS_INCDIR=/usr/include \
-DLLVM_HOST_TRIPLE="x86_64-generic-linux" \
-DPYTHON_EXECUTABLE:FILEPATH=/usr/bin/python3 \
-DCLANG_TOOL_SCAN_VIEW_BUILD:BOOL=OFF \
-DCLANG_TOOL_SCAN_BUILD_BUILD:BOOL=OFF \
-DLLVM_TOOL_OPT_VIEWER_BUILD:BOOL=OFF \
-DLLVM_INSTALL_UTILS:BOOL=OFF \
-DCMAKE_C_COMPILER=clang-13 \
-DCMAKE_CXX_COMPILER=clang++-13
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make test

%install
export SOURCE_DATE_EPOCH=1647647080
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/llvm11
cp %{_builddir}/SPIRV-LLVM-Translator-bf7d21f9f4220643335d13117f3d601692093a96/LICENSE.TXT %{buildroot}/usr/share/package-licenses/llvm11/8f178caf2a2d6e6c711a30da69077572df356cf6
cp %{_builddir}/clang-11.1.0.src/LICENSE.TXT %{buildroot}/usr/share/package-licenses/llvm11/a1691103171dc1d21cfa85f1d4809a16b9f1367f
cp %{_builddir}/clang-11.1.0.src/tools/clang-format-vs/ClangFormat/license.txt %{buildroot}/usr/share/package-licenses/llvm11/b5d4ab4d1191e592c03310adfbe90d99a46bf9d7
cp %{_builddir}/clang-tools-extra-11.1.0.src/LICENSE.TXT %{buildroot}/usr/share/package-licenses/llvm11/a1691103171dc1d21cfa85f1d4809a16b9f1367f
cp %{_builddir}/compiler-rt-11.1.0.src/LICENSE.TXT %{buildroot}/usr/share/package-licenses/llvm11/f4359b9da55a3b9e4d9513eb79cacf125fb49e7b
cp %{_builddir}/lld-11.1.0.src/LICENSE.TXT %{buildroot}/usr/share/package-licenses/llvm11/6b655b0685aa7ee33fa1e02103b3bf22ed06e099
cp %{_builddir}/llvm-11.1.0.src/LICENSE.TXT %{buildroot}/usr/share/package-licenses/llvm11/af07f365643f841c69797e9059b66f0bd847f1cd
cp %{_builddir}/llvm-11.1.0.src/test/YAMLParser/LICENSE.txt %{buildroot}/usr/share/package-licenses/llvm11/c01c212bdf3925189f673e2081b44094023860ea
cp %{_builddir}/llvm-11.1.0.src/tools/msbuild/license.txt %{buildroot}/usr/share/package-licenses/llvm11/b5d4ab4d1191e592c03310adfbe90d99a46bf9d7
cp %{_builddir}/llvm-11.1.0.src/utils/benchmark/LICENSE %{buildroot}/usr/share/package-licenses/llvm11/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/llvm-11.1.0.src/utils/unittest/googlemock/LICENSE.txt %{buildroot}/usr/share/package-licenses/llvm11/5a2314153eadadc69258a9429104cd11804ea304
cp %{_builddir}/llvm-11.1.0.src/utils/unittest/googletest/LICENSE.TXT %{buildroot}/usr/share/package-licenses/llvm11/5a2314153eadadc69258a9429104cd11804ea304
cp %{_builddir}/openmp-11.1.0.src/LICENSE.txt %{buildroot}/usr/share/package-licenses/llvm11/e3cccabb67bd491a643d32a7d2b65b49836e626d
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}*/usr/lib64/libgomp.so
rm -f %{buildroot}*/usr/lib64/TestPlugin.so
rm -f %{buildroot}*/usr/lib64/cmake/llvm/LLVMStaticExports.cmake
rm -f %{buildroot}*/usr/lib64/cmake/llvm/LLVMStaticExports-relwithdebinfo.cmake
rm -f %{buildroot}*/usr/lib64/clang/9.0.0/lib/linux/libclang_rt.asan-i386.so
rm -f %{buildroot}*/usr/lib64/clang/9.0.0/lib/linux/libclang_rt.scudo-i386.so
rm -f %{buildroot}*/usr/lib64/clang/9.0.0/lib/linux/libclang_rt.scudo_minimal-i386.so
rm -f %{buildroot}*/usr/lib64/clang/9.0.0/lib/linux/libclang_rt.ubsan_minimal-i386.so
rm -f %{buildroot}*/usr/lib64/clang/9.0.0/lib/linux/libclang_rt.ubsan_standalone-i386.so
rm -f %{buildroot}*/usr/lib64/pkgconfig/LLVMSPIRVLib.pc
rm -f %{buildroot}*/usr/lib32/pkgconfig/32LLVMSPIRVLib.pc
rm -f %{buildroot}*/usr/lib32/pkgconfig/LLVMSPIRVLib.pc
## install_append content
# Rename the Gold plugin elsewhere, as we're erasing *.so below
mv %{buildroot}/usr/lib64/LLVMgold.so %{buildroot}/usr/lib64/LLVMgold.so.save

# Remove files that should come from the main llvm package
rm -rf %{buildroot}/usr/include
rm -rf %{buildroot}/usr/lib64/*.a
rm -rf %{buildroot}/usr/lib64/*.so
rm -rf %{buildroot}/usr/lib64/cmake
rm -rf %{buildroot}/usr/lib64/pkgconfig
rm -rf %{buildroot}/usr/libexec

mv %{buildroot}/usr/share/package-licenses %{buildroot}/usr/
rm -rf %{buildroot}/usr/share/*
mv %{buildroot}/usr/package-licenses %{buildroot}/usr/share

# Rename the tools to have a versioned suffix and symlink back
pushd %{buildroot}/usr
FULL_VERSION=%{version}
VERSION=${FULL_VERSION%%%%.*}
mkdir -p lib64/clang/$FULL_VERSION/bin
mv bin/* lib64/clang/$FULL_VERSION/bin
for f in lib64/clang/$FULL_VERSION/bin/*; do
case "$f" in
*-$VERSION)
# Already versioned, leave it alone
continue
;;
esac
ln -s ../$f bin/${f##*/}-$VERSION
done

# libclang-cpp auto-relocates, so create a symlink so it finds its files
ln -s ../.. lib64/clang/$FULL_VERSION/lib64

# Put the LLVM gold plugin back, under the versioned name
mv lib64/LLVMgold.so.save lib64/LLVMgold-$VERSION.so
mkdir -p lib/bfd-plugins
ln -s ../../lib64/LLVMgold-$VERSION.so lib/bfd-plugins
popd
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/clang/11.1.0/bin/bugpoint
/usr/lib64/clang/11.1.0/bin/c-index-test
/usr/lib64/clang/11.1.0/bin/clang
/usr/lib64/clang/11.1.0/bin/clang++
/usr/lib64/clang/11.1.0/bin/clang-11
/usr/lib64/clang/11.1.0/bin/clang-apply-replacements
/usr/lib64/clang/11.1.0/bin/clang-change-namespace
/usr/lib64/clang/11.1.0/bin/clang-check
/usr/lib64/clang/11.1.0/bin/clang-cl
/usr/lib64/clang/11.1.0/bin/clang-cpp
/usr/lib64/clang/11.1.0/bin/clang-doc
/usr/lib64/clang/11.1.0/bin/clang-extdef-mapping
/usr/lib64/clang/11.1.0/bin/clang-format
/usr/lib64/clang/11.1.0/bin/clang-include-fixer
/usr/lib64/clang/11.1.0/bin/clang-move
/usr/lib64/clang/11.1.0/bin/clang-offload-bundler
/usr/lib64/clang/11.1.0/bin/clang-offload-wrapper
/usr/lib64/clang/11.1.0/bin/clang-query
/usr/lib64/clang/11.1.0/bin/clang-refactor
/usr/lib64/clang/11.1.0/bin/clang-rename
/usr/lib64/clang/11.1.0/bin/clang-reorder-fields
/usr/lib64/clang/11.1.0/bin/clang-scan-deps
/usr/lib64/clang/11.1.0/bin/clang-tidy
/usr/lib64/clang/11.1.0/bin/clangd
/usr/lib64/clang/11.1.0/bin/diagtool
/usr/lib64/clang/11.1.0/bin/dsymutil
/usr/lib64/clang/11.1.0/bin/find-all-symbols
/usr/lib64/clang/11.1.0/bin/git-clang-format
/usr/lib64/clang/11.1.0/bin/hmaptool
/usr/lib64/clang/11.1.0/bin/hwasan_symbolize
/usr/lib64/clang/11.1.0/bin/ld.lld
/usr/lib64/clang/11.1.0/bin/ld64.lld
/usr/lib64/clang/11.1.0/bin/llc
/usr/lib64/clang/11.1.0/bin/lld
/usr/lib64/clang/11.1.0/bin/lld-link
/usr/lib64/clang/11.1.0/bin/lli
/usr/lib64/clang/11.1.0/bin/llvm-addr2line
/usr/lib64/clang/11.1.0/bin/llvm-ar
/usr/lib64/clang/11.1.0/bin/llvm-as
/usr/lib64/clang/11.1.0/bin/llvm-bcanalyzer
/usr/lib64/clang/11.1.0/bin/llvm-c-test
/usr/lib64/clang/11.1.0/bin/llvm-cat
/usr/lib64/clang/11.1.0/bin/llvm-cfi-verify
/usr/lib64/clang/11.1.0/bin/llvm-config
/usr/lib64/clang/11.1.0/bin/llvm-cov
/usr/lib64/clang/11.1.0/bin/llvm-cvtres
/usr/lib64/clang/11.1.0/bin/llvm-cxxdump
/usr/lib64/clang/11.1.0/bin/llvm-cxxfilt
/usr/lib64/clang/11.1.0/bin/llvm-cxxmap
/usr/lib64/clang/11.1.0/bin/llvm-diff
/usr/lib64/clang/11.1.0/bin/llvm-dis
/usr/lib64/clang/11.1.0/bin/llvm-dlltool
/usr/lib64/clang/11.1.0/bin/llvm-dwarfdump
/usr/lib64/clang/11.1.0/bin/llvm-dwp
/usr/lib64/clang/11.1.0/bin/llvm-elfabi
/usr/lib64/clang/11.1.0/bin/llvm-exegesis
/usr/lib64/clang/11.1.0/bin/llvm-extract
/usr/lib64/clang/11.1.0/bin/llvm-gsymutil
/usr/lib64/clang/11.1.0/bin/llvm-ifs
/usr/lib64/clang/11.1.0/bin/llvm-install-name-tool
/usr/lib64/clang/11.1.0/bin/llvm-jitlink
/usr/lib64/clang/11.1.0/bin/llvm-lib
/usr/lib64/clang/11.1.0/bin/llvm-link
/usr/lib64/clang/11.1.0/bin/llvm-lipo
/usr/lib64/clang/11.1.0/bin/llvm-lto
/usr/lib64/clang/11.1.0/bin/llvm-lto2
/usr/lib64/clang/11.1.0/bin/llvm-mc
/usr/lib64/clang/11.1.0/bin/llvm-mca
/usr/lib64/clang/11.1.0/bin/llvm-ml
/usr/lib64/clang/11.1.0/bin/llvm-modextract
/usr/lib64/clang/11.1.0/bin/llvm-mt
/usr/lib64/clang/11.1.0/bin/llvm-nm
/usr/lib64/clang/11.1.0/bin/llvm-objcopy
/usr/lib64/clang/11.1.0/bin/llvm-objdump
/usr/lib64/clang/11.1.0/bin/llvm-opt-report
/usr/lib64/clang/11.1.0/bin/llvm-pdbutil
/usr/lib64/clang/11.1.0/bin/llvm-profdata
/usr/lib64/clang/11.1.0/bin/llvm-ranlib
/usr/lib64/clang/11.1.0/bin/llvm-rc
/usr/lib64/clang/11.1.0/bin/llvm-readelf
/usr/lib64/clang/11.1.0/bin/llvm-readobj
/usr/lib64/clang/11.1.0/bin/llvm-reduce
/usr/lib64/clang/11.1.0/bin/llvm-rtdyld
/usr/lib64/clang/11.1.0/bin/llvm-size
/usr/lib64/clang/11.1.0/bin/llvm-spirv
/usr/lib64/clang/11.1.0/bin/llvm-split
/usr/lib64/clang/11.1.0/bin/llvm-stress
/usr/lib64/clang/11.1.0/bin/llvm-strings
/usr/lib64/clang/11.1.0/bin/llvm-strip
/usr/lib64/clang/11.1.0/bin/llvm-symbolizer
/usr/lib64/clang/11.1.0/bin/llvm-tblgen
/usr/lib64/clang/11.1.0/bin/llvm-undname
/usr/lib64/clang/11.1.0/bin/llvm-xray
/usr/lib64/clang/11.1.0/bin/modularize
/usr/lib64/clang/11.1.0/bin/obj2yaml
/usr/lib64/clang/11.1.0/bin/opt
/usr/lib64/clang/11.1.0/bin/pp-trace
/usr/lib64/clang/11.1.0/bin/sancov
/usr/lib64/clang/11.1.0/bin/sanstats
/usr/lib64/clang/11.1.0/bin/verify-uselistorder
/usr/lib64/clang/11.1.0/bin/wasm-ld
/usr/lib64/clang/11.1.0/bin/yaml2obj
/usr/lib64/clang/11.1.0/include/openmp_wrappers/cmath
/usr/lib64/clang/11.1.0/include/openmp_wrappers/complex
/usr/lib64/clang/11.1.0/include/openmp_wrappers/new
/usr/lib64/clang/11.1.0/include/profile/InstrProfData.inc
/usr/lib64/clang/11.1.0/lib/linux/clang_rt.crtbegin-x86_64.o
/usr/lib64/clang/11.1.0/lib/linux/clang_rt.crtend-x86_64.o
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.asan-preinit-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.asan-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.asan-x86_64.a.syms
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.asan_cxx-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.asan_cxx-x86_64.a.syms
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.builtins-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.cfi-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.cfi_diag-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.dd-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.dfsan-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.dfsan-x86_64.a.syms
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.fuzzer-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.fuzzer_no_main-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.gwp_asan-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.hwasan-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.hwasan-x86_64.a.syms
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.hwasan_cxx-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.hwasan_cxx-x86_64.a.syms
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.lsan-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.msan-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.msan-x86_64.a.syms
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.msan_cxx-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.msan_cxx-x86_64.a.syms
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.profile-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.safestack-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.scudo-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.scudo_cxx-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.scudo_cxx_minimal-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.scudo_minimal-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.scudo_standalone-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.scudo_standalone_cxx-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.stats-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.stats_client-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.tsan-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.tsan-x86_64.a.syms
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.tsan_cxx-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.tsan_cxx-x86_64.a.syms
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.ubsan_minimal-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.ubsan_minimal-x86_64.a.syms
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.ubsan_standalone-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.ubsan_standalone-x86_64.a.syms
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.ubsan_standalone_cxx-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.ubsan_standalone_cxx-x86_64.a.syms
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.xray-basic-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.xray-fdr-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.xray-profiling-x86_64.a
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.xray-x86_64.a
/usr/lib64/clang/11.1.0/lib64
/usr/lib64/clang/11.1.0/share/asan_blacklist.txt
/usr/lib64/clang/11.1.0/share/cfi_blacklist.txt
/usr/lib64/clang/11.1.0/share/dfsan_abilist.txt
/usr/lib64/clang/11.1.0/share/hwasan_blacklist.txt
/usr/lib64/clang/11.1.0/share/msan_blacklist.txt

%files bin
%defattr(-,root,root,-)
/usr/bin/bugpoint-11
/usr/bin/c-index-test-11
/usr/bin/clang++-11
/usr/bin/clang-11
/usr/bin/clang-apply-replacements-11
/usr/bin/clang-change-namespace-11
/usr/bin/clang-check-11
/usr/bin/clang-cl-11
/usr/bin/clang-cpp-11
/usr/bin/clang-doc-11
/usr/bin/clang-extdef-mapping-11
/usr/bin/clang-format-11
/usr/bin/clang-include-fixer-11
/usr/bin/clang-move-11
/usr/bin/clang-offload-bundler-11
/usr/bin/clang-offload-wrapper-11
/usr/bin/clang-query-11
/usr/bin/clang-refactor-11
/usr/bin/clang-rename-11
/usr/bin/clang-reorder-fields-11
/usr/bin/clang-scan-deps-11
/usr/bin/clang-tidy-11
/usr/bin/clangd-11
/usr/bin/diagtool-11
/usr/bin/dsymutil-11
/usr/bin/find-all-symbols-11
/usr/bin/git-clang-format-11
/usr/bin/hmaptool-11
/usr/bin/hwasan_symbolize-11
/usr/bin/ld.lld-11
/usr/bin/ld64.lld-11
/usr/bin/llc-11
/usr/bin/lld-11
/usr/bin/lld-link-11
/usr/bin/lli-11
/usr/bin/llvm-addr2line-11
/usr/bin/llvm-ar-11
/usr/bin/llvm-as-11
/usr/bin/llvm-bcanalyzer-11
/usr/bin/llvm-c-test-11
/usr/bin/llvm-cat-11
/usr/bin/llvm-cfi-verify-11
/usr/bin/llvm-config-11
/usr/bin/llvm-cov-11
/usr/bin/llvm-cvtres-11
/usr/bin/llvm-cxxdump-11
/usr/bin/llvm-cxxfilt-11
/usr/bin/llvm-cxxmap-11
/usr/bin/llvm-diff-11
/usr/bin/llvm-dis-11
/usr/bin/llvm-dlltool-11
/usr/bin/llvm-dwarfdump-11
/usr/bin/llvm-dwp-11
/usr/bin/llvm-elfabi-11
/usr/bin/llvm-exegesis-11
/usr/bin/llvm-extract-11
/usr/bin/llvm-gsymutil-11
/usr/bin/llvm-ifs-11
/usr/bin/llvm-install-name-tool-11
/usr/bin/llvm-jitlink-11
/usr/bin/llvm-lib-11
/usr/bin/llvm-link-11
/usr/bin/llvm-lipo-11
/usr/bin/llvm-lto-11
/usr/bin/llvm-lto2-11
/usr/bin/llvm-mc-11
/usr/bin/llvm-mca-11
/usr/bin/llvm-ml-11
/usr/bin/llvm-modextract-11
/usr/bin/llvm-mt-11
/usr/bin/llvm-nm-11
/usr/bin/llvm-objcopy-11
/usr/bin/llvm-objdump-11
/usr/bin/llvm-opt-report-11
/usr/bin/llvm-pdbutil-11
/usr/bin/llvm-profdata-11
/usr/bin/llvm-ranlib-11
/usr/bin/llvm-rc-11
/usr/bin/llvm-readelf-11
/usr/bin/llvm-readobj-11
/usr/bin/llvm-reduce-11
/usr/bin/llvm-rtdyld-11
/usr/bin/llvm-size-11
/usr/bin/llvm-spirv-11
/usr/bin/llvm-split-11
/usr/bin/llvm-stress-11
/usr/bin/llvm-strings-11
/usr/bin/llvm-strip-11
/usr/bin/llvm-symbolizer-11
/usr/bin/llvm-tblgen-11
/usr/bin/llvm-undname-11
/usr/bin/llvm-xray-11
/usr/bin/modularize-11
/usr/bin/obj2yaml-11
/usr/bin/opt-11
/usr/bin/pp-trace-11
/usr/bin/sancov-11
/usr/bin/sanstats-11
/usr/bin/verify-uselistorder-11
/usr/bin/wasm-ld-11
/usr/bin/yaml2obj-11

%files dev
%defattr(-,root,root,-)
/usr/lib64/clang/11.1.0/include/__clang_cuda_math.h
/usr/lib64/clang/11.1.0/include/__clang_hip_libdevice_declares.h
/usr/lib64/clang/11.1.0/include/__clang_hip_math.h
/usr/lib64/clang/11.1.0/include/__clang_hip_runtime_wrapper.h
/usr/lib64/clang/11.1.0/include/amxintrin.h
/usr/lib64/clang/11.1.0/include/arm_bf16.h
/usr/lib64/clang/11.1.0/include/arm_cde.h
/usr/lib64/clang/11.1.0/include/arm_sve.h
/usr/lib64/clang/11.1.0/include/cet.h
/usr/lib64/clang/11.1.0/include/openmp_wrappers/__clang_openmp_device_functions.h
/usr/lib64/clang/11.1.0/include/openmp_wrappers/complex.h
/usr/lib64/clang/11.1.0/include/serializeintrin.h
/usr/lib64/clang/11.1.0/include/tsxldtrkintrin.h
/usr/lib64/clang/11.1.0/include/wasm_simd128.h

%files extras
%defattr(-,root,root,-)
/usr/lib/bfd-plugins/LLVMgold-11.so
/usr/lib64/LLVMgold-11.so
/usr/lib64/clang/11.1.0/include/__clang_cuda_builtin_vars.h
/usr/lib64/clang/11.1.0/include/__clang_cuda_cmath.h
/usr/lib64/clang/11.1.0/include/__clang_cuda_complex_builtins.h
/usr/lib64/clang/11.1.0/include/__clang_cuda_device_functions.h
/usr/lib64/clang/11.1.0/include/__clang_cuda_intrinsics.h
/usr/lib64/clang/11.1.0/include/__clang_cuda_libdevice_declares.h
/usr/lib64/clang/11.1.0/include/__clang_cuda_math_forward_declares.h
/usr/lib64/clang/11.1.0/include/__clang_cuda_runtime_wrapper.h
/usr/lib64/clang/11.1.0/include/__stddef_max_align_t.h
/usr/lib64/clang/11.1.0/include/__wmmintrin_aes.h
/usr/lib64/clang/11.1.0/include/__wmmintrin_pclmul.h
/usr/lib64/clang/11.1.0/include/adxintrin.h
/usr/lib64/clang/11.1.0/include/altivec.h
/usr/lib64/clang/11.1.0/include/ammintrin.h
/usr/lib64/clang/11.1.0/include/arm64intr.h
/usr/lib64/clang/11.1.0/include/arm_acle.h
/usr/lib64/clang/11.1.0/include/arm_cmse.h
/usr/lib64/clang/11.1.0/include/arm_fp16.h
/usr/lib64/clang/11.1.0/include/arm_mve.h
/usr/lib64/clang/11.1.0/include/arm_neon.h
/usr/lib64/clang/11.1.0/include/armintr.h
/usr/lib64/clang/11.1.0/include/avx2intrin.h
/usr/lib64/clang/11.1.0/include/avx512bf16intrin.h
/usr/lib64/clang/11.1.0/include/avx512bitalgintrin.h
/usr/lib64/clang/11.1.0/include/avx512bwintrin.h
/usr/lib64/clang/11.1.0/include/avx512cdintrin.h
/usr/lib64/clang/11.1.0/include/avx512dqintrin.h
/usr/lib64/clang/11.1.0/include/avx512erintrin.h
/usr/lib64/clang/11.1.0/include/avx512fintrin.h
/usr/lib64/clang/11.1.0/include/avx512ifmaintrin.h
/usr/lib64/clang/11.1.0/include/avx512ifmavlintrin.h
/usr/lib64/clang/11.1.0/include/avx512pfintrin.h
/usr/lib64/clang/11.1.0/include/avx512vbmi2intrin.h
/usr/lib64/clang/11.1.0/include/avx512vbmiintrin.h
/usr/lib64/clang/11.1.0/include/avx512vbmivlintrin.h
/usr/lib64/clang/11.1.0/include/avx512vlbf16intrin.h
/usr/lib64/clang/11.1.0/include/avx512vlbitalgintrin.h
/usr/lib64/clang/11.1.0/include/avx512vlbwintrin.h
/usr/lib64/clang/11.1.0/include/avx512vlcdintrin.h
/usr/lib64/clang/11.1.0/include/avx512vldqintrin.h
/usr/lib64/clang/11.1.0/include/avx512vlintrin.h
/usr/lib64/clang/11.1.0/include/avx512vlvbmi2intrin.h
/usr/lib64/clang/11.1.0/include/avx512vlvnniintrin.h
/usr/lib64/clang/11.1.0/include/avx512vlvp2intersectintrin.h
/usr/lib64/clang/11.1.0/include/avx512vnniintrin.h
/usr/lib64/clang/11.1.0/include/avx512vp2intersectintrin.h
/usr/lib64/clang/11.1.0/include/avx512vpopcntdqintrin.h
/usr/lib64/clang/11.1.0/include/avx512vpopcntdqvlintrin.h
/usr/lib64/clang/11.1.0/include/avxintrin.h
/usr/lib64/clang/11.1.0/include/bmi2intrin.h
/usr/lib64/clang/11.1.0/include/bmiintrin.h
/usr/lib64/clang/11.1.0/include/cetintrin.h
/usr/lib64/clang/11.1.0/include/cldemoteintrin.h
/usr/lib64/clang/11.1.0/include/clflushoptintrin.h
/usr/lib64/clang/11.1.0/include/clwbintrin.h
/usr/lib64/clang/11.1.0/include/clzerointrin.h
/usr/lib64/clang/11.1.0/include/cpuid.h
/usr/lib64/clang/11.1.0/include/cuda_wrappers/algorithm
/usr/lib64/clang/11.1.0/include/cuda_wrappers/complex
/usr/lib64/clang/11.1.0/include/cuda_wrappers/new
/usr/lib64/clang/11.1.0/include/emmintrin.h
/usr/lib64/clang/11.1.0/include/enqcmdintrin.h
/usr/lib64/clang/11.1.0/include/f16cintrin.h
/usr/lib64/clang/11.1.0/include/float.h
/usr/lib64/clang/11.1.0/include/fma4intrin.h
/usr/lib64/clang/11.1.0/include/fmaintrin.h
/usr/lib64/clang/11.1.0/include/fuzzer/FuzzedDataProvider.h
/usr/lib64/clang/11.1.0/include/fxsrintrin.h
/usr/lib64/clang/11.1.0/include/gfniintrin.h
/usr/lib64/clang/11.1.0/include/htmintrin.h
/usr/lib64/clang/11.1.0/include/htmxlintrin.h
/usr/lib64/clang/11.1.0/include/ia32intrin.h
/usr/lib64/clang/11.1.0/include/immintrin.h
/usr/lib64/clang/11.1.0/include/intrin.h
/usr/lib64/clang/11.1.0/include/inttypes.h
/usr/lib64/clang/11.1.0/include/invpcidintrin.h
/usr/lib64/clang/11.1.0/include/iso646.h
/usr/lib64/clang/11.1.0/include/limits.h
/usr/lib64/clang/11.1.0/include/lwpintrin.h
/usr/lib64/clang/11.1.0/include/lzcntintrin.h
/usr/lib64/clang/11.1.0/include/mm3dnow.h
/usr/lib64/clang/11.1.0/include/mm_malloc.h
/usr/lib64/clang/11.1.0/include/mmintrin.h
/usr/lib64/clang/11.1.0/include/module.modulemap
/usr/lib64/clang/11.1.0/include/movdirintrin.h
/usr/lib64/clang/11.1.0/include/msa.h
/usr/lib64/clang/11.1.0/include/mwaitxintrin.h
/usr/lib64/clang/11.1.0/include/nmmintrin.h
/usr/lib64/clang/11.1.0/include/omp-tools.h
/usr/lib64/clang/11.1.0/include/omp.h
/usr/lib64/clang/11.1.0/include/ompt.h
/usr/lib64/clang/11.1.0/include/opencl-c-base.h
/usr/lib64/clang/11.1.0/include/opencl-c.h
/usr/lib64/clang/11.1.0/include/openmp_wrappers/math.h
/usr/lib64/clang/11.1.0/include/pconfigintrin.h
/usr/lib64/clang/11.1.0/include/pkuintrin.h
/usr/lib64/clang/11.1.0/include/pmmintrin.h
/usr/lib64/clang/11.1.0/include/popcntintrin.h
/usr/lib64/clang/11.1.0/include/ppc_wrappers/emmintrin.h
/usr/lib64/clang/11.1.0/include/ppc_wrappers/mm_malloc.h
/usr/lib64/clang/11.1.0/include/ppc_wrappers/mmintrin.h
/usr/lib64/clang/11.1.0/include/ppc_wrappers/pmmintrin.h
/usr/lib64/clang/11.1.0/include/ppc_wrappers/smmintrin.h
/usr/lib64/clang/11.1.0/include/ppc_wrappers/tmmintrin.h
/usr/lib64/clang/11.1.0/include/ppc_wrappers/xmmintrin.h
/usr/lib64/clang/11.1.0/include/prfchwintrin.h
/usr/lib64/clang/11.1.0/include/ptwriteintrin.h
/usr/lib64/clang/11.1.0/include/rdseedintrin.h
/usr/lib64/clang/11.1.0/include/rtmintrin.h
/usr/lib64/clang/11.1.0/include/s390intrin.h
/usr/lib64/clang/11.1.0/include/sanitizer/allocator_interface.h
/usr/lib64/clang/11.1.0/include/sanitizer/asan_interface.h
/usr/lib64/clang/11.1.0/include/sanitizer/common_interface_defs.h
/usr/lib64/clang/11.1.0/include/sanitizer/coverage_interface.h
/usr/lib64/clang/11.1.0/include/sanitizer/dfsan_interface.h
/usr/lib64/clang/11.1.0/include/sanitizer/hwasan_interface.h
/usr/lib64/clang/11.1.0/include/sanitizer/linux_syscall_hooks.h
/usr/lib64/clang/11.1.0/include/sanitizer/lsan_interface.h
/usr/lib64/clang/11.1.0/include/sanitizer/msan_interface.h
/usr/lib64/clang/11.1.0/include/sanitizer/netbsd_syscall_hooks.h
/usr/lib64/clang/11.1.0/include/sanitizer/scudo_interface.h
/usr/lib64/clang/11.1.0/include/sanitizer/tsan_interface.h
/usr/lib64/clang/11.1.0/include/sanitizer/tsan_interface_atomic.h
/usr/lib64/clang/11.1.0/include/sanitizer/ubsan_interface.h
/usr/lib64/clang/11.1.0/include/sgxintrin.h
/usr/lib64/clang/11.1.0/include/shaintrin.h
/usr/lib64/clang/11.1.0/include/smmintrin.h
/usr/lib64/clang/11.1.0/include/stdalign.h
/usr/lib64/clang/11.1.0/include/stdarg.h
/usr/lib64/clang/11.1.0/include/stdatomic.h
/usr/lib64/clang/11.1.0/include/stdbool.h
/usr/lib64/clang/11.1.0/include/stddef.h
/usr/lib64/clang/11.1.0/include/stdint.h
/usr/lib64/clang/11.1.0/include/stdnoreturn.h
/usr/lib64/clang/11.1.0/include/tbmintrin.h
/usr/lib64/clang/11.1.0/include/tgmath.h
/usr/lib64/clang/11.1.0/include/tmmintrin.h
/usr/lib64/clang/11.1.0/include/unwind.h
/usr/lib64/clang/11.1.0/include/vadefs.h
/usr/lib64/clang/11.1.0/include/vaesintrin.h
/usr/lib64/clang/11.1.0/include/varargs.h
/usr/lib64/clang/11.1.0/include/vecintrin.h
/usr/lib64/clang/11.1.0/include/vpclmulqdqintrin.h
/usr/lib64/clang/11.1.0/include/waitpkgintrin.h
/usr/lib64/clang/11.1.0/include/wbnoinvdintrin.h
/usr/lib64/clang/11.1.0/include/wmmintrin.h
/usr/lib64/clang/11.1.0/include/x86intrin.h
/usr/lib64/clang/11.1.0/include/xmmintrin.h
/usr/lib64/clang/11.1.0/include/xopintrin.h
/usr/lib64/clang/11.1.0/include/xray/xray_interface.h
/usr/lib64/clang/11.1.0/include/xray/xray_log_interface.h
/usr/lib64/clang/11.1.0/include/xray/xray_records.h
/usr/lib64/clang/11.1.0/include/xsavecintrin.h
/usr/lib64/clang/11.1.0/include/xsaveintrin.h
/usr/lib64/clang/11.1.0/include/xsaveoptintrin.h
/usr/lib64/clang/11.1.0/include/xsavesintrin.h
/usr/lib64/clang/11.1.0/include/xtestintrin.h
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.asan-x86_64.so
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.dyndd-x86_64.so
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.hwasan-x86_64.so
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.scudo-x86_64.so
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.scudo_minimal-x86_64.so
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.ubsan_minimal-x86_64.so
/usr/lib64/clang/11.1.0/lib/linux/libclang_rt.ubsan_standalone-x86_64.so

%files extras-libllvm
%defattr(-,root,root,-)
/usr/lib64/libLLVM.so.11

%files extras-libllvmtablegen
%defattr(-,root,root,-)
/usr/lib64/libLLVMTableGen.so.11

%files lib
%defattr(-,root,root,-)
/usr/lib64/libLTO.so.11
/usr/lib64/libRemarks.so.11
/usr/lib64/libclang-cpp.so.11.1
/usr/lib64/libclang.so.11.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/llvm11/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/llvm11/5a2314153eadadc69258a9429104cd11804ea304
/usr/share/package-licenses/llvm11/6b655b0685aa7ee33fa1e02103b3bf22ed06e099
/usr/share/package-licenses/llvm11/8f178caf2a2d6e6c711a30da69077572df356cf6
/usr/share/package-licenses/llvm11/a1691103171dc1d21cfa85f1d4809a16b9f1367f
/usr/share/package-licenses/llvm11/af07f365643f841c69797e9059b66f0bd847f1cd
/usr/share/package-licenses/llvm11/b5d4ab4d1191e592c03310adfbe90d99a46bf9d7
/usr/share/package-licenses/llvm11/c01c212bdf3925189f673e2081b44094023860ea
/usr/share/package-licenses/llvm11/e3cccabb67bd491a643d32a7d2b65b49836e626d
/usr/share/package-licenses/llvm11/f4359b9da55a3b9e4d9513eb79cacf125fb49e7b
