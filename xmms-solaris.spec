Name: xmms-solaris
Version: 0.5.0
Release: 2
Summary: xmms plugin for Solaris
Copyright: GPL
Group: Applications/Productivity
Source: xmms-solaris-0.5.0.tar.gz
Requires: xmms
Provides: libSolaris.so
BuildRoot: /var/tmp/%{name}-root

%description
The xmms-solaris plugin for xmms lets you listen to mp3s (with xmms)
on your Solaris workstation.

%prep
%setup -q

%build
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export LDFLAGS
./configure
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/lib/xmms/Output
cd src/.libs
for i in libSolaris.* ; do
    install -m 0755 $i $RPM_BUILD_ROOT/usr/local/lib/xmms/Output/$i
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, bin, bin)
/usr/local/lib/xmms/Output/libSolaris.la
/usr/local/lib/xmms/Output/libSolaris.so
