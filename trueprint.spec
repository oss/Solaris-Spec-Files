Summary: GNU trueprint
Name: trueprint
Version: 5.2.1
Release: 2
Group: Applications/Printing
Copyright: GPL
Source: trueprint-5.2.1.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Trueprint is a general purpose program printing program.  It tries to
produce everything that anybody could need in a program printout
without the need for large numbers of switches or pipelines.
Trueprint can currently handle C, C++, Java, Perl, Verilog, shell
(including ksh), Pascal, pseudo C, report files (trueprint report
file, see NOTES), listing files, text files. [ from trueprint.1 ]

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
 LDFLAGS="-L/usr/local/lib -R/usr/local/lib" CPPFLAGS="-I/usr/local/include" \
 ./configure --prefix=/usr/local --sysconfdir=/etc
make trueprint
make check

%install
rm -rf $RPM_BUILD_ROOT
for i in bin man/man1 lib info ; do
    mkdir -p $RPM_BUILD_ROOT/usr/local/$i
done
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/trueprint.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/trueprint.info
fi

%files
%defattr(-,bin,bin)
%doc BUGS README COPYING NEWS
/usr/local/bin/trueprint
/usr/local/man/man1/trueprint.1
/usr/local/lib/printers
/usr/local/info/trueprint.info
