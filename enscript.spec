Summary: Imitation nenscript text to postscript filter
Name: enscript
Version: 1.6.1
Release: 2
Group: Applications/Printing
License: GPL
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
%description
GNU enscript is a drop-in replacement for the enscript program.
Enscript converts ASCII files to PostScript and stores generated output
to a file or sends it directly to the printer.

  [ from README ]

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld" LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
  ./configure --with-media=Letter
make
make check

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%post
cat <<EOF
To finish this installation, edit and copy /usr/local/etc/enscript.cfg.rpm.
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ABOUT-NLS AUTHORS COPYING FAQ.html NEWS README README.ESCAPES THANKS TODO
/usr/local/share/enscript
/usr/local/etc/*
/usr/local/bin/*
/usr/local/man/man1/*
/usr/local/lib/locale/*/LC_MESSAGES/enscript.mo
