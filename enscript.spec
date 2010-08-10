Summary:    Imitation nenscript text to postscript filter
Name:       enscript
Version:    1.6.5.2
Release:    1
Group:      Applications/Printing
License:    GPL
URL:        http://ftp.gnu.org/gnu/enscript/
Source:     http://ftp.gnu.org/gnu/enscript/%{name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
GNU enscript is a drop-in replacement for the enscript program.
Enscript converts ASCII files to PostScript and stores generated output
to a file or sends it directly to the printer.

  [ from README ]

%prep
%setup -q

%build
%configure --with-media=Letter

gmake -j3

%check
gmake check

%install
rm -rf $RPM_BUILD_ROOT
gmake install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_libdir}/charset.alias
rm -f $RPM_BUILD_ROOT%{_localedir}/locale.alias


%find_lang %{name}

%post
cat <<EOF
To finish this installation, edit and copy /usr/local/etc/enscript.cfg.rpm.
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc ABOUT-NLS AUTHORS COPYING FAQ.html NEWS README README.ESCAPES THANKS TODO
%{_datadir}/enscript/
%{_sysconfdir}/*
%{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/%{name}.info

%changelog
* Mon Aug 09 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.6.5.2-1
- Update to the latest version
