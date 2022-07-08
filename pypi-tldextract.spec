#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-tldextract
Version  : 3.3.1
Release  : 36
URL      : https://files.pythonhosted.org/packages/80/d8/75264c54cfa1371d2a42fb613c24d71628c411764ab0d5046b54ca18a5b2/tldextract-3.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/80/d8/75264c54cfa1371d2a42fb613c24d71628c411764ab0d5046b54ca18a5b2/tldextract-3.3.1.tar.gz
Summary  : Accurately separates a URL's subdomain, domain, and public suffix, using the Public Suffix List (PSL). By default, this includes the public ICANN TLDs and their exceptions. You can optionally support the Public Suffix List's private domains as well.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-tldextract-bin = %{version}-%{release}
Requires: pypi-tldextract-license = %{version}-%{release}
Requires: pypi-tldextract-python = %{version}-%{release}
Requires: pypi-tldextract-python3 = %{version}-%{release}
Requires: pypi(requests_file)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(filelock)
BuildRequires : pypi(idna)
BuildRequires : pypi(py)
BuildRequires : pypi(requests)
BuildRequires : pypi(requests_file)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

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
%setup -q -n tldextract-3.3.1
cd %{_builddir}/tldextract-3.3.1
pushd ..
cp -a tldextract-3.3.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657313213
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-tldextract
cp %{_builddir}/tldextract-3.3.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-tldextract/b8641358e21254308b9a6258fc93eed20c9f7960
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
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
