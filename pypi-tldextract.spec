#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-tldextract
Version  : 3.5.0
Release  : 46
URL      : https://files.pythonhosted.org/packages/50/c6/3a555f4a1b22c66c70b0450353a0cab91c3946b8a0a732d8b72e60047103/tldextract-3.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/50/c6/3a555f4a1b22c66c70b0450353a0cab91c3946b8a0a732d8b72e60047103/tldextract-3.5.0.tar.gz
Summary  : Accurately separates a URL's subdomain, domain, and public suffix, using the Public Suffix List (PSL). By default, this includes the public ICANN TLDs and their exceptions. You can optionally support the Public Suffix List's private domains as well.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-tldextract-bin = %{version}-%{release}
Requires: pypi-tldextract-license = %{version}-%{release}
Requires: pypi-tldextract-python = %{version}-%{release}
Requires: pypi-tldextract-python3 = %{version}-%{release}
Requires: pypi(requests_file)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# tldextract [![PyPI version](https://badge.fury.io/py/tldextract.svg)](https://badge.fury.io/py/tldextract) [![Build Status](https://travis-ci.com/john-kurkowski/tldextract.svg?branch=master)](https://app.travis-ci.com/github/john-kurkowski/tldextract)

%package bin
Summary: bin components for the pypi-tldextract package.
Group: Binaries
Requires: pypi-tldextract-license = %{version}-%{release}

%description bin
bin components for the pypi-tldextract package.


%package license
Summary: license components for the pypi-tldextract package.
Group: Default

%description license
license components for the pypi-tldextract package.


%package python
Summary: python components for the pypi-tldextract package.
Group: Default
Requires: pypi-tldextract-python3 = %{version}-%{release}

%description python
python components for the pypi-tldextract package.


%package python3
Summary: python3 components for the pypi-tldextract package.
Group: Default
Requires: python3-core
Provides: pypi(tldextract)
Requires: pypi(filelock)
Requires: pypi(idna)
Requires: pypi(requests)
Requires: pypi(requests_file)

%description python3
python3 components for the pypi-tldextract package.


%prep
%setup -q -n tldextract-3.5.0
cd %{_builddir}/tldextract-3.5.0
pushd ..
cp -a tldextract-3.5.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1694101603
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-tldextract
cp %{_builddir}/tldextract-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-tldextract/b8641358e21254308b9a6258fc93eed20c9f7960 || :
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
/usr/bin/tldextract

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-tldextract/b8641358e21254308b9a6258fc93eed20c9f7960

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
