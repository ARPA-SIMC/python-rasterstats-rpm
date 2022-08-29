%if 0%{?rhel} == 7
%define python3_vers python36
%else
%define python3_vers python3
%endif

Name:           python-rasterstats
Version:        0.17.0
Release:        1%{?dist}
Summary:        Summarize geospatial raster datasets based on vector geometries

License:        Apache License, Version 2.0
URL:            https://github.com/perrygeo/python-rasterstats
Source0:        https://github.com/perrygeo/python-rasterstats/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  %{python3_vers}-devel
BuildRequires:  %{python3_vers}-setuptools
BuildRequires:  %{python3_vers}-affine < 3
BuildRequires:  %{python3_vers}-shapely
BuildRequires:  %{python3_vers}-numpy >= 1.9
BuildRequires:  %{python3_vers}-rasterio >= 1.0
BuildRequires:  %{python3_vers}-cligj >= 0.4
BuildRequires:  %{python3_vers}-fiona
BuildRequires:  %{python3_vers}-simplejson
BuildRequires:  gdal-devel
BuildRequires:  python3-pytest

Requires:       %{python3_vers}-affine < 3
Requires:       %{python3_vers}-shapely
Requires:       %{python3_vers}-numpy >= 1.9
Requires:       %{python3_vers}-rasterio >= 1.0
Requires:       %{python3_vers}-cligj >= 0.4
Requires:       %{python3_vers}-fiona
Requires:       %{python3_vers}-simplejson

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
%autosetup -n python-rasterstats-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest -v

%files -n %{python3_vers}-rasterstats
%{python3_sitelib}/*


%changelog
* Mon Aug 29 2022 Emanuele Di Giacomo <edigiacomo@arpae.it> - 0.17.0-1
- New version

* Thu Aug 25 2022 Emanuele Di Giacomo <edigiacomo@arpae.it> - 0.13.1-2
- Removed python 2 support

* Wed Oct 16 2019 Daniele Branchini <dbranchini@arpae.it> - 0.13.1-1
- Initial package
