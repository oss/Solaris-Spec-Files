Summary: print multiple pages per sheet on a Postscript printer
Name: mpage
Version: 2.5.2
Release: 1
Group: Applications/Printing
License: BSD type
Source: %{name}-%{version}.tgz
BuildRoot: /var/tmp/%{name}-root
Conflicts: vpkg-SFWmpage

%description
Mpage reads plain text files or PostScript documents and prints them
on a PostScript printer with the text reduced in size so that several
pages appear on one sheet of paper.  This is useful for viewing large
printouts on a small amount of paper.  Uses ISO 8859.1 to print 8-bit
characters.

%prep
%setup -q

sed "s/PAGESIZE=A4/PAGESIZE=Letter/" Makefile > Makefile.cjs
mv Makefile.cjs Makefile

%build
make

%install
rm -rf $RPM_BUILD_ROOT
for i in lib/mpage bin man/man1 ; do
    mkdir -p $RPM_BUILD_ROOT/usr/local/$i
done
install -m 0555 mpage $RPM_BUILD_ROOT/usr/local/bin/mpage
install -m 0444 mpage.1 $RPM_BUILD_ROOT/usr/local/man/man1/mpage.1
for i in Encodings/* ; do
    install -m 0444 $i $RPM_BUILD_ROOT/usr/local/lib/mpage
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/bin/*
/usr/local/lib/mpage

%attr(-,bin,bin) /usr/local/man/man1/mpage.1




