Summary: Advanced music synthesis software
Name: Csound
Version: 4.07
Release: 2
Group: Applications/Multimedia
Copyright: free for noncommercial use
Source0: Csound.tar.gz
Source1: csound-html.tar.gz
Patch: Csound.patch
BuildRoot: /var/tmp/%{name}-root
BuildRequires: vpkg-SUNWaudmo infozip tcl tcl-tk
Requires: tcl tcl-tk

%description
Csound is an advanced synthesis engine that can be used to create
music.

%package devel
Summary: Csound headers and static libraries
Group: Development/Libraries

%description devel
Csound-devel contains the csound header files and static libraries;
you may want this package if you are developing applications that use
the Csound API.

%package doc
Summary: Csound manual
Group: Documentation

%description doc
Csound-doc contains the Csound manual.

%prep
%setup -n Csound -c -T
%setup -n Csound -D -T -a 0
%setup -n Csound -D -T -a 1
cp Makefile.sol Makefile
%patch -p1

%build
make
make csound.a
make makedb
./makedb english-strings English

%install
rm -rf $RPM_BUILD_ROOT
for i in include lib bin ; do
    mkdir -p $RPM_BUILD_ROOT/usr/local/$i
done
make install INCLUDE=$RPM_BUILD_ROOT/usr/local/include \
             LIB=$RPM_BUILD_ROOT/usr/local/lib \
             DEST=$RPM_BUILD_ROOT/usr/local/bin
install -m 0444 sysdep.h $RPM_BUILD_ROOT/usr/local/include
install -m 0444 English.txt $RPM_BUILD_ROOT/usr/local/lib/csound.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/lib/csound.txt

%files devel
%defattr(-,bin,bin)
/usr/local/include/*
/usr/local/lib/*a

%files doc
%defattr(-,bin,bin)
%doc csound-html/*
