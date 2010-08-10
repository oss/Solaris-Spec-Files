Name:          indent
Version:       2.2.10
Release:       1
License:       GPL
Group:         Development/Tools
Summary:       indent is a C beautifier
Source:        http://ftp.gnu.org/gnu/indent/indent-%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Indent is a program that reformats C code in several classic and modern
styles for your viewing pleasure.

%prep
%setup -q

%build
%configure

gmake

%install
rm -rf $RPM_BUILD_ROOT
gmake install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_datadir}/locale/locale.alias
rm -f $RPM_BUILD_ROOT%{_libdir}/charset.alias
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

mv $RPM_BUILD_ROOT/usr/local/doc/indent/indent.html .

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/share/info \
	    /usr/local/share/info/indent.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/share/info \
	    /usr/local/share/info/indent.info
fi

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING indent.html
%{_bindir}/indent
%{_bindir}/texinfo2man

%{_infodir}/indent.info
%{_mandir}/man1/indent.1

%changelog
* Mon Aug 09 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 2.2.10-1
- Update to the latest version
