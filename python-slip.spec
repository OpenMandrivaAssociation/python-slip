# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(0)")}
%{!?python_version: %global python_version %(%{__python} -c "from distutils.sysconfig import get_python_version; print get_python_version()")}

Name:       python-slip
Version:    0.2.24
Release:    1
Summary:    Miscellaneous convenience, extension and workaround code for Python

Group:      System/Libraries
License:    GPLv2+
URL:        http://fedorahosted.org/python-slip
Source0:    http://fedorahosted.org/released/python-slip/%{name}-%{version}.tar.bz2
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

BuildRequires:  python
BuildRequires:  python-devel

Requires: python-selinux

%description
The Simple Library for Python packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides the "slip" and the "slip.util" modules.

%package dbus
Summary:    Convenience functions for dbus services
Group:      System/Libraries
Requires:   %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:   dbus-python >= 0.80
Requires:   python-gobject
Requires:   policykit
Requires:   polkit >= 0.94
Requires:   python-decorator

%description dbus
The Simple Library for Python packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides slip.dbus.service.Object, which is a dbus.service.Object
derivative that ends itself after a certain time without being used and/or if
there are no clients anymore on the message bus, as well as convenience
functions and decorators for integrating a dbus service with PolicyKit.

%package gtk
Summary:    Code to make auto-wrapping gtk labels
Group:      System/Libraries
Requires:   %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:   pygtk2.0

%description gtk
The Simple Library for Python packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides slip.gtk.set_autowrap(), a convenience function which
lets gtk labels be automatically re-wrapped upon resizing.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
rm -rf %buildroot
make install DESTDIR=%buildroot

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%doc COPYING doc/dbus
%dir %{python_sitelib}/slip/
%{python_sitelib}/slip/__init__.py*
%{python_sitelib}/slip/util
%{python_sitelib}/slip/_wrappers
%{python_sitelib}/slip-%{version}-py%{python_version}.egg-info

%files dbus
%defattr(-,root,root,-)
%doc doc/dbus/*
%{python_sitelib}/slip/dbus
%{python_sitelib}/slip.dbus-%{version}-py%{python_version}.egg-info

%files gtk
%defattr(-,root,root,-)
%{python_sitelib}/slip/gtk
%{python_sitelib}/slip.gtk-%{version}-py%{python_version}.egg-info

%changelog
* Thu Aug 11 2011 Александр Казанцев <kazancas@mandriva.org> 0.2.17-1mdv2011.0
+ Revision: 694012
- Update to 0.2.17. Prevent dbus timeout error

* Fri May 27 2011 Александр Казанцев <kazancas@mandriva.org> 0.2.14-1
+ Revision: 680332
- adapt for Mandriva
- imported package python-slip


