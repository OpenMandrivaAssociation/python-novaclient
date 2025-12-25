Name:		python-novaclient
Version:	18.11.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/python_novaclient/python_novaclient-%{version}.tar.gz
Summary:	Client library for OpenStack Compute API
URL:		https://pypi.org/project/python-novaclient/
License:	Apache License, Version 2.0
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pbr)
BuildSystem:	python
BuildArch:	noarch

%description
Client library for OpenStack Compute API

%files
%{_bindir}/nova
%{py_sitedir}/novaclient
%{py_sitedir}/python_novaclient-*.*-info
