Summary:	Miscellaneous convenience, extension and workaround code for Python
Name:		python-slip
Version:	0.6.0
Release:	5
Group:		System/Libraries
License:	GPLv2+
Url:		http://fedorahosted.org/python-slip
Source0:	http://fedorahosted.org/released/python-slip/%{name}-%{version}.tar.bz2
Patch0:		python-slip-0.2.24-selinux.patch
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
Obsoletes:	policykit
Requires:       python-six

%description
The Simple Library for Python packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides the "slip" and the "slip.util" modules.

%package dbus
Summary:	Convenience functions for dbus services
Group:		System/Libraries
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	python-dbus >= 0.80
Requires:	python-gobject
Requires:	polkit >= 0.94
Requires:	python-decorator

%description dbus
The Simple Library for Python packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides slip.dbus.service.Object, which is a dbus.service.Object
derivative that ends itself after a certain time without being used and/or if
there are no clients anymore on the message bus, as well as convenience
functions and decorators for integrating a dbus service with PolicyKit.

%package -n python2-slip
Summary:        Miscellaneous convenience, extension and workaround code for Python
Group:          System/Libraries
Requires:	python2-six

%description -n python2-slip
The Simple Library for Python packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides the "slip" and the "slip.util" modules.


%package -n python2-slip-dbus
Summary:        Convenience functions for dbus services
Group:          System/Libraries
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       python2-dbus >= 0.80
Requires:       python2-gobject
Requires:       polkit >= 0.94
Requires:       python2-decorator

%description -n python2-slip-dbus
The Simple Library for Python packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides slip.dbus.service.Object, which is a dbus.service.Object
derivative that ends itself after a certain time without being used and/or if
there are no clients anymore on the message bus, as well as convenience
functions and decorators for integrating a dbus service with PolicyKit.


%package -n python2-slip-gtk
Summary:	Code to make auto-wrapping gtk labels
Group:		System/Libraries
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	pygtk2.0

%description -n python2-slip-gtk
The Simple Library for Python packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides slip.gtk.set_autowrap(), a convenience function which
lets gtk labels be automatically re-wrapped upon resizing.

%prep
%setup -q
%apply_patches
cp -a . %{py2dir}
find %{py2dir} -name '*.py' -o -name '*.py.in' | xargs sed -i '1s|^#!/usr/bin/python|#!%{__python2}|'

%build
%make PYTHON=%__python

pushd %{py2dir}
%make PYTHON=%__python2

%install
%makeinstall_std PYTHON=%__python

pushd %{py2dir}
%makeinstall_std PYTHON=%__python2


%files
%doc COPYING doc/dbus
%dir %{py_puresitedir}/slip/
%{py_puresitedir}/slip/__init__.py*
%{py_puresitedir}/slip/util
%{py_puresitedir}/slip/_wrappers
%{py_puresitedir}/slip-%{version}-py%{py_ver}.egg-info

%files dbus
%doc doc/dbus/*
%{py_puresitedir}/slip/dbus
%{py_puresitedir}/slip.dbus-%{version}-py%{py_ver}.egg-info

%files -n python2-slip
%doc COPYING doc/dbus
%dir %{py2_puresitedir}/slip/
%{py2_puresitedir}/slip/__init__.py*
%{py2_puresitedir}/slip/util
%{py2_puresitedir}/slip/_wrappers
%{py2_puresitedir}/slip-%{version}-py%{py2_ver}.egg-info

%files -n python2-slip-dbus
%doc doc/dbus/*
%{py2_puresitedir}/slip/dbus
%{py2_puresitedir}/slip.dbus-%{version}-py%{py2_ver}.egg-info

%files -n python2-slip-gtk
%{py2_puresitedir}/slip/gtk
%{py2_puresitedir}/slip.gtk-%{version}-py%{py2_ver}.egg-info


