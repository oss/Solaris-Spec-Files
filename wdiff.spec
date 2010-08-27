Summary: 	wdiff - Frontend to GNU diff
Name: 		wdiff
Version: 	0.6.3
Release: 	3
Group: 		System Environment/Base
License: 	GPL
URL: ftp://ftp.gnu.org/gnu/wdiff/
Source: ftp://ftp.gnu.org/gnu/wdiff/wdiff-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

%description
Compares two files on a word per word basis, finding the word deleted or added from the first file to make the 
second. A word is defined as anything between whitespace. It works by creating two temporary files, one word per 
line, and the executes 'diff' on these fields. It collects the 'diff' output and uses it to produce a nicer display 
of word differences between the original files. 

%prep
%setup -q

%build
%configure 
gmake

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
gmake install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/usr/local/share/info/dir
rm -rf $RPM_BUILD_ROOT/usr/local/lib/charset.alias

%post
if [ -x /usr/local/bin/install-info ] ; then
        /usr/local/bin/install-info --info-dir=%{_infodir} \
                 %{_infodir}/%{name}.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
        /usr/local/bin/install-info --delete --info-dir=%{_infodir} \
                 %{_infodir}/%{name}.info
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)  
/usr/local/bin/*
/usr/local/share/info/*
/usr/local/share/man/man*/*
%doc AUTHORS COPYING ChangeLog NEWS README TODO THANKS

%changelog
* Tue Aug 24 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu>
- Fix preun scriptlet

* Wed Aug 18 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.6.3-2
- Don't package /usr/local/lib/charset.alias
- Update info scriptlets

* Fri Aug 06 2010 Steven Lu <sjlu@nbcs.rutgers.edu> - 0.6.3-1
- bump to 0.6.3, spec file update
