#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pint
Version  : 0.20
Release  : 6
URL      : https://files.pythonhosted.org/packages/29/94/d5a951f0312a9824154fdf2e6a73bc4f9f487df11dbc8a2dbf3da7796130/Pint-0.20.tar.gz
Source0  : https://files.pythonhosted.org/packages/29/94/d5a951f0312a9824154fdf2e6a73bc4f9f487df11dbc8a2dbf3da7796130/Pint-0.20.tar.gz
Summary  : Physical quantities module
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-pint-bin = %{version}-%{release}
Requires: pypi-pint-license = %{version}-%{release}
Requires: pypi-pint-python = %{version}-%{release}
Requires: pypi-pint-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)

%description
.. image:: https://img.shields.io/pypi/v/pint.svg
:target: https://pypi.python.org/pypi/pint
:alt: Latest Version

%package bin
Summary: bin components for the pypi-pint package.
Group: Binaries
Requires: pypi-pint-license = %{version}-%{release}

%description bin
bin components for the pypi-pint package.


%package license
Summary: license components for the pypi-pint package.
Group: Default

%description license
license components for the pypi-pint package.


%package python
Summary: python components for the pypi-pint package.
Group: Default
Requires: pypi-pint-python3 = %{version}-%{release}

%description python
python components for the pypi-pint package.


%package python3
Summary: python3 components for the pypi-pint package.
Group: Default
Requires: python3-core
Provides: pypi(pint)

%description python3
python3 components for the pypi-pint package.


%prep
%setup -q -n Pint-0.20
cd %{_builddir}/Pint-0.20
pushd ..
cp -a Pint-0.20 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666863553
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pint
cp %{_builddir}/Pint-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pint/39c7163c5c236aaaaf2a5847b6e32022259d6f23 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pint-convert

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pint/39c7163c5c236aaaaf2a5847b6e32022259d6f23

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
