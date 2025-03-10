#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	pytest plugin to enable format checking with black
Summary(pl.UTF-8):	Wtyczka pytesta do sprawdzania formatowania przy użyciu modułu black
Name:		python-pytest-black
Version:	0.3.12
Release:	5
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-black/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-black/pytest-black-%{version}.tar.gz
# Source0-md5:	5c44840754f9edfb5c775768aa07990a
Patch0:		%{name}-pytest.patch
URL:		https://pypi.org/project/pytest-black/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
%if %{with tests}
BuildRequires:	python-pytest >= 3.5.0
BuildRequires:	python-toml
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
%if %{with tests}
BuildRequires:	python3-black >= 19.3b0
BuildRequires:	python3-pytest >= 6
BuildRequires:	python3-toml
%endif
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

%package -n python3-pytest-black
Summary:	pytest plugin to enable format checking with black
Summary(pl.UTF-8):	Wtyczka pytesta do sprawdzania formatowania przy użyciu modułu black
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.6

%description -n python3-pytest-black
A pytest plugin to enable format checking with black
<https://github.com/ambv/black>.

%description -n python3-pytest-black -l pl.UTF-8
Wtyczka pytesta do sprawdzania formatowania przy użyciu modułu black
<https://github.com/ambv/black>.

%prep
%setup -q -n pytest-black-%{version}
%patch -P 0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytest_black" \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytest_black" \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py_sitescriptdir}/pytest_black.py[co]
%{py_sitescriptdir}/pytest_black-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytest-black
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/pytest_black.py
%{py3_sitescriptdir}/__pycache__/pytest_black.cpython-*.py[co]
%{py3_sitescriptdir}/pytest_black-%{version}-py*.egg-info
%endif
