Summary: Adobe Acrobat Reader
Name: acroread
Version: 4.05
Release: 3
Group: Applications/Printing
License: Commercial software
Source: sunsparc-rs-405.tar.gz
Provides: libAGM.so libAGM.so.3.0 libCoolType.so libCoolType.so.1.0 libICC.so
Provides: libICC.so.1.0 libreadcore.so libreadcore.so.4.0
BuildRoot: /var/tmp/%{name}-root

%description
Acroread is a PDF viewer.

%prep
%setup -q -n SSOLRS.install

%install
PREFIX="/opt/Acrobat4"
DESTDIR="%{buildroot}$PREFIX"

umask 022
rm -rf %{buildroot}
mkdir -p $DESTDIR

for i in READ.TAR SEARCH.TAR SSOLR.TAR SSOLS.TAR ; do
    (cd $DESTDIR && tar xf -) < $i
done

ed -s "$DESTDIR/bin/acroread.sh" <<__EOF__
  1,\$s@REPLACE_ME@$PREFIX/Reader@
  w
  q
__EOF__
mv $DESTDIR/bin/acroread.sh $DESTDIR/bin/acroread
chmod 755 $DESTDIR/bin/acroread

mkdir -p %{buildroot}/usr/local/bin
ln -s /opt/Acrobat4/bin/acroread %{buildroot}/usr/local/bin/acroread4

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,bin)
%doc LICREAD.TXT ReadMe
/opt/Acrobat4/Reader
/opt/Acrobat4/ReadMe
/opt/Acrobat4/bin/acroread
/opt/Acrobat4/Resource/Font/*
/opt/Acrobat4/Browsers/netscape
/opt/Acrobat4/Browsers/sparcsolaris/*
/usr/local/bin/acroread4
