# This is heavily based on the specfile included with gnome-python.

%define python_ver 1.6
%define pygtk_ver 0.6.6
%define pygnome_ver 1.0.53

Summary: The sources for the PyGTK and PyGNOME Python extension modules.
Name: gnome-python
Version: %{pygnome_ver}
Release: 3
Group: System Environment/Libraries
Copyright: LGPL
Source: gnome-python-%{pygnome_ver}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: gtk+ gnome-libs libglade gnome-applets
Requires: pygtk = %{pygtk_ver}
BuildRequires: gtk+-devel gnome-libs-devel libglade-devel gnome-applets 
BuildRequires: python >= %{python_ver}

%description
The gnome-python package contains the source packages for the Python
bindings for GTK+ and GNOME (PyGTK and PyGNOME, respectively). 

PyGTK is an extension module for Python that provides access to the
GTK+ widget set. Just about anything (within reason) you can write in
C with GTK+, you can write in Python with PyGTK, but with all of
Python's benefits.

PyGNOME is an extension module for Python that provides access to the
base GNOME libraries, so you have access to more widgets, a simple
configuration interface, and metadata support.

%package -n pygtk
Version: %{pygtk_ver}
Summary: Python bindings for the GTK+ widget set.
Group: Development/Languages
Requires: glib, imlib, python >= %{python_ver}
Requires: gtk+ >= 1.2.6

%description -n pygtk
PyGTK is an extension module for Python that gives you access to the
GTK+ widget set.  Just about anything you can write in C with GTK+ you
can write in Python with PyGTK (within reason), but with all of
Python's benefits. PyGTK provides an object-oriented interface at a
slightly higher level than the C interface. The PyGTK interface does
all of the type casting and reference counting that you'd have to do
yourself using the C API.

Install pygtk if you need Python bindings for the GTK+ widget set.

%package -n pygtk-libglade
Version: %{pygtk_ver}
Summary: A wrapper for the libglade library for use with PyGTK
Group: Development/Languages
Requires: pygtk = %{pygtk_ver}

%description -n pygtk-libglade
This module contains a wrapper for the libglade library.  Libglade is a
library similar to the pyglade module, except that it is written in C (so
is faster) and is more complete.

%package -n pygnome-libglade
Version: %{pygnome_ver}
Summary: GNOME support for the libglade python wrapper
Group: Development/Languages
Requires: pygnome = %{pygnome_ver}
Requires: pygtk-libglade = %{pygtk_ver}

%description -n pygnome-libglade
This module contains GNOME support to suppliment the libglade python
wrapper.  Libglade is a library similar to the pyglade module, except
that it is written in C (so is faster) and is more complete.

%package -n pygnome
Version: %{pygnome_ver}
Summary: Python bindings for the GNOME libraries.
Group: Development/Languages
Requires: pygtk = %{pygtk_ver}
Requires: gnome-libs

%description -n pygnome
PyGNOME is an extension module for python that gives you access to the
base GNOME libraries.  This means you have access to more widgets, simple
configuration interface, metadata support and many other features.

Install pygnome if you need Python bindings for the GNOME libraries.

%package -n pygnome-applet
Version: %{pygnome_ver}
Summary: Python bindings for GNOME Panel applets.
Group: Development/Languages
Requires: pygnome = %{pygnome_ver}

%description -n pygnome-applet
This module contains a wrapper that allows GNOME Panel applets to be
written in Python.

%package -n pygnome-capplet
Version: %{pygnome_ver}
Summary: Python bindings for GNOME Panel applets.
Group: Development/Languages
Requires: pygnome = %{pygnome_ver}

%description -n pygnome-capplet
This module contains a wrapper that allows GNOME Control Center
capplets to be in Python.

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
 LDFLAGS="-L/usr/local/lib -R/usr/local/lib" CPPFLAGS="-I/usr/local/include" \
 ./configure --prefix=/usr/local --disable-numpy
make

%install
build_dir=`pwd`
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files -n pygtk
%defattr(-,bin,bin)
/usr/local/include/pygtk
/usr/local/lib/python%{python_ver}/site-packages/gtk.py*
/usr/local/lib/python%{python_ver}/site-packages/Gtkinter.py*
/usr/local/lib/python%{python_ver}/site-packages/GtkExtra.py*
/usr/local/lib/python%{python_ver}/site-packages/GTK.py*
/usr/local/lib/python%{python_ver}/site-packages/GDK.py*
/usr/local/lib/python%{python_ver}/site-packages/GdkImlib.py*
/usr/local/lib/python%{python_ver}/site-packages/pyglade/*.py*

%doc pygtk/AUTHORS pygtk/NEWS pygtk/README pygtk/MAPPING pygtk/ChangeLog
%doc pygtk/description.py pygtk/examples

%files -n pygtk-libglade
%defattr(-,bin,bin)
/usr/local/lib/python%{python_ver}/site-packages/libglade.py*
/usr/local/lib/python%{python_ver}/site-packages/_libglademodule.so

%files -n pygnome-libglade
%defattr(-,bin,bin)
/usr/local/lib/python%{python_ver}/site-packages/_gladegnomemodule.so

%files -n pygnome-applet
%defattr(-,bin,bin)
/usr/local/lib/python%{python_ver}/site-packages/_appletmodule.so
/usr/local/lib/python%{python_ver}/site-packages/gnome/applet.py*

%files -n pygnome-capplet
%defattr(-,bin,bin)
/usr/local/lib/python%{python_ver}/site-packages/_cappletmodule.so
/usr/local/lib/python%{python_ver}/site-packages/gnome/capplet.py*

%files -n pygnome
%defattr(-,bin,bin)
/usr/local/lib/python%{python_ver}/site-packages/gettext.py*
/usr/local/lib/python%{python_ver}/site-packages/gnome/__init__.py*
/usr/local/lib/python%{python_ver}/site-packages/gnome/affine.py*
/usr/local/lib/python%{python_ver}/site-packages/gnome/config.py*
/usr/local/lib/python%{python_ver}/site-packages/gnome/file.py*
/usr/local/lib/python%{python_ver}/site-packages/gnome/help.py*
/usr/local/lib/python%{python_ver}/site-packages/gnome/history.py*
/usr/local/lib/python%{python_ver}/site-packages/gnome/metadata.py*
/usr/local/lib/python%{python_ver}/site-packages/gnome/mime.py*
/usr/local/lib/python%{python_ver}/site-packages/gnome/score.py*
/usr/local/lib/python%{python_ver}/site-packages/gnome/triggers.py*
/usr/local/lib/python%{python_ver}/site-packages/gnome/ui.py*
/usr/local/lib/python%{python_ver}/site-packages/gnome/uiconsts.py*
/usr/local/lib/python%{python_ver}/site-packages/gnome/url.py*
/usr/local/lib/python%{python_ver}/site-packages/gnome/xmhtml.py*
/usr/local/lib/python%{python_ver}/site-packages/gnome/zvt.py*

/usr/local/lib/python%{python_ver}/site-packages/_gnomemodule.so
/usr/local/lib/python%{python_ver}/site-packages/_gnomeuimodule.so
/usr/local/lib/python%{python_ver}/site-packages/_zvtmodule.so
/usr/local/lib/python%{python_ver}/site-packages/_gtkxmhtmlmodule.so

%doc AUTHORS NEWS README ChangeLog
%doc pygnome/examples

