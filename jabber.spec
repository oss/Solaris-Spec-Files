Summary: Jabber chat server
Name: jabberd
Version: 1.4.1
Release: 1

%define nam_ver jabber-%{version}

Group: Applications/Productivity
License: JOSL, LGPL
Source: %{nam_ver}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Jabber is an instant-messaging system similar to AIM.  This package
contains a jabber server.

%prep
%setup -q -n %{nam_ver}

%build
./configure
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/%{nam_ver}
find . | cpio -pdmuv $RPM_BUILD_ROOT/usr/local/%{nam_ver}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/%{nam_ver}


