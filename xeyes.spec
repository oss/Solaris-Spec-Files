Name: xeyes
Version: 1
Release: 2
Summary: Xeyes observes you.
Group: Amusements/Games
Copyright: Freely distributable
Source: xeyes.tar.gz
BuildRoot: /var/tmp/%{name}-root


%description
Xeyes observes you.

%prep
%setup -q -n xeyes

%build
xmkmf -a
make CC=gcc PICFLAGS="-fpic" CDEBUGFLAGS="-g" CCOPTIONS="-O"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
cp xeyes $RPM_BUILD_ROOT/usr/local/bin
cp xeyes.man $RPM_BUILD_ROOT/usr/local/man/man1/xeyes.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/bin/xeyes
/usr/local/man/man1/xeyes.1
