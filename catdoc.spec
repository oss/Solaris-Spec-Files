Summary: MSWord .doc viewer
Name: catdoc
Version: 0.94
Release: 2
Group: Applications/Text
Copyright: GPL
Source: catdoc-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Vendor: NBCS-OSS
Packager: Hardik Varia <hvaria@nbcs@rutgers.edu>

%description
Catdoc is a viewer for MS-Word .doc files.

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
 LDFLAGS="-L/usr/local/lib -R/usr/local/lib" CPPFLAGS="-I/usr/local/include" \
 ./configure --prefix=/usr/local --sysconfdir=/etc
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local sysconfdir=$RPM_BUILD_ROOT/etc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc COPYING README TODO NEWS
/usr/local/bin/catdoc
/usr/local/bin/wordview
/usr/local/bin/catppt
/usr/local/bin/xls2csv
/usr/local/man/man1/catdoc.1
/usr/local/man/man1/catppt.1
/usr/local/man/man1/wordview.1
/usr/local/man/man1/xls2csv.1
/usr/local/share/catdoc/8859-1.txt
/usr/local/share/catdoc/8859-10.txt
/usr/local/share/catdoc/8859-11.txt
/usr/local/share/catdoc/8859-13.txt
/usr/local/share/catdoc/8859-14.txt
/usr/local/share/catdoc/8859-15.txt
/usr/local/share/catdoc/8859-2.txt
/usr/local/share/catdoc/8859-3.txt
/usr/local/share/catdoc/8859-4.txt
/usr/local/share/catdoc/8859-5.txt
/usr/local/share/catdoc/8859-6.txt
/usr/local/share/catdoc/8859-7.txt
/usr/local/share/catdoc/8859-8.txt
/usr/local/share/catdoc/8859-9.txt
/usr/local/share/catdoc/ascii.replchars
/usr/local/share/catdoc/ascii.specchars
/usr/local/share/catdoc/cp1250.txt
/usr/local/share/catdoc/cp1251.txt
/usr/local/share/catdoc/cp1252.txt
/usr/local/share/catdoc/cp1253.txt
/usr/local/share/catdoc/cp1254.txt
/usr/local/share/catdoc/cp1255.txt
/usr/local/share/catdoc/cp1256.txt
/usr/local/share/catdoc/cp1257.txt
/usr/local/share/catdoc/cp1258.txt
/usr/local/share/catdoc/cp437.txt
/usr/local/share/catdoc/cp850.txt
/usr/local/share/catdoc/cp852.txt
/usr/local/share/catdoc/cp855.txt
/usr/local/share/catdoc/cp857.txt
/usr/local/share/catdoc/cp860.txt
/usr/local/share/catdoc/cp861.txt
/usr/local/share/catdoc/cp862.txt
/usr/local/share/catdoc/cp863.txt
/usr/local/share/catdoc/cp864.txt
/usr/local/share/catdoc/cp865.txt
/usr/local/share/catdoc/cp866.txt
/usr/local/share/catdoc/cp869.txt
/usr/local/share/catdoc/cp874.txt
/usr/local/share/catdoc/koi8-r.txt
/usr/local/share/catdoc/koi8-u.txt
/usr/local/share/catdoc/mac-arabic.txt
/usr/local/share/catdoc/mac-centeuro.txt
/usr/local/share/catdoc/mac-cyrillic.txt
/usr/local/share/catdoc/mac-greek.txt
/usr/local/share/catdoc/mac-hebrew.txt
/usr/local/share/catdoc/mac-roman.txt
/usr/local/share/catdoc/tex.replchars
/usr/local/share/catdoc/tex.specchars
/usr/local/share/catdoc/us-ascii.txt
/usr/local/share/catdoc/x-mac-cyrillic.txt							 
