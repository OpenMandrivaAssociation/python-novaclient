%define module novaclient
%define oname python_novaclient

Name:		python-novaclient
Version:	18.12.0
Release:	1
Summary:	Client library for OpenStack Compute API
License:	Apache License, Version 2.0
Group:		Development/Python
URL:		https://pypi.org/project/python-novaclient/
Source0:	https://files.pythonhosted.org/packages/source/p/%{oname}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pbr)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Client library for OpenStack Compute API

%files
%{_bindir}/nova
%{py_sitedir}/%{module}
%{py_sitedir}/%{oname}-%{version}.dist-info
