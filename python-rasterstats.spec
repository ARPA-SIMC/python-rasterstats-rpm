%if 0%{?rhel} == 7
%define python3_vers python36
%else
%define python3_vers python3
%endif

Name:           python-rasterstats
Version:        0.13.1
Release:        1%{?dist}
Summary:        Summarize geospatial raster datasets based on vector geometries

License:        Apache License, Version 2.0
URL:            https://pypi.org/project/rasterstats/
Source0:        https://files.pythonhosted.org/packages/source/r/rasterstats/rasterstats-%{version}.tar.gz#/python-rasterstats-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  %{python3_vers}-devel

%description
Rasterstats is a Python module for summarizing geospatial raster datasets based on vector geometries.
It includes functions for zonal statistics and interpolated point queries.
The command-line interface allows for easy interoperability with other GeoJSON tools.


%package     -n %{python3_vers}-rasterstats
Summary:        Summarize geospatial raster datasets based on vector geometries


%description -n %{python3_vers}-rasterstats
Rasterstats is a Python module for summarizing geospatial raster datasets based on vector geometries.
It includes functions for zonal statistics and interpolated point queries.
The command-line interface allows for easy interoperability with other GeoJSON tools.

%prep
%autosetup -n rasterstats-%{version}

rm -rf %{py3dir}
cp -a . %{py3dir}

%build
%{__python2} setup.py build
pushd %{py3dir}
%py3_build
popd

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
pushd %{py3dir}
%py3_install
popd

%check
%{__python2} setup.py test
pushd %{py3dir}
%{__python3} setup.py test
popd

%files
%{python2_sitelib}/*

%files -n %{python3_vers}-rasterstats
%{python3_sitelib}/*


%changelog
* Wed Oct 16 2019 Daniele Branchini <dbranchini@arpae.it> - 0.13.1-1
- Initial package
