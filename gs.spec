Name: gs
Version: 6.01
Copyright: AFPL
Group: Applications/Publishing
Summary: Aladdin Ghostscript
Release: 8
Source0: ghostscript-%{version}.tar.gz
Source1: libpng-1.2.1.tar.gz
Source2: jpegsrc.v6b.tar.gz
Source3: zlib.tar.gz
Source4: ghostscript-fonts-std-6.0.tar.gz
Patch: gs.patch
Requires: gs-fonts
BuildRoot: /var/tmp/%{name}-root
BuildRequires: libpng
Requires: libpng
Conflicts: vpkg-SFWgs

%description 
Aladdin Ghostscript lets you print or view postscript files without a
postscript printer.  You need to install gs-fonts if you want to use
Ghostscript.

%package fonts
Summary: Ghostscript fonts
Group: Applications/Publishing

%description fonts
Gs-fonts contains the fonts used by Ghostscript.  

%prep
%setup -q -n gs%{version}
%setup -q -D -T -a 1 -n gs%{version}
%setup -q -D -T -a 2 -n gs%{version}
%setup -q -D -T -a 3 -n gs%{version}
%setup -q -D -T -a 4 -n gs%{version}

# The patch configures the makefile properly.
%patch -p1

cp src/unix-gcc.mak makefile

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local
tar cf - fonts | (cd $RPM_BUILD_ROOT/usr/local/share/ghostscript && tar xf -)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc doc/*
/usr/local/share/ghostscript/%{version}
/usr/local/bin/*
/usr/local/man/man1/*

%files fonts
%defattr(-,root,root)
/usr/local/share/ghostscript/fonts/*
