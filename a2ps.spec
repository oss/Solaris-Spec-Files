Name:          a2ps
Version:       4.14
Release:       1
License:       GPL
Group:         Applications/Printing
Summary:       ASCII to PS
URL:           http://ftp.gnu.org/gnu/a2ps/
Source:        http://ftp.gnu.org/gnu/a2ps/a2ps-%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: psutils
Requires:      gs-fonts psutils

%description
   a2ps formats files for printing on a PostScript printer.

   The format used is nice and compact: normally two pages on each
physical page, borders surrounding pages, headers with useful
information (page number, printing date, file name or supplied header),
line numbering, pretty-printing, symbol substitution etc.  This is very
useful for making archive listings of programs or just to check your
code in the bus.  Actually a2ps is kind of boostrapped: its sources are
frequently printed with a2ps `:)'.

   While at the origin its names was derived from "ASCII to PostScript",
today we like to think of it as "Any to PostScript".  Indeed, a2ps
supports "delegations", i.e., you can safely use a2ps to print DVI,
PostScript, LaTeX, JPEG etc., even compressed.

       [from the Info documentation]

%package devel
Summary:        Development files for a2ps
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains development libraries and headers for a2ps.

%prep
%setup -q

# Very weird syntax. Solaris compiler doesn't like these lines
sed -i 's/.*\(configure-time declaration test was not run\).*/#warning "\1"/' lib/strtoimax.c

%build
%configure --enable-shared --disable-static
gmake

%install
rm -rf $RPM_BUILD_ROOT
gmake install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT/%{_infodir}/dir
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la


%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=%{_infodir} \
		 %{_infodir}/ogonkify.info
	/usr/local/bin/install-info --info-dir=%{_infodir} \
		 %{_infodir}/a2ps.info
	/usr/local/bin/install-info --info-dir=%{_infodir} \
		 %{_infodir}/regex.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=%{_infodir} \
		 %{_infodir}/ogonkify.info
	/usr/local/bin/install-info --delete --info-dir=%{_infodir} \
		 %{_infodir}/a2ps.info
	/usr/local/bin/install-info --delete --info-dir=%{_infodir} \
		 %{_infodir}/regex.info
fi

%files
%defattr(-,root,root,-)
%doc ANNOUNCE AUTHORS COPYING ChangeLog FAQ HACKING NEWS README THANKS TODO
%{_datadir}/a2ps
%{_datadir}/ogonkify
%{_datadir}/emacs/site-lisp/*.el*
%{_sysconfdir}/*
%{_infodir}/*.info*
%{_mandir}/man1/*
%{_bindir}/*
%{_libdir}/lib*.so.*


%files devel
%defattr(-,root,root,-)
%{_libdir}/lib*.so
%{_includedir}/liba2ps.h

%changelog
* Tue Aug 17 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 4.14-1
- Update to the latest version
