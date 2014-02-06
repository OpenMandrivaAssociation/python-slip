# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(0)")}
%{!?python_version: %global python_version %(python -c "from distutils.sysconfig import get_python_version; print get_python_version()")}

Summary:	Miscellaneous convenience, extension and workaround code for Python
Name:		python-slip
Version:	0.6.0
Release:	1
Group:		System/Libraries
License:	GPLv2+
Url:		http://fedorahosted.org/python-slip
Source0:	http://fedorahosted.org/released/python-slip/%{name}-%{version}.tar.bz2
Patch0:		python-slip-0.2.24-selinux.patch
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
Obsoletes:	policykit

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

%package gtk
Summary:	Code to make auto-wrapping gtk labels
Group:		System/Libraries
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	pygtk2.0

%description gtk
The Simple Library for Python packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides slip.gtk.set_autowrap(), a convenience function which
lets gtk labels be automatically re-wrapped upon resizing.

%prep
%setup -q
%apply_patches

%build
%make

%install
%makeinstall_std

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

%files gtk
%{py_puresitedir}/slip/gtk
%{py_puresitedir}/slip.gtk-%{version}-py%{py_ver}.egg-info


