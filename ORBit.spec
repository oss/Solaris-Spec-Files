Summary: High-performance CORBA Object Request Broker
Name: ORBit
Version: 0.5.5
Release: 2
Group: System Environment/Libraries
Copyright: LGPL/GPL
Source: ORBit-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: glib >= 1.2.8
BuildRequires: flex
BuildRequires: gettext

%description
ORBit is a high-performance CORBA (Common Object Request Broker 
Architecture) ORB (object request broker). It allows programs to 
send requests and receive replies from other programs, regardless 
of the locations of the two programs. CORBA is an architecture that 
enables communication between program objects, regardless of the 
programming language they're written in or the operating system they
run on.

You will need to install this package if you want to run programs that use
the ORBit implementation of CORBA technology.

This package was build -without- TCP wrappers.

%package devel
Summary: Development libraries, header files and utilities for ORBit.
Group: Development/Libraries
Requires: indent
Requires: glib
Requires: ORBit = %{version}

%description devel
This package contains the header files, libraries and utilities 
necessary to write programs that use CORBA technology. If you want to
write such programs, you'll also need to install the ORBit package.


%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
    LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
    ./configure --enable-shared --enable-static \
    --with-glib-prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%post devel
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/libIDL.info
fi

%preun devel
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/libIDL.info
fi

%files
%defattr(-,bin,bin)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%doc libIDL/COPYING libIDL/ChangeLog libIDL/AUTHORS
%doc libIDL/README* libIDL/NEWS libIDL/BUGS libIDL/tstidl.c
/usr/local/lib/lib*.so*
/usr/local/bin/orbit-event-server
/usr/local/bin/orbit-name-server
/usr/local/bin/name-client
/usr/local/bin/orbit-ird

%files devel
%defattr(-,bin,bin)
/usr/local/bin/orbit-idl
/usr/local/bin/orbit-config
/usr/local/bin/libIDL-config
/usr/local/include/*
/usr/local/info/*info*
/usr/local/lib/*.sh
/usr/local/lib/lib*a
/usr/local/share/aclocal/*

