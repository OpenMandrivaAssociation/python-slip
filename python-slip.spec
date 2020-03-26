Summary:	Miscellaneous convenience, extension and workaround code for Python
Name:		python-slip
Version:	0.6.5
Release:	1
License:	GPLv2+
Group:		Development/Python
Url:		https://github.com/nphilipp/python-slip
Source0:	https://github.com/nphilipp/python-slip/releases/download/python-slip-%{version}/python-slip-%{version}.tar.bz2
BuildRequires:	pkgconfig(python3)
Requires:	python3-six
BuildArch:	noarch

%description
The Simple Library for Python packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides the "slip" and the "slip.util" modules.
#----------------------------------------------------------------------------

%package -n python3-slip
Summary:	Convenience, extension and workaround code for Python 3.x
Group:		Development/Python

%description -n python3-slip
The Simple Library for Python 3.x packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides the "slip" and the "slip.util" modules.

%files -n python3-slip
%doc COPYING doc/dbus
%dir %{python3_sitelib}/slip/
%{python3_sitelib}/slip/__pycache__
%{python3_sitelib}/slip/__init__.py*
%{python3_sitelib}/slip/util
%{python3_sitelib}/slip/_wrappers
%{python3_sitelib}/slip-%{version}-py%{python3_version}.egg-info

#----------------------------------------------------------------------------

%package -n python3-slip-dbus
Summary:	Convenience functions for dbus services in Python 3.x
Group:		Development/Python
Requires:	python3-slip = %{EVRD}
Requires:	python3-dbus >= 0.80
# Don't require any of pygobject2/3 because slip.dbus works with either one. In
# theory users of slip.dbus should require one or the other anyway to use the
# main loop.
Requires:	python3-decorator
Requires:	python3-six

%description -n python3-slip-dbus
The Simple Library for Python 3.x packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides slip.dbus.service.Object, which is a dbus.service.Object
derivative that ends itself after a certain time without being used and/or if
there are no clients anymore on the message bus, as well as convenience
functions and decorators for integrating a dbus service with PolicyKit.

%files -n python3-slip-dbus
%doc doc/dbus/*
%{python3_sitelib}/slip/dbus
%{python3_sitelib}/slip.dbus-%{version}-py%{python3_version}.egg-info

#----------------------------------------------------------------------------

%prep
%autosetup -p1
find . -name '*.py' -o -name '*.py.in' | xargs sed -i '1s|^#!/usr/bin/python|#!%{__python3}|'

%build
%make_build PYTHON=%__python3

%install
%make_install PYTHON=%__python3
