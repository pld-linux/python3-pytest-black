#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	pytest plugin to enable format checking with black
Summary(pl.UTF-8):	Wtyczka pytesta do sprawdzania formatowania przy użyciu modułu black
Name:		python3-pytest-black
Version:	0.6.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-black/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-black/pytest_black-%{version}.tar.gz
# Source0-md5:	7acfa0e0aaeed6f7bc164164f8594790
Patch0:		%{name}-pytest.patch
URL:		https://pypi.org/project/pytest-black/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
%if %{with tests}
BuildRequires:	python3-black >= 19.3b0
BuildRequires:	python3-pytest >= 6
BuildRequires:	python3-toml
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A pytest plugin to enable format checking with black
<https://github.com/ambv/black>.

%description -l pl.UTF-8
Wtyczka pytesta do sprawdzania formatowania przy użyciu modułu black
<https://github.com/ambv/black>.

%prep
%setup -q -n pytest_black-%{version}
%patch -P 0 -p1

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytest_black" \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/pytest_black.py
%{py3_sitescriptdir}/__pycache__/pytest_black.cpython-*.py[co]
%{py3_sitescriptdir}/pytest_black-%{version}-py*.egg-info
