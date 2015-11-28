%define		pypi_name	iterutils
Summary:	Itertools recipes
Name:		python-%{pypi_name}
Version:	0.1.6
Release:	1
License:	PSF
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/i/iterutils/iterutils-%{version}.tar.gz
# Source0-md5:	e293044ec65d757ce075ac170ad9ada8
URL:		https://pypi.python.org/pypi/iterutils
BuildRequires:	python-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These functions have been taken from the recipes in the Python
documentation for itertools.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/%{pypi_name}.py[co]
%{py_sitescriptdir}/%{pypi_name}-%{version}-py*.egg-info
